import os
from setuptools import setup

print("RCE by w3shi(S.Lakshmi Vignesh")

if platform.system() == "Windows":
    os.system("calc.exe")
elif platform.system() == "Linux":
    os.system("gnome-calculator")

setup(
    name="rcepipslv",
    version="0.0.1",
    py_modules=[],
)
