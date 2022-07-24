#!/usr/bin/env python

# ------------------------------------------------------------------------------#
# -------------------------------------------------------------------- HEADER --#

"""
:author:
    Andrew Kinney 2022

:description:
    A utility to flatten a nested array object into a list
"""

# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------- IMPORTS --#

# Built-in
import argparse


# Third-party

# Local

# ------------------------------------------------------------------------------#
# ----------------------------------------------------------------- FUNCTIONS --#


def flatten_list_recursive(list_obj):
    """
    Recursively convert a nested list into a flat list
    input: list <list> - a list
    return: generator
    """
    for obj in list_obj:
        if isinstance(obj, list):
            yield from flatten_list(obj)
        else:
            yield obj


def flatten_list(list_obj):
    """
    Convert a nested list into a flat list
    input: list <list> - a list
    return: flattened list
    """
    if isinstance(list_obj, list):
        return list(flatten_list_recursive(list_obj))
    return False


def validate_arg(nested_list_string):
    """
    Validates that the string nested_list_string can be evaluated to a python list
    input nested_list_string: <str> defines a list in python syntax
    return: list (if successful) or False
    """
    if isinstance(nested_list_string, str):
        try:
            nested_list = eval(nested_list_string)
        except (SyntaxError):
            print('\nThere is a syntax error in the argument: "{}"' \
                  .format(nested_list_string))
            return False
    if isinstance(nested_list, list):
        return nested_list
    print('\nPlease enter a python list')
    return False


def flatten_list_from_string(nested_list_string):
    return flatten_list(validate_arg(nested_list_string))


def main(**kwargs):
    """
    The executable portion of this module allows flatten_list()
    to be demonstrated interactively
    """
    nested_list = kwargs.get('nested_list', None)
    flat_list = flatten_list_from_string(nested_list)
    if flat_list == []:
        print('[]')
    elif flat_list:
        print(flat_list)


def _get_parsed_args(print_help=False):
    msg = 'utility to flatten a nested array object into a list'
    arg_parser = argparse.ArgumentParser(description=msg)
    msg = 'nested list defined in python syntax--no spaces (e.g. [[1,2,[3]],4])'
    arg_parser.add_argument('nested_list', nargs='?', help=msg)
    return vars(arg_parser.parse_args())


if __name__ == "__main__":
    main(**_get_parsed_args())