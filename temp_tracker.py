#!/usr/bin/env python

# ------------------------------------------------------------------------------#
# -------------------------------------------------------------------- HEADER --#

"""
:author:
    Andrew Kinney 2022

:description:
    Module containing TempTracker class. The TempTracker class 
    accumulates temperature samples into a list and can provide 
    the min, max and mean values.'
"""

# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- IMPORTS --#

# Built-in

# Third-party

# Local

# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- GLOBALS --#

MIN_TEMP = 0
MAX_TEMP = 110


# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- CLASSES --#


class TempTracker(object):
    def __init__(self, temps=None):
        self.temps = []
        self.insert(temps)

    def insert(self, temperature):
        if isinstance(temperature, list):
            temps = temperature
        else:
            temps = [temperature]
        for temp in temps:
            temp = self.validate_temp(temp)
            if temp is not None:
                self.temps.append(temp)

    def validate_temp(self, temp):
        if isinstance(temp, int):
            if temp <= MAX_TEMP and temp >= MIN_TEMP:
                return int(temp)
        return None

    def get_max(self):
        if self.temps:
            return max(self.temps)
        return None

    def get_min(self):
        if self.temps:
            return min(self.temps)
        return None

    def get_mean(self):
        if self.temps:
            return float(sum(self.temps)) / len(self.temps)
        return None

    def get_temps(self):
        return sorted(self.temps)

    def reset_temps(self):
        self.temps = []