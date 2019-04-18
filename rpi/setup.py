"""Setup tool of actsim."""
import setuptools


setuptools.setup(
    name="actcast",
    version="0.0.1",
    description="Python API for Actcast apps",
    packages=setuptools.find_packages(),
    install_requires=['picamera'],
    python_requires='~=3.5.3',
    tests_require=['nose2'],
    test_suite='nose2.collector.collector',
)
