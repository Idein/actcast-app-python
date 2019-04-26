import os, json
from pathlib import Path
import actfw.task
import actfw.capture
from .application import Application
from .display import Display
from .command_server import CommandServer

from actfw import _version

__version__ = _version.__version__

def notify(notification, *args, **kwargs):
    kwargs['flush'] = True
    print(json.dumps(notification), *args, **kwargs)

_default_heartbeat_file = Path('/root/heartbeat')

def _default_heartbeat():
    _default_heartbeat_file.touch()

_heartbeat_function = _default_heartbeat

def set_heartbeat_function(f):
    _heartbeat_function = f

def heartbeat():
    _heartbeat_function()
