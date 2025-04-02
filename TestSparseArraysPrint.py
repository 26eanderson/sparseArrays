import unittest
from io import StringIO
import sys
from sparseArray import SparseArrays  # Adjust import to match your file name


class TestSparseArraysPrint(unittest.TestCase):

    def setUp(self):
        """Create a fresh sparse array for each test"""
        self.sparse = SparseArrays()
        # Redirect stdout to capture print output
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = self.original_stdout

    def test_empty_sparse_array(self):
        """Test printing an empty sparse array"""
        # Mock get_elements to return an empty list
        self.sparse.get_elements = lambda: []

        # Call the print method
        self.sparse.print()

        # Get the captured output
        output = self.held_output.getvalue()

        # An empty sparse array should print nothing or a specific message
        self.assertEqual(output.strip(), "", "Empty sparse array should print nothing")

    def test_single_element(self):
        """Test printing a sparse array with a single element"""
        # Mock get_elements to return a single element
        self.sparse.get_elements = lambda: [(1, 1, 'x')]

        # Call the print method
        self.sparse.print()

        # Get the captured output
        output = self.held_output.getvalue()

        # Check if 'x' appears in the output
        self.assertIn('x', output, "Output should contain 'x'")

    def test_multiple_elements(self):
        """Test printing a sparse array with multiple elements"""
        # Mock get_elements to return multiple elements
        elements = [
            (0, 0, 'a'), (0, 2, 'b'),
            (2, 1, 'c'), (2, 3, 'd')
        ]
        self.sparse.get_elements = lambda: elements

        # Call the print method
        self.sparse.print()

        # Get the captured output
        output = self.held_output.getvalue()

        # Check if all letters appear in the output
        for _, _, letter in elements:
            self.assertIn(letter, output, f"Output should contain '{letter}'")

        # Count spaces to ensure empty cells are represented
        space_count = output.count(' ')
        self.assertGreaterEqual(space_count, 1, "Output should contain spaces for empty cells")

    def test_large_sparse_array(self):
        """Test printing a larger sparse array"""
        # Mock get_elements to return elements in a larger grid
        elements = [
            (0, 0, 'a'), (0, 4, 'b'),
            (3, 1, 'c'), (3, 3, 'd'),
            (5, 2, 'e'), (5, 5, 'f')
        ]
        self.sparse.get_elements = lambda: elements

        # Call the print method
        self.sparse.print()

        # Get the captured output
        output = self.held_output.getvalue()

        # Check if all letters appear in the output
        for _, _, letter in elements:
            self.assertIn(letter, output, f"Output should contain '{letter}'")

    def test_updated_print_logic(self):
        """Test with a modified version of the print method to verify logic"""
        # This test is designed to check if the print method's logic works correctly
        # by mocking a simplified version that just returns the expected grid

        # Create a test instance with a modified print method for testing
        test_sparse = SparseArrays()

        # Mock data
        elements = [
            (0, 0, 'a'), (0, 2, 'b'),
            (1, 1, 'c'), (1, 3, 'd'),
            (2, 0, 'e'), (2, 2, 'f')
        ]

        # Mock get_elements
        test_sparse.get_elements = lambda: elements

        # Call the print method
        test_sparse.print()

        # Get the captured output
        output = self.held_output.getvalue()

        # Verify that the output contains all the expected characters
        expected_chars = ['a', 'b', 'c', 'd', 'e', 'f', ' ']
        for char in expected_chars:
            self.assertIn(char, output, f"Output should contain '{char}'")


if __name__ == '__main__':
    unittest.main()