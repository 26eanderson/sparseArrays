import unittest
from sparseArray import SparseArrays  # Adjust import to match your file name

class TestSparseArraysGetElements(unittest.TestCase):

    def setUp(self):
        """Create a fresh sparse array for each test"""
        self.sparse = SparseArrays()

    def test_empty_sparse_array(self):
        """Test getting elements from an empty sparse array"""
        result = self.sparse.get_elements()
        self.assertFalse(result, "Empty sparse array should return False")

    def test_single_element(self):
        """Test getting elements with a single element in the array"""
        # Add one element
        self.sparse.add_element(3, 4, 'x')

        # Get all elements
        elements = self.sparse.get_elements()

        # Verify result
        self.assertIsInstance(elements, dict, "Result should be a dictionary")
        self.assertEqual(len(elements), 1, "Should have exactly one element")
        self.assertIn((3, 4), elements, "Position (3, 4) should exist in elements")
        self.assertEqual(elements[(3, 4)], 'x', "Value at (3, 4) should be 'x'")

    def test_multiple_elements_same_row(self):
        """Test getting elements with multiple elements in the same row"""
        # Add elements to the same row
        self.sparse.add_element(5, 2, 'a')
        self.sparse.add_element(5, 7, 'b')
        self.sparse.add_element(5, 3, 'c')

        # Get all elements
        elements = self.sparse.get_elements()

        # Verify result
        self.assertEqual(len(elements), 3, "Should have exactly three elements")

        # Check if all expected elements are in the result
        expected_elements = {
            (5, 2): 'a',
            (5, 7): 'b',
            (5, 3): 'c'
        }
        for position, value in expected_elements.items():
            self.assertIn(position, elements, f"Position {position} should exist")
            self.assertEqual(elements[position], value, f"Value at {position} should be {value}")

    def test_multiple_elements_different_rows(self):
        """Test getting elements with elements in different rows"""
        # Add elements to different rows
        self.sparse.add_element(1, 1, 'p')
        self.sparse.add_element(3, 2, 'q')
        self.sparse.add_element(5, 3, 'r')

        # Get all elements
        elements = self.sparse.get_elements()

        # Verify result
        self.assertEqual(len(elements), 3, "Should have exactly three elements")

        # Check if all expected elements are in the result
        expected_elements = {
            (1, 1): 'p',
            (3, 2): 'q',
            (5, 3): 'r'
        }
        for position, value in expected_elements.items():
            self.assertIn(position, elements, f"Position {position} should exist")
            self.assertEqual(elements[position], value, f"Value at {position} should be {value}")

    def test_complex_sparse_array(self):
        """Test getting elements from a more complex sparse array"""
        # Add several elements in various positions
        test_data = [
            (1, 1, 'a'), (1, 5, 'b'),
            (3, 2, 'c'), (3, 4, 'd'), (3, 7, 'e'),
            (8, 3, 'f')
        ]

        for row, col, val in test_data:
            self.sparse.add_element(row, col, val)

        # Get all elements
        elements = self.sparse.get_elements()

        # Verify result
        self.assertEqual(len(elements), len(test_data),
                         f"Should have exactly {len(test_data)} elements")

        # Check if all expected elements are in the result
        for row, col, val in test_data:
            self.assertIn((row, col), elements, f"Position ({row}, {col}) should exist")
            self.assertEqual(elements[(row, col)], val, f"Value at ({row}, {col}) should be {val}")

    def test_updated_elements(self):
        """Test getting elements after updating some values"""
        # Add initial elements
        self.sparse.add_element(2, 3, 'old1')
        self.sparse.add_element(4, 5, 'old2')

        # Update one element
        self.sparse.add_element(2, 3, 'new1')

        # Get all elements
        elements = self.sparse.get_elements()

        # Verify result
        self.assertEqual(len(elements), 2, "Should have exactly two elements")
        self.assertIn((2, 3), elements, "Position (2, 3) should exist")
        self.assertEqual(elements[(2, 3)], 'new1', "Value at (2, 3) should be 'new1'")
        self.assertIn((4, 5), elements, "Position (4, 5) should exist")
        self.assertEqual(elements[(4, 5)], 'old2', "Value at (4, 5) should be 'old2'")


if __name__ == '__main__':
    unittest.main()