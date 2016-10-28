# -*- coding: utf-8 -*-
from math import factorial

class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):

        if not (isinstance(a,int) | isinstance(a,float)):
            return "Error, first argument is a string value."

        if not (isinstance(b,int) | isinstance(b,float)):
            return "Error, second argument is a string value."

        return a+b
       
    def multiplication(self, a, b=None):

        if b is None:
            return a*a

        if not (isinstance(a,int) | isinstance(a,float)):
            return "Error, first argument is a string value."

        if not (isinstance(b,int) | isinstance(b,float)):
            return "Error, second argument is a string value."

        return a*b

    def poweroftwo(self, value):

        if not (isinstance(value,int) | isinstance(value,float)):
            return "Error, the argument is a string value."

        return value ** 2

    def division(self, a,b):

        if (b==0):
            return 'Error, the second argument can not be 0.'

        if not (isinstance(a,int) | isinstance(a,float)):
            return "Error, first argument is a string value."

        if not (isinstance(b,int) | isinstance(b,float)):
            return "Error, second argument is a string value."

        return a/b

    def factorial(self, value):

        if not isinstance(value,int):
            return "Error, argument must be a integer value."

        if not (isinstance(value,int) | isinstance(value,float)):
            return "Error, first argument is a string value."

        return factorial(value)