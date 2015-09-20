# CheckGPIOPinsOfBeagleBoneBlack Borad
================================================================================

Check GPIO Pins Of BeagleBone Black, this small project provide three python files. one of them names bonescript.py. this is a support file and collected all the necessary infos of P8 and P9 Pin arrays. you can use the another two python scirpts check the avaiable Pins and find out the state of the specific Pin.

### File structure of this small project:

  - bonescirpt.py
  - findGPIO.py
  - freeGPIO.py
 
### Dependent library:

this is a very small project, there is no specific dependent manner. the only one dependents library names json. Mainly it will be used to extract the relevant information from bonescirpt.py

-----------------------------------------------------------------
## Useage:
------------------------------------------------------------------

### For findGPIO.py:
 >> Infos: Program to test looking up information of GPIO Pins on BeagleBone Black Board
 >>> Usage:  
  - findGPIO.py 7     # Look up info for gpio7 (internal pin number)
  - findGPIO.py P9_12 # Look up using header pin number (external)
  - findGPIO.py P9_12 P9_13 ...  # Look up multiple pins and use one line
                                     # output for each.
  - Returns current pin mux

### For freeGPIO.py
>> Infos: Lists all gpio pins with MUX UNCLAIMED and GPIO UNCLAIMED in $PINMUX
>>> Usage:  freeGPIO.py    # List free GPIOs using P8 or P9 pin number
>>>>Approach:
1. search PINMUX for all entries with "(MUX UNCLAIMED) (GPIO UNCLAIMED)"
2. An entry looks like "pin 8 (44e10820): (MUX UNCLAIMED) (GPIO UNCLAIMED)"
3. Extract the address (44e10820) and subtract 0x44e10800 to ge the offset
4. Format the offset as 0x020, with leading 0's to give 3 digits
5. Search for the address in the muxRegOffset field in b.bone.pins
6. Print the matching key

### Version
0.1 Beta Rev 0.3

### Installation

```sh
$ git clone [git-repo-url] CheckGPIOPinsOfBeagleBoneBlack
$ cd CheckGPIOPinsOfBeagleBoneBlack
$ python findGPIO.py P8 or freeGPIO.py
```

### Todos

 - Write Tests
 - Add Code Comments

License
----
The MIT License (MIT)

Copyright (c) 2015 Zhichao Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Free Software, Hell Yeah!**
