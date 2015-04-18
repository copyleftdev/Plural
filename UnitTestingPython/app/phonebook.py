#!/usr/bin/env python

#Author: Don Johnson <dj@codetestcode.io>


class Phonebook:

    def __init__(self):
        self.entries = {}

    def add(self, name , number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def valid_names(self, names):
        if type(names) == str:
            return True
        else:
            return False

    def valid_numbers(self, numbers):
        if type(numbers) == int:
            return True
        else:
            False
