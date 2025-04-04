import random
from idlelib.debugger_r import DictProxy
from typing import Generic, TypeVar, Dict, List, Optional
T = TypeVar("T")
from LinkedListFile import *
class SparseArrays:
    mySparse = LinkedList()
    lettersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
    def __init__(self):
        self.mySparse = LinkedList()

    def get_elements(self) -> Dict:
        elements = {}
        if self.mySparse.start is None:
            return elements
        else:
            p: LL_Node[T] = self.mySparse.start
            i = 0
            while self.mySparse.__len__() > i:
                row, ll = p.get_value()
                q: LL_Node[T] = ll.start
                j = 0
                while ll.__len__() > j:
                    col, let = q.get_value()
                    elements.update({(row,col):let})
                    #elements[(row,col)] = let
                    q = q.get_next()
                    j += 1
                p = p.get_next()
                i += 1
        return elements


    def print(self):
        elements:Dict = self.get_elements()
        print(f"{type(elements)=}")
        print(f"{elements=}")
        maxrow = 0
        maxcol = 0
        for (row, col) in elements.keys():
            if row > maxrow:
                maxrow = row
            if col > maxcol:
                maxcol = col
        for x in range(maxrow+1):
            for y in range(maxcol+1):
                if (x,y) in elements:
                        print(elements[(x,y)], end="")
                else:
                    print(" ", end="")
            print()



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

    def search_for_element_with_r_and_c(self, row, col, let):
        row_exists, row_node = self.search_for_row(row)
        if row_exists:
            return row_node.get_value()[1].add_to_start((col, let))
        else:
            rowLinkedList = LinkedList()
            rowLinkedList.insert_value_at_start((col,let))
            self.mySparse.add_to_end((row,rowLinkedList))


    def remove_element(self, row, col, let):
        row_exists, row_node = self.search_for_row(row)
        if row_exists:
            row_node.get_value()[1].remove((col, let))
