#!/usr/bin/env python3

"""
Name: Alexander Katrompas
Assignment: OOP Reference Example
Purpose: Demonstrates a small reusable class with encapsulated state,
         searching, sorting, and simple calculations.
"""


class ShoppingCart:
    """
    Represent one shopping cart and the items it contains.

    Each ShoppingCart object owns its own customer name and item collection.
    Items are stored as (item_name, price) tuples.

    :note: this class is intentionally small and instructional
    """

    def __init__(self, customer_name: str) -> None:
        """
        Initialize an empty shopping cart.

        :param customer_name: the name associated with this shopping cart
        :raises: none
        :return: None
        :note: the new cart begins with no items
        """
        self._customer_name: str = customer_name
        self._items: list[tuple[str, float]] = []

    def get_customer_name(self) -> str:
        """
        Return the customer name associated with the cart.

        :param: none
        :raises: none
        :return: the customer name
        :note: none
        """
        return self._customer_name

    def get_items(self) -> list[tuple[str, float]]:
        """
        Return a copy of the cart's item collection.

        :param: none
        :raises: none
        :return: a new list containing the current item tuples
        :note: changing the returned list does not change the ShoppingCart
        """
        
        return list(self._items)

    def add_item(self, item_name: str, price: float) -> bool:
        """
        Add a valid item to the shopping cart.

        :param item_name: the name of the item to add
        :param price: the item's price
        :raises: none
        :return: True when the item is added or False when validation fails
        :note: item names must be unique and price must be positive
        """
        success = False
        numeric_price = (
            isinstance(price, (int, float))
            and not isinstance(price, bool)
        )

        if numeric_price and price > 0:
            item_is_new = self.find_item(item_name) is None

            if item_is_new:
                self._items.append(
                    (item_name, float(price))
                )
                success = True

        return success

    def find_item(self, item_name: str) -> tuple[str, float] | None:
        """
        Find one item by name using linear search.

        :param item_name: the item name to locate
        :raises: none
        :return: the matching item tuple or None when the item is not present
        :note: the search does not require the collection to be sorted
        """
        index = 0
        result = None

        while index < len(self._items) and result is None:
            if self._items[index][0] == item_name:
                result = self._items[index]

            index += 1

        return result

    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the cart.

        :param: none
        :raises: none
        :return: the total price or 0.0 when the cart is empty
        :note: none
        """
        total = 0.0

        for item_name, price in self._items:
            total += price

        return total

    def sort_by_name(self) -> None:
        """
        Sort the internal item collection by item name.

        :param: none
        :raises: none
        :return: None
        :note: uses Selection Sort in ascending item-name order
        """
        for start in range(len(self._items) - 1):
            smallest = start

            for index in range(start + 1, len(self._items)):
                if self._items[index][0] < self._items[smallest][0]:
                    smallest = index

            if smallest != start:
                temporary = self._items[start]
                self._items[start] = self._items[smallest]
                self._items[smallest] = temporary

        return None
