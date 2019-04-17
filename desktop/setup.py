"""Setup tool of actcast for desktop."""


import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="actcast",
    version="0.0.1",
    description="Python API for Actcast apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Idein/actcast-py",
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='~=3.5.3',
    tests_require=['nose2'],
    test_suite='nose2.collector.collector',
)
