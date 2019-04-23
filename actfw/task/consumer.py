from .pipe import Pipe

class Consumer(Pipe):

    def __init__(self):
        super(Consumer, self).__init__()

    def _add_out_queue(self, q):
        raise NotImplementedError('This is consumer')

    def _outlet(self, o):
        raise NotImplementedError('This is consumer')

    def run(self):
        for i in self._inlet():
            self.proc(i)
            if not self._is_running:
                break

    def connect(self, follow):
        if not issubclass(type(follow), Task):
            raise TypeError("type(follow) must be a subclass of actfw.task.Task.")
        raise NotImplementedError('This is consumer')
