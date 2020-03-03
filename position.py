from pymouse import PyMouse
from time import sleep
from gi.repository import Gdk
import sys

m = PyMouse()
while True:
    print(m.position())
    sleep(0.5)
