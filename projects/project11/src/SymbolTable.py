#!/usr/bin/python -O

############################
# Scott Wiedemann		   #
# Project11 SymbolTable.py #
############################

# libraries
import sys

######################
# SymbolTable Module #
######################
class SymbolTable:

	Kind="kind"
	Type="type"
	Index="index"

	Static="static"
	Field="this"
	Arg="argument"
	Var="local"

	Kinds = {	"static":"static",
				"field":"this",
				"argument":"argument",
				"var":"local"
			}

	classTable = None
	subTable = None

	def __init__(self):
		self.classTable = dict()
		self.subTable = dict()
		return

	def startSubroutine(self):
		self.subTable = dict()

	def insert(self, identifierName, identifierKind, identifierType):
		if(identifierKind == SymbolTable.Static or identifierKind == SymbolTable.Field):
			self.classTable[identifierName] = dict(kind=identifierKind, type=identifierType, index=self.varCount(identifierKind))
		else:
			self.subTable[identifierName] = dict(kind=identifierKind, type=identifierType, index=self.varCount(identifierKind))
			
	def varCount(self, identifierKind):
		count = 0
		if(identifierKind == SymbolTable.Static or identifierKind == SymbolTable.Field):
			for key in self.classTable.keys():
				if self.classTable[key][self.Kind] == identifierKind:
					count += 1
		else:
			for key in self.subTable.keys():
				if self.subTable[key][self.Kind] == identifierKind:
					count += 1
		return count

	def kindOf(self, name):
		return self.fieldOf(name, "kind")

	def typeOf(self, name):
		return self.fieldOf(name, "type")

	def indexOf(self, name):
		return self.fieldOf(name, "index")

	def fieldOf(self, identifierName, identifierField):
		if identifierName in self.subTable:
			return self.subTable[identifierName][identifierField]
		elif identifierName in self.classTable:
			return self.classTable[identifierName][identifierField]
		else:
			try:
				raise Exception("'"+identifierName+"' not found in scope.\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return
	
	def exists(self, identifierName):
		return identifierName in self.classTable or identifierName in self.subTable

