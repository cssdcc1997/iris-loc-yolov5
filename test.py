from curses import flash
import os

print(__file__)

abs = os.path.abspath(os.path.dirname(__file__))
print(abs)
print(os.path.dirname(__file__))

a = not False and not False

print(a)