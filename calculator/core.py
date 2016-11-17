# -*- coding: utf-8 -*-
from math import factorial

class Calculator:

	def __init__(self):
		self.romanNumeralMap = (
			('M',  1000),
			('CM', 900),
			('D',  500),
			('CD', 400),
			('C',  100),
			('XC', 90),
			('L',  50),
			('XL', 40),
			('X',  10),
			('IX', 9),
			('V',  5),
			('IV', 4),
			('I',  1)
			)

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


	def roman_to_latin(self,s):
		for i in s:
			match = 0
			for numeral, integer in self.romanNumeralMap:
				if i == numeral:
					match+=1
			if match == 0:
				return "Error, Uknown letter."

			index = 0
			result = 0	

			while index < len(s):
				for numeral, integer in self.romanNumeralMap:
					if s[index:index+len(numeral)] == numeral:
						result += integer
						index += len(numeral)
						break
			return result

	def latin_to_roman(self,n):

			result = ""
			for numeral, integer in self.romanNumeralMap:
				while n >= integer:
					result += numeral
					n -= integer
			return result