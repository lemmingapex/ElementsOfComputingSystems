#!/usr/bin/python -O

######################
# Scott Wiedemann    #
# Project11 Token.py #
######################

################
# Token Module #
################
class Token:

	# token types
	Keyword="keyword"
	Symbol="symbol"
	Identifier="identifier"
	IntegerConstant="integerConstant"
	StringConstant="stringConstant"

	_Text = None
	_Type = None

	Class = None
	Subroutine = None

	_Children=[]

	def __init__(self, type, text=None):
		self._Type=type
		self._Text=text
		self._Children=[]
		self.Class = None
		self.Subroutine = None
		return

	def type(self):
		return self._Type;

	def text(self):
		return self._Text;

	def appendChild(self, Token):
		self._Children.append(Token)
		return self._Children[len(self._Children)-1]

	def hasChildren(self):
		return len(self._Children)>0
