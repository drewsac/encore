#!/usr/bin/env python

# ------------------------------------------------------------------------------#
# -------------------------------------------------------------------- HEADER --#

"""
:author:
    Andrew Kinney 2022

:description:
    This is a unit test class for the list_flattener module
"""

# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- IMPORTS --#

# Built-in
import unittest

# Third-party

# Local
from list_flattener import flatten_list, flatten_list_from_string


# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- CLASSES --#

class TestFlattenListObj(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list_from_string('[]'), [])
        self.assertEqual(flatten_list([[[[[[]]]]]]), [])
        self.assertEqual(flatten_list_from_string('[[[[[[]]]]]]'), [])

    def test_no_list_test(self):
        self.assertFalse(flatten_list(1))
        self.assertFalse(flatten_list({}))
        self.assertFalse(flatten_list_from_string('1'))
        self.assertFalse(flatten_list_from_string('{}'))
        self.assertFalse(flatten_list_from_string(''))

    def test_simple_list(self):
        self.assertEqual(flatten_list([1]), [1])
        self.assertEqual(flatten_list_from_string('[1]'), [1])

    def test_nested_list(self):
        self.assertEqual(flatten_list([[1, 2, [3]], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten_list_from_string('[[1,2,[3]],4]'),
                                                  [1, 2, 3, 4])

    def test_argument_syntax_test(self):
        self.assertFalse(flatten_list_from_string('[[1,2,[3]],4]]'))


if __name__ == "__main__":
    unittest.main()