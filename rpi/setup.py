"""Setup tool of actsim."""
import setuptools


setuptools.setup(
    name="actcast",
    version="0.0.1",
    author="Takeo Imai",
    author_email="bonotake.oshigoto@gmail.com",
    description="Python API for Actcast apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Idein/actcast-py",
    packages=setuptools.find_packages(),
    install_requires=['picamera'],
    python_requires='~=3.5.3',
    tests_require=['nose2'],
    test_suite='nose2.collector.collector',
)
