#!/usr/bin/env python3

"""
Name: Alexander Katrompas
Assignment: OOP Reference Example
Purpose: Runs the ShoppingCart verification testbed.
"""

from test import run_tests


def main() -> None:
    """
    Run the ShoppingCart verification suite.

    :param: none
    :raises: none
    :return: None
    :note: main.py is a testbed rather than an application interface
    """
    run_tests()

    return None


if __name__ == "__main__":
    main()
