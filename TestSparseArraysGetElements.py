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
        self.assertIsInstance(elements, list, "Result should be a list")
        self.assertEqual(len(elements), 1, "Should have exactly one element")
        self.assertEqual(elements[0], (3, 4, 'x'), "Element should be (3, 4, 'x')")

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
        expected_elements = [(5, 2, 'a'), (5, 7, 'b'), (5, 3, 'c')]
        for element in expected_elements:
            self.assertIn(element, elements, f"Element {element} should be in the result")

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
        expected_elements = [(1, 1, 'p'), (3, 2, 'q'), (5, 3, 'r')]
        for element in expected_elements:
            self.assertIn(element, elements, f"Element {element} should be in the result")

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
        for element in test_data:
            self.assertIn(element, elements, f"Element {element} should be in the result")

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
        self.assertIn((2, 3, 'new1'), elements, "Updated element should have new value")
        self.assertIn((4, 5, 'old2'), elements, "Unchanged element should remain the same")
        self.assertNotIn((2, 3, 'old1'), elements, "Old value should not be present")


if __name__ == '__main__':
    unittest.main()