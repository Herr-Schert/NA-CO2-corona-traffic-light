import sys
sys.path.pop(0)
from setuptools import setup
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NA-CO2-corona-traffic-light",
    py_modules=["scd30"],
    version="0.0.1",
    description="MicroPython Project, using a Senserion SCD30 CO₂ sensor along Wemos D1 mini (ESP8266) to achive a networkattached corona traffic light",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="scd30, co2, temperature, humidity, micropython, i2c",
    url="https://github.com/agners/micropython-scd30",
    author="Herr Schert",
    author_email="schert@dillmann-gymnasium.de",
    maintainer="Herr Schert",
    maintainer_email="schert@dillmann-gymnasium.de",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
