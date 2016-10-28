# -*- coding: utf-8 -*-


class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):
        return a+b

    def multiplication(self, a, b=None):
        if b is None:
            return a*a

        return a*b

    def poweroftwo(self, value):
        return 2 ** value

    def division(self, a, b):
        return a/b

