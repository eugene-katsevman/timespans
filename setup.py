import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "timespans",
    version = "0.0.1",
    author = "Eugene Katsevman",
    author_email = "eugene.katsevman@gmail.com",
    description = ("A library for adding and subtracting datetime spans"),
    license = "MIT",
    keywords = "datetime timedelta timespan span",
    url = "https://github.com/eugene-katsevman/timespans",
    py_modules=['timespans'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
