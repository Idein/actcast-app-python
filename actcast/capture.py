import fcntl
import threading
from queue import Queue, Full, Empty
import v4l2


class Capture(threading.Thread):
    def __init__(self, width, height, rotation, hflip, display, background, cmd):
        super(Capture, self).__init__()
        self.queue = Queue(1)
        self.camera = PiCamera()
        self.camera.rotation = rotation
        self.camera.hflip = hflip
        self.camera.resolution = (width, height)
        self.camera.framerate = 15
        self.event = threading.Event()
        self.event.clear()
        while not self.event.is_set():
            stream = io.BytesIO()
            self.camera.capture(stream, format='rgb', use_video_port=True)
            stream = io.BytesIO()
            self.camera.capture(stream, format='rgb', use_video_port=True)
            stream = io.BytesIO()
            self.camera.capture(stream, format='rgb', use_video_port=True)
            stream = io.BytesIO()
            self.camera.capture(stream, format='rgb', use_video_port=True)
            start = time.time()
            self.camera.capture(stream, format='rgb', use_video_port=True)
            if time.time() - start < 0.09: break
            self.camera.framerate += 1
            if self.camera.framerate >= 30: break
        self.display = display
        n = math.gcd(PREFFERED_DISPLAY_WIDTH, PREFFERED_DISPLAY_HEIGHT)
        black = np.zeros((32 * PREFFERED_DISPLAY_HEIGHT // n, 32 * PREFFERED_DISPLAY_WIDTH // n, 3), dtype=np.uint8)
        self.camera.add_overlay(black, size=(black.shape[1], black.shape[0]), layer=0, alpha=255)
        self.overlay = []
        if self.display:
            bg = self.camera.add_overlay(background, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT), layer=1, alpha=255)
            self.camera.start_preview(fullscreen=False, window = (OVERSCAN, OVERSCAN, PREVIEW_WIDTH, PREVIEW_HEIGHT), layer=3)
        self.cmd = cmd

    def run(self):
        try:
            while not self.event.is_set():
                stream = io.BytesIO()
                self.camera.capture(stream, format='rgb', use_video_port=True)
                image = np.asarray(bytearray(stream.getvalue()), dtype=np.uint8).reshape(IMAGENET_HEIGHT,IMAGENET_WIDTH,3)
                self.cmd.update_image(image)
                image = image.astype(np.float32)
                try:
                    self.queue.put(image, timeout=1)
                except Full:
                    pass
                except:
                    traceback.print_exc()
            if self.display:
                for ol in self.overlay:
                    self.camera.remove_overlay(ol)
                self.camera.stop_preview()
        except: # picamera.exc.PiCameraRuntimeError, etc...
            traceback.print_exc()

    def get(self):
        return self.queue.get(timeout=1)

    def stop(self):
        self.event.set()

    def update_overlay(self, src):
        if self.display:
            if not self.event.is_set():
                if True:
                    # double buffering
                    layer = self.camera.add_overlay(src, size=(UPDATE_AREA_WIDTH, UPDATE_AREA_HEIGHT), layer=2, alpha=255,
                                                    fullscreen=False, window=UPDATE_AREA_DISPLAY_WINDOW)
                    self.overlay.append(layer)
                    if len(self.overlay) > 1:
                        self.camera.remove_overlay(self.overlay.pop(0))
                else:
                    self.overlay[0].update(src)
