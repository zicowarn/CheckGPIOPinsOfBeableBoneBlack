#!/usr/bin/env python
#
# The MIT License (MIT)

# Copyright (c) 2015 Zhichao Wang

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE..
#

"""

.. moduleauthor:: zhichao, wang <ziccowarn@gmail.com>
.. Program to test looking up information in /usr/share/bone101/static/bone.js
.. Usage:  findGPIO.py 7     # Look up info for gpio7 (internal pin number)
..         findGPIO.py P9_12 # Look up using header pin number (external)
..         findGPIO.py P9_12 P9_13 ...  # Look up multiple pins and use one line
..                                      # output for each.
.. Returns current pin mux
"""

__author__ = 'zhichao,wang'
__email__ = 'ziccowarn@gmail.com'
__url__ = 'http://www.axxeo.de/'
__version__ = '0.1'
__license__ = 'MIT License'
__status__ = 'Beta'
__revision__ = '$Rev: 03 $'
__date__ = '2015-09-19 22:32:11'


import bonescript
import os,sys
import getopt
import json

PINS = "/sys/kernel/debug/pinctrl/44e10800.pinmux/pins"
PINMUX = "/sys/kernel/debug/pinctrl/44e10800.pinmux/pinmux-pins"

def usage():
    """
    """
    print """.. Program to test looking up information in /usr/share/bone101/static/bone.js
.. Usage:  findGPIO.py 7     # Look up info for gpio7 (internal pin number)
..         findGPIO.py P9_12 # Look up using header pin number (external)
..         findGPIO.py P9_12 P9_13 ...  # Look up multiple pins and use one line
..                                      # output for each.
..         Returns current pin mux
    """


def pinMux(gpio, flag):
    """
    """
    dirs = " "
    addr='('+hex(0x44e10800 +int(gpio['muxRegOffset'],16))[2:]+')'
    stdout=os.popen("grep '"+addr+"' "+PINS)
    line = stdout.readlines()
    mux = int(line[0].split(" ")[3], 16)
    out = gpio['key'] + ' (gpio ' + str(gpio['gpio']) + ") mode: " + str(mux & 0x7) + " (" + gpio['options'][mux&0x7] +") " + gpio['muxRegOffset']
    if not (mux & 0x8):
        if (mux & 0x10):
            dirs = " up"
        else:
            pass
        out += ' pull' + dirs
    else:
        pass
    if (mux & 0x20):
        out += " Receiver Active"
    else:
        pass
    if (mux & 0x40):
        out += " Slew Control Slow"
    else:
        pass
    print out
    if flag:
        stdout=os.popen("grep '"+addr+"' "+PINMUX)
        line = stdout.readlines()
        print line[0],


def main(argv):
    try:
      opts, args = getopt.getopt(argv, "", "")
    except getopt.GetoptError:
      usage()
      sys.exit(2)

    if len(args) == 0:
        usage()
    elif len(args)<2:
        flag = True
    else:
        flag = False
    for arg in args:
        gpio = arg.upper()
        print gpio
        if (gpio[0] is 'P') or (gpio[0] is 'U'):
            if flag:
                print json.dumps(bonescript.pins[gpio], indent=2)
            else:
                pass
            pinMux(bonescript.pins[gpio],flag)
        else:
            print "Looking for gpio " + gpio
            for (k, v) in bonescript.pins:
                if bonescript.pins[k].gpio == int(gpio, 10):
                    if flag:
                        print json.dumps(bonescript.pins[gpio], indent=2)
                    else:
                        pass
                    pinMux(bonescript.pins[k],flag)
                else:
                    pass

if __name__ == '__main__':
    main(sys.argv[1:])

