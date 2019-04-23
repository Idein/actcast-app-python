import os, signal, time, json
from actfw.task import Task

class Application:

    def __init__(self):
        self.tasks = []
        self.settings = None
        env = 'ACT_SETTINGS_PATH'
        if env in os.environ:
            try:
                with open(os.environ[env]) as f:
                    self.settings = json.load(f)
            except FileNotFoundError:
                pass

    def get_settings(self, default_settings):
        if not isinstance(default_settings, dict):
            raise TypeError("default_settings must be dict.")
        settings = default_settings.copy()
        if self.settings is not None:
            settings.update(self.settings)
        return settings

    def register_task(self, task):
        if not issubclass(type(task), Task):
            raise TypeError("type(task) must be a subclass of actfw.task.Task.")
        self.tasks.append(task)

    def run(self):
        # start all task
        for task in self.tasks:
            task.start()

        try:
            sigint_handler = signal.getsignal(signal.SIGINT)
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            signal.signal(signal.SIGINT, signal.SIG_IGN)
            time.sleep(1)
        except:
            raise

        for task in self.tasks:
            task.stop()
        for task in self.tasks:
            task.join()
