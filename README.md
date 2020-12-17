# *DEPRECATED* Actcast Application Framework for Python

This package provides a Python API for developing Actcast apps.

This framework has moved into [actfw-core](https://pypi.org/project/actfw-core/) & [actfw-raspberrypi](https://pypi.org/project/actfw-raspberrypi/) since v1.4.0.

This package only provides `actfw` module name, which interally binds submodules in `actfw_core` and `actfw_raspberrypi`.

## Document

* [API References](https://idein.github.io/actfw-docs/latest/)

## Usage

Construct your application with a task parallel model

* Application
    * `actfw.Application` : Main application
* Workers
    * `actfw.task.Producer` : Task generator
        * `actfw.capture.PiCameraCapture` : Generate CSI camera capture image
        * `actfw.capture.V4LCameraCapture` : Generate UVC camera capture image
    * `actfw.task.Pipe` : Task to Task converter
    * `actfw.task.Consumer` : Task terminator

Each worker is executed in parallel.

User should

* Define subclass of `Producer/Pipe/Consumer`
~~~~python
class MyPipe(actfw.task.Pipe):
    def proc(self, i):
        ...
~~~~
* Connect defined worker objects
~~~~python
p  = MyProducer()
f1 = MyPipe()
f2 = MyPipe()
c  = MyConsumer()
p.connect(f1)
f1.connect(f2)
f2.connect(c)
~~~~
* Register to `Application`
~~~~python
app = actfw.Application()
app.register_task(p)
app.register_task(f1)
app.register_task(f2)
app.register_task(c)
~~~~
* Execute application
~~~~python
app.run()
~~~~
