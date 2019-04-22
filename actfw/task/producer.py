from .pipe import Pipe

class Producer(Pipe):

    def __init__(self):
        super(Producer, self).__init__()

    def _add_in_queue(self, q):
        raise NotImplementedError('This is producer')

    def _inlet(self):
        yield ()
