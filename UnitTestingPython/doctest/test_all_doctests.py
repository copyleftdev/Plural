import unittest
import doctest
import yatzy

def load_tests(loader, tests, ignore):
    test.addTests(doctest.DocTestSuite(yatzy))
    return tests
