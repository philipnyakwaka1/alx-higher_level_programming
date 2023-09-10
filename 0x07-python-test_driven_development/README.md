         Test-Driven Development (TDD) with doctest and unittest

Test-Driven Development (TDD) is a software development methodology that emphasizes writing tests before writing code. This approach ensures code correctness, maintains clear documentation, and supports iterative development. In Python, two popular testing frameworks for TDD are doctest and unittest. Here's a brief overview of how TDD works with each of them:

                      TDD with doctest

Purpose: doctest focuses on testing code through embedded documentation.

How it works: Write tests as part of your documentation in docstrings. doctest extracts these examples and runs them as tests to verify code behavior.

Example:
def add(a, b):
    """
    This function takes two numbers, 'a' and 'b', and returns their sum.
    
    >>> add(2, 3)
    5
    
    >>> add(-2, 5)
    3
    """
    return a + b

TDD Approach: Write test examples in docstrings before implementing the code. Run doctest to ensure that the examples pass. Implement the code to make the tests pass, thereby synchronizing documentation and code.


                     TDD with unittest

Purpose: unittest provides a structured framework for unit testing in Python.

How it works: Create test classes that inherit from unittest.TestCase and define test methods within these classes. Use assertion methods provided by unittest to check code behavior.

Example:
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = add(-2, 5)
        self.assertEqual(result, 3)

TDD Approach: Define test cases in classes and methods before writing the actual code. Run tests using unittest to ensure code correctness. Implement the code to make the tests pass, focusing on isolating and testing specific code units.

             
            Choosing Between doctest and unittest

The choice between doctest and unittest depends on your project's requirements. doctest is well-suited for keeping documentation and tests closely aligned, while unittest provides a more structured approach to unit testing. Regardless of the framework you choose, TDD promotes code quality, correctness, and maintainability.

