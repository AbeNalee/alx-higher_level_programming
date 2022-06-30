#!/usr/bin/python3
# 100-magic-string.py
"""Prints a string n times the number of the iteration."""

def magic_string():
    """
    Print a string n times the number of the iteration
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "Best School")
