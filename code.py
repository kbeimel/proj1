# Extensible Stack
# Basically a stack but works by pre-allocating space.
# When we overflow the stack we allocate to a new length
# and copy the old contents over.

from __future__ import annotations
import json

# The Extensible Stack class.
# DO NOT MODIFY!
class EStack():
    def  __init__(self,
                  m : int,
                  b : int):
        self.m               = m
        self.b               = b
        self.currentpointer  = 0
        self.data            = [None]

    # DO NOT MODIFY!
    def esdump(self) -> str:
        return json.dumps(self.data)

    # Push an integer onto the stack.

    def espush(self,x:int):
        # The next line is just to make the code run.
        # Remove it and replace with your code.
        print('hi')

    # Pop an integer off the stack  but do not return it.

    def espop_quiet(self):
        # The next line is just to make the code run.
        # Remove it and replace with your code.
        print('hi')

    # Pop an integer off the stack and return it.

    def espop(self):
        # The next line is just to make the code run.
        # Remove it and replace with your code.
        print('hi')
        r = 0 # You'll have to fix this!
        return r