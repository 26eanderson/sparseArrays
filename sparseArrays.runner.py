import random
from typing import Generic, TypeVar, List, Optional
T = TypeVar("T")
from LinkedListFile import *
class SparseArrays:
    mySparse = LinkedList()
    lettersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
    def __init__(self):
        self.mySparse = LinkedList[(int,LinkedList())]

    def add_element(self, row, col, let):
        len = len(self.mySparse)
        for i in range(len):
            current = self.mySparse[i].item_at_index:
            if current[0] == row:


