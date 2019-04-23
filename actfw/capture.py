import io
from queue import Full
from .task import Producer

class Frame(object):

    def __init__(self, value):
        self.value = value
        self.updatable = True

    def getvalue(self):
        self.updatable = False
        return self.value

    def _update(self, value):
        if self.updatable:
            self.value = value
            return True
        return False

class PiCameraCapture(Producer):

    def __init__(self, camera, *args, **kwargs):
        super(PiCameraCapture, self).__init__()
        self.camera = camera
        self.args = args
        self.kwargs = kwargs
        self.frames = []

    def run(self):
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
                self.out_queues[self.out_queue_id%length].put(o, block=False)
                self.out_queue_id += 1
                return True
            except Full:
                return False
            except:
                traceback.print_exc()
        return False
