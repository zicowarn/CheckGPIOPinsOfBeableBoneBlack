#!/usr/bin/env python
#
#   Copyright 2012 Axxeo GmbH
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
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
__license__ = 'Apache License, Version 2.0'
__status__ = 'Beta'
__revision__ = '$Rev: 03 $'
__date__ = '2014-10-19 22:32:11'


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

