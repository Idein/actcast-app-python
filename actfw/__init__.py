import os
import json
from pathlib import Path
import time
import actfw.task
import actfw.capture
from .application import Application
from .display import Display
from .command_server import CommandServer

from actfw import _version

__version__ = _version.__version__


def notify(notification, *args, **kwargs):
    """

    Make a notification to Actcast.

    Args:
        notification (list of dict): dicts must be encodable to JSON.

    Example:

        >>> import actfw
        >>> actfw.notify([{'msg': 'Hello!'}])
        [{"msg": "Hello!"}]

    """
    if type(notification) != list:
        raise TypeError('must be a list of JSON encodable objects.')
    kwargs['flush'] = True
    print(json.dumps(notification), *args, **kwargs)


class Notifier():
    """

    Notifier at constant-time intervals.

    Args:
        notification_window (int or float): seconds as the interval of notification

    Example:

        >>> import actfw
        >>> notifier = actfw.Notifier(3)  # the interval is 3-seconds
        >>> for i in range(100):
        ...   n.notify([{"hello": "msg"}])
        ...   time.sleep(0.1)
        ...
        [{"hello": "msg"}]
        [{"hello": "msg"}]
        [{"hello": "msg"}]
        [{"hello": "msg"}]
    """

    def __init__(self, notification_window):
        self.notification_window = notification_window
        self.last_notification = None

    def notify(self, notification, *args, **kwargs):
        _current_time = time.time()

        if self.last_notification is not None and _current_time - self.last_notification < self.notification_window:
            pass
        else:
            notify(notification, *args, **kwargs)
            self.last_notification = _current_time


_default_heartbeat_file = Path('/root/heartbeat')


def _default_heartbeat(*args, **kwargs):
    _default_heartbeat_file.touch()


_heartbeat_function = _default_heartbeat


def set_heartbeat_function(f):
    """

    Set heartbeat action.

    Args:
        f (function): function which execute heartbeat action

    Example:

        >>> import actfw
        >>> def heartbeat(): print("working!")
        ...
        >>> actfw.set_heartbeat_function(heartbeat)
        >>> actfw.heartbeat()
        working!

    """
    global _heartbeat_function
    _heartbeat_function = f


def heartbeat(*args, **kwargs):
    """

    Execute heartbeat action.

    Notes:
        Default action is 'touch /root/heartbeat'.

    """
    _heartbeat_function(*args, **kwargs)
