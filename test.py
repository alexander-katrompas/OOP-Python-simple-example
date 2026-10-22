#!/usr/bin/env python3

"""
Name: Alexander Katrompas
Assignment: OOP Reference Example
Purpose: Demonstrates a small verification suite for ShoppingCart.
"""

from shopping_cart import ShoppingCart


def test_basic_cart() -> None:
    """
    Verify construction, item addition, searching, and total calculation.

    :param: none
    :raises AssertionError: if the ShoppingCart behavior is incorrect
    :return: None
    :note: this test evolves one object through several related states
    """
    cart = ShoppingCart("Alex")

    assert cart.get_customer_name() == "Alex"
    assert cart.get_items() == []
    assert cart.calculate_total() == 0.0

    assert cart.add_item("Coffee", 4.50) is True
    assert cart.add_item("Bread", 3.25) is True
    assert cart.add_item("Cheese", 6.75) is True

    assert cart.find_item("Bread") == (
        "Bread",
        3.25,
    )
    assert cart.find_item("Milk") is None
    assert cart.calculate_total() == 14.50

    return None


def test_sort_and_encapsulation() -> None:
    """
    Verify Selection Sort and defensive-copy encapsulation.

    :param: none
    :raises AssertionError: if sorting or encapsulation behavior is incorrect
    :return: None
    :note: the returned item list may be changed without changing the cart
    """
    cart = ShoppingCart("Jessica")

    assert cart.add_item("Tea", 5.00) is True
    assert cart.add_item("Apples", 4.00) is True
    assert cart.add_item("Rice", 3.00) is True

    cart.sort_by_name()

    assert cart.get_items() == [
        ("Apples", 4.0),
        ("Rice", 3.0),
        ("Tea", 5.0),
    ]

    outside_copy = cart.get_items()
    outside_copy.append(
        ("Hacked Item", 1.0)
    )

    assert cart.find_item("Hacked Item") is None
    assert len(cart.get_items()) == 3

    return None


def test_independent_objects() -> None:
    """
    Verify that separate ShoppingCart objects maintain independent state.

    :param: none
    :raises AssertionError: if one object incorrectly changes another object
    :return: None
    :note: demonstrates one class definition producing independent instances
    """
    first_cart = ShoppingCart("Customer One")
    second_cart = ShoppingCart("Customer Two")

    assert first_cart.add_item("Notebook", 2.50) is True
    assert second_cart.add_item("Pen", 1.25) is True

    assert first_cart.find_item("Pen") is None
    assert second_cart.find_item("Notebook") is None

    return None


def run_tests() -> None:
    """
    Run the ShoppingCart reference verification suite.

    :param: none
    :raises: none
    :return: None
    :note: each test is independent and reports its own pass or failure
    """
    tests = (
        test_basic_cart,
        test_sort_and_encapsulation,
        test_independent_objects,
    )

    passed = 0

    print("ShoppingCart Verification")
    print()

    for test_function in tests:
        try:
            test_function()
            passed += 1
            print(
                f"PASS: {test_function.__name__}"
            )
        except Exception as error:
            print(
                f"FAIL: {test_function.__name__}"
            )
            print(
                f"      {error}"
            )

    print()
    print(
        f"{passed}/{len(tests)} tests passed."
    )

    return None
