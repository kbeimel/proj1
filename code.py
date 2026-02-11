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
        self.m               = m #factor to multiply by
        self.b               = b #bonus spots added 
        self.currentpointer  = 0 #first empty position
        self.data            = [None] #list 

    # DO NOT MODIFY!
    def esdump(self) -> str:
        return json.dumps(self.data)

    # Push an integer onto the stack.


    def espush(self,x:int):
        if self.currentpointer == len(self.data) : 
            nu_le = (len(self.data) * self.m) + self.b 
            nu_d = [None] * (nu_le - len(self.data))
            self.data = self.data + nu_d
            self.data[self.currentpointer]= x
            self.currentpointer += 1 
        else: 
            self.data[self.currentpointer]= x
            self.currentpointer += 1 
    

    # Pop an integer off the stack  but do not return it.

    def espop_quiet(self):
        self.data[self.currentpointer-1]=None 
        self.currentpointer -= 1 

    # Pop an integer off the stack and return it.

    def espop(self):
        # The next line is just to make the code run.
        # Remove it and replace with your code.
        print('hi')
        r = 0 # You'll have to fix this!
        return r