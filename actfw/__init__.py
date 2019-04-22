import json
import actfw.task
import actfw.capture
from .application import Application
from .display import Display
from .command_server import CommandServer

from actfw import _version

__version__ = _version.__version__

def notice(notices, *args, **kwargs):
    kwargs['flush'] = True
    print(json.dumps(notices), *args, **kwargs)
