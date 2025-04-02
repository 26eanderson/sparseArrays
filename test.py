import unittest
import random
import math
from sparseArray import SparseArrays  # Adjust import to match your file name

class TestSparseArrays(unittest.TestCase):

    def setUp(self):
        self.sparse = SparseArrays()
        lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

        for i in range(20):
            row = random.randint(0,40)
            col = random.randint(0,40)
            let = lettersList[random.randint(0,len(lettersList)-1)]
            self.sparse.add_element(row, col, let)

