# -*- coding: utf-8 -*-


class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):
        return a+b

        if not a.isdigit():
            return "a not number"

        if not b.isdigit():
            return "b not number"
       
    def multiplication(self, a, b=None):
        if b is None:
            return a*a

        return a*b

    def poweroftwo(self, value):
        return 2 ** value

    def division(self, a, b):
        return a/b

