import pip
pip.main(['install','pyfirmata'])
from pyfirmata import Arduino, util

board = Arduino('COM')
