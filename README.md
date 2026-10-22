# OOP Reference Example — ShoppingCart

## Purpose

This repository is a small reference example for the introductory
object-oriented programming material in COSC 1336.

It demonstrates a **basic architecture pattern** for creating stand alone classes for use in other applications.

The important idea is not shopping carts. The important idea is how a reusable
class is designed, instantiated, passed around, and verified.

## What the Example Demonstrates

The project shows:

- one class with non-public instance state;
- a constructor that initializes object state;
- public methods that control access to that state;
- multiple independent objects created from one class;
- a collection owned by an object;
- defensive copying for encapsulation;
- explicit iterative linear search;
- Selection Sort implemented inside the class;
- a calculation based on object state;
- a separate testing module;
- a small test runner;
- `main.py` used as a testbed rather than as an application; and
- complete course-standard documentation.

## Project Structure

```text
.
├── README.md
├── shopping_cart.py
├── test.py
└── main.py
```

### `shopping_cart.py`

Contains the reusable `ShoppingCart` class. This is the component being
developed and verified.

### `test.py`

Contains a small verification suite. The tests create `ShoppingCart` objects,
call the public interface, change object state, and verify behavior.

### `main.py`

Runs the test suite. It does not contain a menu or interactive application.

## The Class

Each `ShoppingCart` object owns:

```text
customer name
collection of item tuples
```

The internal collection is:

```python
self._items
```

Each item is:

```text
(item_name, price)
```

The public interface is:

```text
get_customer_name()
get_items()
add_item()
find_item()
calculate_total()
sort_by_name()
```

## Encapsulation

Outside code does not directly manipulate:

```python
cart._items
```

Instead, it uses the public methods.

`get_items()` returns a **copy** of the internal list. Another programmer can
inspect the cart without receiving direct access to its internal collection.

## Searching

`find_item()` performs an explicit iterative **linear search**. The collection
does not need to be sorted first.

## Sorting

`sort_by_name()` uses **Selection Sort** to sort the cart's internal collection
in ascending item-name order.

Professional software would normally use the language or library sorting
implementation. Selection Sort is used here deliberately because the goal is
to demonstrate how a familiar algorithm can become behavior owned by an object.

## Multiple Objects

The tests create more than one `ShoppingCart`:

```python
first_cart = ShoppingCart("Customer One")
second_cart = ShoppingCart("Customer Two")
```

Both use the same class definition, but each object owns independent state.

## Testing

The example contains only three tests:

```text
test_basic_cart()
test_sort_and_encapsulation()
test_independent_objects()
```

They are intentionally small.

The final project requires a substantially larger and more systematic test
suite, but the architecture is the same:

```text
main.py
    ↓
run_tests()
    ↓
test functions
    ↓
objects created from the class
    ↓
public methods exercised and verified
```

## Run

From the repository directory:

```bash
python main.py
```

Expected result:

```text
ShoppingCart Verification

PASS: test_basic_cart
PASS: test_sort_and_encapsulation
PASS: test_independent_objects

3/3 tests passed.
```

## What to Study

Focus on these questions:

1. What state belongs inside the class?
2. Why are `_customer_name` and `_items` non-public?
3. Why does outside code call methods instead of directly changing `_items`?
4. How does `self` identify the particular object being used?
5. How can several objects share one class definition but maintain different state?
6. Why does `get_items()` return a copy?
7. Why does `find_item()` belong to `ShoppingCart`?
8. Why does `sort_by_name()` modify the cart's internal state?
9. Why are the tests outside the class?
10. Why is `main.py` only responsible for running the testbed?

The final project is larger and more demanding, but these are the same core
object-oriented engineering ideas.
