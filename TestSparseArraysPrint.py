import unittest
import random
import io
import sys
from sparseArray import SparseArrays  # Adjust import to match your file name


class TestSparseArraysPrintExamples(unittest.TestCase):

    def setUp(self):
        """Create a fresh sparse array for each test"""
        self.sparse = SparseArrays()
        # Redirect stdout to capture print output
        self.held_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = self.original_stdout
        # Print a separator between tests
        print("\n" + "=" * 50 + "\n")

    def test_print_examples(self):
        """Print various examples of sparse arrays"""
        examples = [
            # Example 1: Empty array
            [],

            # Example 2: Single element
            [(1, 1, 'X')],

            # Example 3: Small grid with a few elements
            [(0, 0, 'A'), (0, 2, 'B'), (2, 0, 'C'), (2, 2, 'D')],

            # Example 4: Row pattern
            [(1, 0, 'a'), (1, 1, 'b'), (1, 2, 'c'), (1, 3, 'd'), (1, 4, 'e')],

            # Example 5: Column pattern
            [(0, 2, 'v'), (1, 2, 'w'), (2, 2, 'x'), (3, 2, 'y'), (4, 2, 'z')],

            # Example 6: Diagonal pattern
            [(0, 0, '1'), (1, 1, '2'), (2, 2, '3'), (3, 3, '4'), (4, 4, '5')],

            # Example 7: Random scattered elements
            [(0, 3, 'R'), (1, 5, 'A'), (2, 1, 'N'), (3, 4, 'D'), (4, 0, 'O'), (5, 2, 'M')],

            # Example 8: Larger grid with more elements
            [(i, j, chr(65 + i * 5 + j)) for i in range(5) for j in range(5) if (i + j) % 2 == 0],

            # Example 9: Sparse representation of a word
            [(0, 0, 'S'), (0, 1, 'P'), (0, 2, 'A'), (0, 3, 'R'), (0, 4, 'S'), (0, 5, 'E')]
        ]

        # Print each example
        for i, example in enumerate(examples):
            print(f"\nExample {i + 1}:")
            print(f"Elements: {example}")

            # Clear the sparse array
            self.sparse = SparseArrays()

            # Add elements to the sparse array
            for row, col, val in example:
                self.sparse.add_element(row, col, val)

            # Print the sparse array
            print("\nPrinted Sparse Array:")
            self.sparse.print()

            # Get the output
            output = self.held_output.getvalue()
            print(output)

            # Reset the output buffer for the next example
            self.held_output = io.StringIO()
            sys.stdout = self.held_output

    def test_print_random_examples(self):
        """Print random examples of sparse arrays"""
        random.seed(42)  # For reproducible results

        # Generate several random examples
        for i in range(5):
            # Generate random dimensions
            max_row = random.randint(3, 8)
            max_col = random.randint(3, 8)

            # Generate random number of elements
            density = random.uniform(0.1, 0.5)  # How filled the array is
            num_elements = int(max_row * max_col * density)

            # Generate random positions and letters
            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            positions = set()

            while len(positions) < num_elements:
                row = random.randint(0, max_row - 1)
                col = random.randint(0, max_col - 1)
                positions.add((row, col))

            # Create the example
            example = []
            for row, col in positions:
                letter = random.choice(letters)
                example.append((row, col, letter))

            # Print the example
            print(f"\nRandom Example {i + 1}:")
            print(f"Dimensions: {max_row}x{max_col}, Elements: {len(example)}")
            print(f"Elements: {example}")

            # Clear the sparse array
            self.sparse = SparseArrays()

            # Add elements to the sparse array
            for row, col, val in example:
                self.sparse.add_element(row, col, val)

            # Print the sparse array
            print("\nPrinted Sparse Array:")
            self.sparse.print()

            # Get the output
            output = self.held_output.getvalue()
            print(output)

            # Reset the output buffer for the next example
            self.held_output = io.StringIO()
            sys.stdout = self.held_output


if __name__ == '__main__':
    unittest.main()