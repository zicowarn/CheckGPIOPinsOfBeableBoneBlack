
1. findGPIO.py
.. moduleauthor:: zhichao, wang <ziccowarn@gmail.com>
.. Program to test looking up information in /usr/share/bone101/static/bone.js
.. Usage:  findGPIO.py 7     # Look up info for gpio7 (internal pin number)
..         findGPIO.py P9_12 # Look up using header pin number (external)
..         findGPIO.py P9_12 P9_13 ...  # Look up multiple pins and use one line
..                                      # output for each.
.. Returns current pin mux

2. freeGPIO.py

.. Lists all gpio pins with MUX UNCLAIMED and GPIO UNCLAIMED in $PINMUX
.. Usage:  freeGPIO.py    # List free GPIOs using P8 or P9 pin number
     Approach:
        1. search PINMUX for all entries with "(MUX UNCLAIMED) (GPIO UNCLAIMED)"
        2. An entry looks like "pin 8 (44e10820): (MUX UNCLAIMED) (GPIO UNCLAIMED)"
        3. Extract the address (44e10820) and subtract 0x44e10800 to ge the offset
        4. Format the offset as 0x020, with leading 0's to give 3 digits
        5. Search for the address in the muxRegOffset field in b.bone.pins
        6. Print the matching key