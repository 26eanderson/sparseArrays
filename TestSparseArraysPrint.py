import unittest
import random
from sparseArray import SparseArrays

class TestSparseArrayPrinting(unittest.TestCase):

    def setUp(self):
        """Create a fresh sparse array for each test"""
        self.sparse = SparseArrays()

    def test_print_variations(self):
        """Print various sparse array configurations"""

        # Variation 1: Empty Array
        print("\n--- Empty Array ---")
        self.sparse.print()

        # Variation 2: Single Element
        print("\n--- Single Element ---")
        self.sparse = SparseArrays()
        self.sparse.add_element(2, 3, 'X')
        self.sparse.print()

        # Variation 3: Row of Elements
        print("\n--- Row of Elements ---")
        self.sparse = SparseArrays()
        for col in range(5):
            self.sparse.add_element(1, col, chr(65 + col))
        self.sparse.print()

        # Variation 4: Column of Elements
        print("\n--- Column of Elements ---")
        self.sparse = SparseArrays()
        for row in range(5):
            self.sparse.add_element(row, 2, chr(97 + row))
        self.sparse.print()

        # Variation 5: Diagonal Elements
        print("\n--- Diagonal Elements ---")
        self.sparse = SparseArrays()
        for i in range(5):
            self.sparse.add_element(i, i, str(i))
        self.sparse.print()

        # Variation 6: Scattered Elements
        print("\n--- Scattered Elements ---")
        self.sparse = SparseArrays()
        scattered_elements = [
            (0, 3, 'A'), (1, 1, 'B'),
            (2, 4, 'C'), (3, 0, 'D'),
            (4, 2, 'E')
        ]
        for row, col, val in scattered_elements:
            self.sparse.add_element(row, col, val)
        self.sparse.print()

        # Variation 7: Large Sparse Grid
        print("\n--- Large Sparse Grid ---")
        self.sparse = SparseArrays()
        for _ in range(10):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            val = chr(random.randint(65, 90))
            self.sparse.add_element(row, col, val)
        self.sparse.print()

        # Variation 8: Word Representation
        print("\n--- Word Representation ---")
        self.sparse = SparseArrays()
        word = "SPARSE"
        for i, letter in enumerate(word):
            self.sparse.add_element(0, i, letter)
        self.sparse.print()

        # Variation 9: Overlapping Elements
        print("\n--- Overlapping Elements ---")
        self.sparse = SparseArrays()
        self.sparse.add_element(2, 3, 'A')
        self.sparse.add_element(2, 3, 'B')  # Should replace previous
        self.sparse.print()

if __name__ == '__main__':
    unittest.main()