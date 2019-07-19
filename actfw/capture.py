import io
import time
from queue import Full
from .task import Producer
from actfw.v4l2.video import Video, V4L2_PIX_FMT


class Frame(object):

    """Captured Frame"""

    def __init__(self, value):
        self.value = value
        self.updatable = True

    def getvalue(self):
        """
        Get frame data.

        Returns:
            bytes: captured image data

        """
        self.updatable = False
        return self.value

    def _update(self, value):
        if self.updatable:
            self.value = value
            return True
        return False


class PiCameraCapture(Producer):

    """Captured Frame Producer for Raspberry Pi Camera Module"""

    def __init__(self, camera, *args, **kwargs):
        """

        Args:
            camera (:class:`~picamera.PiCamera`): picamera object

        """
        super(PiCameraCapture, self).__init__()
        self.camera = camera
        self.args = args
        self.kwargs = kwargs
        self.frames = []

    def run(self):
        """Run producer activity"""
        def generator():
            stream = io.BytesIO()
            while self._is_running():
                try:
                    yield stream
                    stream.seek(0)
                    value = stream.getvalue()
                    updated = 0
                    for frame in reversed(self.frames):
                        if frame._update(value):
                            updated += 1
                        else:
                            break
                    self.frames = self.frames[len(self.frames)-updated:]
                    frame = Frame(value)
                    if self._outlet(frame):
                        self.frames.append(frame)
                    stream.seek(0)
                    stream.truncate()
                except GeneratorExit:
                    break
        self.camera.capture_sequence(generator(), *self.args, **self.kwargs)

    def _outlet(self, o):
        length = len(self.out_queues)
        while self._is_running():
            try:
                self.out_queues[self.out_queue_id % length].put(o, block=False)
                self.out_queue_id += 1
                return True
            except Full:
                return False
            except:
                traceback.print_exc()
        return False


class V4LCameraCapture(Producer):

    """Captured Frame Producer for Video4Linux"""

    def __init__(self, device='/dev/video0', size=(640, 480), framerate=30,
                 expected_format=V4L2_PIX_FMT.RGB24, fallback_formats=[V4L2_PIX_FMT.YUYV]):
        """

        Args:
            device (str): v4l device path
            size (int, int): expected capture resolution
            framerate (int): capture framerate
            expected_format (:class:`~actfw.v4l2.video.V4L2_PIX_FMT`): expected capture format
            fallback_formats (list of :class:`~actfw.v4l2.video.V4L2_PIX_FMT`): fallback capture format

        Notes:
            If a camera doesn't support the expected_format,
            try to capture one of the fallback_formats and convert it to expected_format.

        """
        super(V4LCameraCapture, self).__init__()
        self.video = Video(device)
        self.frames = []

        width, height = size

        candidates = self.video.lookup_config(width, height, framerate, expected_format, expected_format)
        for fallback_format in fallback_formats:
            candidates += self.video.lookup_config(width, height, framerate, fallback_format, expected_format)
        config = candidates[0]
        fmt = self.video.set_format(config, width, height, expected_format)
        self.capture_width, self.capture_height, self.capture_format = fmt
        self.video.set_framerate(config)
        # video.set_rotation(90)
        buffers = self.video.request_buffers(4)
        for buf in buffers:
            self.video.queue_buffer(buf)

    def capture_size(self):
        """
        Get configured capture resolution.

        Returns:
            (int, int): configured capture resolution (width, height)
        """
        return (self.capture_width, self.capture_height)

    def run(self):
        """Run producer activity"""
        with self.video.start_streaming() as stream:
            time.sleep(1)  # for Logicool C270
            while self._is_running():
                try:
                    value = stream.capture()
                    updated = 0
                    for frame in reversed(self.frames):
                        if frame._update(value):
                            updated += 1
                        else:
                            break
                    self.frames = self.frames[len(self.frames)-updated:]
                    frame = Frame(value)
                    if self._outlet(frame):
                        self.frames.append(frame)
                except:
                    raise
        self.video.close()

    def _outlet(self, o):
        length = len(self.out_queues)
        while self._is_running():
            try:
                self.out_queues[self.out_queue_id % length].put(o, block=False)
                self.out_queue_id += 1
                return True
            except Full:
                return False
            except:
                traceback.print_exc()
        return False
