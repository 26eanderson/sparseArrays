import unittest
from sparseArray import SparseArrays  # Adjust import to match your file name


class TestSparseArrays(unittest.TestCase):

    def setUp(self):
        """Create a fresh sparse array for each test"""
        self.sparse = SparseArrays()

    def test_add_to_empty(self):
        """Test adding an element to an empty sparse array"""
        # Add element to empty array
        self.sparse.add_element(3, 4, 'x')

        # Verify row exists
        row_exists, row_node = self.sparse.search_for_row(3)
        self.assertTrue(row_exists, "Row 3 should exist after adding element")

        # Verify column exists with correct value
        row_tuple = row_node.get_value()
        col_list = row_tuple[1]

        # Find column in the list
        found = False
        p = col_list.start
        while p is not None:
            col_data = p.get_value()
            if col_data[0] == 4:  # If this is column 4
                self.assertEqual(col_data[1], 'x', "Value at (3,4) should be 'x'")
                found = True
                break
            p = p.get_next()

        self.assertTrue(found, "Column 4 should exist in row 3")

    def test_add_to_existing_row(self):
        """Test adding an element to an existing row"""
        # First add a row
        self.sparse.add_element(5, 2, 'a')

        # Now add another element to the same row
        self.sparse.add_element(5, 7, 'b')

        # Verify both elements exist
        row_exists, row_node = self.sparse.search_for_row(5)
        self.assertTrue(row_exists, "Row 5 should exist")

        row_tuple = row_node.get_value()
        col_list = row_tuple[1]

        # Check both columns exist
        col_values = {}
        p = col_list.start
        while p is not None:
            col_data = p.get_value()
            col_values[col_data[0]] = col_data[1]
            p = p.get_next()

        self.assertIn(2, col_values, "Column 2 should exist in row 5")
        self.assertIn(7, col_values, "Column 7 should exist in row 5")
        self.assertEqual(col_values[2], 'a', "Value at (5,2) should be 'a'")
        self.assertEqual(col_values[7], 'b', "Value at (5,7) should be 'b'")

    def test_add_to_new_row(self):
        """Test adding elements to multiple rows"""
        # Add elements to different rows
        self.sparse.add_element(1, 1, 'p')
        self.sparse.add_element(3, 2, 'q')
        self.sparse.add_element(5, 3, 'r')

        # Verify all rows exist
        for row, expected_value in [(1, 'p'), (3, 'q'), (5, 'r')]:
            row_exists, row_node = self.sparse.search_for_row(row)
            self.assertTrue(row_exists, f"Row {row} should exist")

            # Get the column list
            col_list = row_node.get_value()[1]

            # Find the column (each row has only one column in this test)
            p = col_list.start
            col_data = p.get_value()

            # Verify column and value
            self.assertEqual(col_data[1], expected_value,
                             f"Value at row {row} should be '{expected_value}'")

    def test_update_existing_column(self):
        """Test updating an existing column value"""
        # Add initial element
        self.sparse.add_element(2, 3, 'old')

        # Update the same position
        self.sparse.add_element(2, 3, 'new')

        # Verify the update
        row_exists, row_node = self.sparse.search_for_row(2)
        self.assertTrue(row_exists, "Row 2 should exist")

        # Get column list
        col_list = row_node.get_value()[1]

        # Check if column has updated value
        found = False
        p = col_list.start
        while p is not None:
            col_data = p.get_value()
            if col_data[0] == 3:  # If this is column 3
                self.assertEqual(col_data[1], 'new', "Value should be updated to 'new'")
                found = True
                break
            p = p.get_next()

        self.assertTrue(found, "Column 3 should exist in row 2")

    def test_multiple_operations(self):
        """Test a sequence of operations"""
        # Add several elements
        self.sparse.add_element(1, 1, 'a')
        self.sparse.add_element(1, 2, 'b')
        self.sparse.add_element(2, 1, 'c')
        self.sparse.add_element(1, 1, 'd')  # Update existing

        # Verify final state
        # Row 1 should have columns 1 and 2 with values 'd' and 'b'
        # Row 2 should have column 1 with value 'c'

        # Check row 1
        row_exists, row_node = self.sparse.search_for_row(1)
        self.assertTrue(row_exists, "Row 1 should exist")

        col_list = row_node.get_value()[1]
        col_values = {}
        p = col_list.start
        while p is not None:
            col_data = p.get_value()
            col_values[col_data[0]] = col_data[1]
            p = p.get_next()

        self.assertEqual(col_values[1], 'd', "Value at (1,1) should be 'd'")
        self.assertEqual(col_values[2], 'b', "Value at (1,2) should be 'b'")

        # Check row 2
        row_exists, row_node = self.sparse.search_for_row(2)
        self.assertTrue(row_exists, "Row 2 should exist")

        col_list = row_node.get_value()[1]
        p = col_list.start
        col_data = p.get_value()
        self.assertEqual(col_data[0], 1, "Column should be 1")
        self.assertEqual(col_data[1], 'c', "Value at (2,1) should be 'c'")


if __name__ == '__main__':
    unittest.main()
