#!/usr/bin/env python

# ------------------------------------------------------------------------------#
# -------------------------------------------------------------------- HEADER --#

"""
:author:
    Andrew Kinney 2022

:description:
    This is a unit test class for the TestTempTracker class in
    the temp_tracker module.
"""

# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- IMPORTS --#

# Built-in
import unittest

# Third-party

# Local
from temp_tracker import TempTracker, MIN_TEMP, MAX_TEMP


# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- CLASSES --#

class TestTempTracker(unittest.TestCase):

    def test_init_and_get_temps(self):
        tt = TempTracker([])
        self.assertEqual(tt.get_temps(), [])
        tt = TempTracker([70, 80, 90, 100, 110])
        self.assertEqual(tt.get_temps(), [70, 80, 90, 100, 110])

    def test_reset_temps(self):
        tt = TempTracker([70, 80, 90, 100, 110])
        tt.reset_temps()
        self.assertEqual(tt.get_temps(), [])

    def test_insert(self):
        tt = TempTracker()
        tt.insert(70)
        tt.insert(80)
        self.assertEqual(tt.get_temps(), [70, 80])
        tt.insert([90])
        tt.insert([100, 110])
        self.assertEqual(tt.get_temps(), [70, 80, 90, 100, 110])

    def test_zero_degrees(self):
        tt = TempTracker(0)
        self.assertEqual(tt.get_temps(), [0])
        tt = TempTracker([0])
        self.assertEqual(tt.get_temps(), [0])

    def test_get_min(self):
        tt = TempTracker()
        self.assertEqual(tt.get_min(), None)
        tt = TempTracker([70, 80, 90, 100, 110])
        self.assertEqual(tt.get_min(), 70)
        self.assertTrue(isinstance(tt.get_min(), int))

    def test_get_max(self):
        tt = TempTracker()
        self.assertEqual(tt.get_max(), None)
        tt.insert([70, 80, 90, 100, 110])
        self.assertEqual(tt.get_max(), 110)
        self.assertTrue(isinstance(tt.get_max(), int))

    def test_get_mean(self):
        tt = TempTracker()
        self.assertEqual(tt.get_mean(), None)
        tt.insert(0)
        self.assertEqual(tt.get_mean(), 0.0)
        tt.insert([0, 0, 0, 0])
        self.assertEqual(tt.get_mean(), 0.0)
        tt = TempTracker([80, 81])
        self.assertEqual(tt.get_mean(), 80.5)
        self.assertTrue(isinstance(tt.get_mean(), float))

    def test_min_value(self):
        tt = TempTracker(MIN_TEMP)
        self.assertEqual(tt.get_temps(), [MIN_TEMP])

    def test_max_value(self):
        tt = TempTracker(MAX_TEMP)
        self.assertEqual(tt.get_temps(), [MAX_TEMP])

    def test_temp_range(self):
        tt = TempTracker([0, 10, -10, -1, 110, 111, 120])
        self.assertEqual(tt.get_temps(), [0, 10, 110])


if __name__ == "__main__":
    unittest.main()