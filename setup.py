"""Setup tool of actsim."""


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

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
    install_requires=['v4l2'],
    python_requires='~=3.5.3',
    tests_require=['nose2'],
    test_suite='nose2.collector.collector',
)
