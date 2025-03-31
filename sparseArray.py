import random
from typing import Generic, TypeVar, List, Optional
T = TypeVar("T")
from LinkedListFile import *
class SparseArrays:
    mySparse = LinkedList()
    lettersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
    def __init__(self):
        self.mySparse = LinkedList()

    def search_for_row(self, row):
        if self.mySparse.start is None:
            return (False, None)
        else:
            p: LL_Node[T] = self.mySparse.start
            i = 0
            while self.mySparse.__len__()>i:
                if p.get_value()[0] == row:
                    return (True, p)
                p = p.get_next()
                i += 1
        return (False, None)

    def add_element(self, row, col, let):
        row_exists, row_node = self.search_for_row(row)
        if row_exists:
            row_node.get_value()[1].add_to_start((col, let))
        else:
            rowLinkedList = LinkedList()
            rowLinkedList.insert_value_at_start((col,let))
            self.mySparse.add_to_end((row,rowLinkedList))


