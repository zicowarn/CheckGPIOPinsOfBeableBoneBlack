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
.. Lists all gpio pins with MUX UNCLAIMED and GPIO UNCLAIMED in $PINMUX
.. Usage:  freeGPIO.py    # List free GPIOs using P8 or P9 pin number
     Approach:
        1. search PINMUX for all entries with "(MUX UNCLAIMED) (GPIO UNCLAIMED)"
        2. An entry looks like "pin 8 (44e10820): (MUX UNCLAIMED) (GPIO UNCLAIMED)"
        3. Extract the address (44e10820) and subtract 0x44e10800 to ge the offset
        4. Format the offset as 0x020, with leading 0's to give 3 digits
        5. Search for the address in the muxRegOffset field in b.bone.pins
        6. Print the matching key
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

PINMUX = "/sys/kernel/debug/pinctrl/44e10800.pinmux/pinmux-pins"
keylist = []


def usage():
    print """.. Lists all gpio pins with MUX UNCLAIMED and GPIO UNCLAIMED in $PINMUX
..  Usage:  freeGPIO.js    # List free GPIOs using P8 or P9 pin number
       Approach:
          1. search PINMUX for all entries with "(MUX UNCLAIMED) (GPIO UNCLAIMED)"
          2. An entry looks like "pin 8 (44e10820): (MUX UNCLAIMED) (GPIO UNCLAIMED)"
          3. Extract the address (44e10820) and subtract 0x44e10800 to ge the offset
          4. Format the offset as 0x020, with leading 0's to give 3 digits
          5. Search for the address in the muxRegOffset field in b.bone.pins
          6. Print the matching key
"""

def run():
    """
    the run function
    """
    stdout=os.popen("grep '(MUX UNCLAIMED) (GPIO UNCLAIMED)' /sys/kernel/debug/pinctrl/44e10800.pinmux/pinmux-pins")
    line = stdout.readlines()
    for i in range(len(line)):
        if not line[i]: break
        #print line[i]
        addr=line[i].split(' ')[2][1:9]
        pin='0x'+("000"+hex(int(addr,16)-0x44e10800)[2:])[-3:]
        #print pin+" "+line[i],
        for k in bonescript.pins:
            try:
                #print bonescript.pins[k]["muxRegOffset"]
                if(bonescript.pins[k]["muxRegOffset"] == pin):
                    keylist.append(bonescript.pins[k]["key"])
                    break
            except KeyError:
                pass

    keylist.sort()
    for key in keylist:
        print key + " ",
    print


def main(argv):
    try:
      opts, args = getopt.getopt(argv, "h", "")
    except getopt.GetoptError:
      usage()
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            usage()
            sys.exit()

    if len(args) > 0:
        usage()
    else:
        run()


if __name__ == '__main__':
    main(sys.argv[1:])





