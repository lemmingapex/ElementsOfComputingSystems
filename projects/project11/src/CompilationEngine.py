#!/usr/bin/python -O

##################################
# Scott Wiedemann                #
# Project11 CompilationEngine.py #
##################################

# libraries
import sys
import os
import re

from JackTokenizer import JackTokenizer
from SymbolTable import SymbolTable
from VMWriter import VMWriter
from Token import Token

############################
# CompilationEngine Module #
############################
class CompilationEngine:

	_MyTokenizer = None
	_MyOutputFile = None
	_MyClassToken = None
	MyVMWriter = None
	CurrentSubroutine = None
	CurrentClass = None
	MySymbolTable = None
	LabelNum = 0
	numExpressions = 0

	_classTypes = [ "int",
					"char",
					"boolean"
	]

	_classVarDecOpenings = [	"static",
								"field"
	]

	_subroutineDecOpenings = [	"constructor",
								"function",
								"method"
	]

	_statementOpenings = [	"let",
							"if",
							"while",
							"do",
							"return"
	]

	_operators = ["+","-","*","/","&","|","<",">","="]
	_unaryOperators = {"-":"neg", "~":"not"}

	_keywordConstants = [	"null",
							"true",
							"false",
							"this"
	]

	subroutineNames = []
	classNames = []
	varNames = []

	def __init__(self, Tokenizer, OutputFile):

		self._MyTokenizer=Tokenizer
		self._MyOutputFile=OutputFile
		self.MyVMWriter=VMWriter(self._MyOutputFile)
		self.MySymbolTable=SymbolTable()
		self.CurrentSubroutine = None
		self.CurrentClass = None
		self.LabelNum = 0
		self.numExpressions = 0

		return

	def compileClass(self):
		classText="class"

		if self.token().text() != classText:
			try:
				raise Exception("Keyword '"+classText+"' expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

		self._MyClassToken=Token(None)

		# first insert: 'class'
		self.insert(self._MyClassToken, "class", Token.Keyword)
		# class name
		self.MySymbolTable=SymbolTable()
		self.CurrentClass=self.token().text()
		self.classNames.append(self.token().text())

		self.insert(self._MyClassToken, None, Token.Identifier)
		self.insert(self._MyClassToken, "{", Token.Symbol)

		while(	self._MyTokenizer.hasMoreTokens() and
				self.token().text() in self._classVarDecOpenings):
			self.compileClassVarDec(self._MyClassToken)

		while(	self._MyTokenizer.hasMoreTokens() and
				self.token().type() == Token.Keyword and
				self.token().text() in self._subroutineDecOpenings):
			self.compileSubroutineDec(self._MyClassToken)

		self.insert(self._MyClassToken, "}", Token.Symbol)
		self.CurrentClass=None

	def compileClassVarDec(self, ParentToken):
		# 'classVarDec'
		ParentToken = self.insert(ParentToken, None, None, "classVarDec")

		# symbol* : temp vars to add to symbol table 
		symbolKind=None
		# ('static' | 'field')
		if(self.token().text() in self._classVarDecOpenings):
			symbolKind=self.token().text()
			self.insert(ParentToken)
		
		symbolType=self.token().text()
		# type
		self.insert(ParentToken)

		symbolName=self.token().text()
		# varName
		self.insert(ParentToken, None, Token.Identifier)

		# add to class symbol table
		self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

		# (',' varName)*
		while(self.token().text() != ";"):
			self.insert(ParentToken, ",", Token.Symbol)
			symbolName=self.token().text()
			self.insert(ParentToken, None, Token.Identifier)
			self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

		# ';'
		self.insert(ParentToken, ";", Token.Symbol)

	def compileSubroutineDec(self, ParentToken):
		# 'subroutineDec'
		ParentToken = self.insert(ParentToken, None, None, "subroutineDec")

		self.isConstructor = False
		self.isMethod = False
		if self.token().text() == "constructor":
			self.isConstructor = True
		elif self.token().text() == "method":
			self.isMethod = True

		# ('constructor' | 'function' | 'method')
		if(self.token().text() in self._subroutineDecOpenings):
			self.insert(ParentToken)

		if(	self.token().text() == "void" or
			self.token().text() in self._classTypes or
			self.token().text() in self.classNames):
			self.insert(ParentToken)
		else:
			try:
				raise Exception("type expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

		# set up subroutine symbol table and add first entry: THIS, classname, ...
		self.MySymbolTable.startSubroutine()
		
		if self.isMethod:
			self.MySymbolTable.insert("this", SymbolTable.Arg, self.CurrentClass)

		self.CurrentSubroutine=self.token().text()

		# subroutineName
		self.subroutineNames.append(self.token().text())
		self.insert(ParentToken)

		self.insert(ParentToken, "(", Token.Symbol)
		self.compileParameterList(ParentToken)
		self.insert(ParentToken, ")", Token.Symbol)

		self.compileSubroutineBody(ParentToken)
		self.CurrentSubroutine=None

	def compileParameterList(self, ParentToken):
		# 'parameterList'
		ParentToken = self.insert(ParentToken, None, None, "parameterList")

		symbolKind="argument"

		if self.token().type() != Token.Symbol or self.token().text() != ")":
			# type
			symbolType=self.token().text()
			self.insert(ParentToken)
			# varName
			symbolName=self.token().text()
			self.insert(ParentToken, None, Token.Identifier)
			self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

		while self.token().type() != Token.Symbol or self.token().text() != ")":
			self.insert(ParentToken, ",", Token.Symbol)
			# type
			symbolType=self.token().text()
			self.insert(ParentToken)
			# varName
			symbolName=self.token().text()
			self.insert(ParentToken, None, Token.Identifier)
			self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

	def compileSubroutineBody(self, ParentToken):
		# 'subroutineBody'
		ParentToken = self.insert(ParentToken, None, None, "subroutineBody")

		self.insert(ParentToken, "{", Token.Symbol)

		if self.token().text() != "}":
			while self.token().text() == "var":
				self.compileVarDec(ParentToken)
			
			self.MyVMWriter.writeFunction(self.CurrentClass + "." + self.CurrentSubroutine, self.MySymbolTable.varCount(SymbolTable.Var))
						
			if self.isConstructor:
				self.MyVMWriter.writePush("constant", self.MySymbolTable.varCount(SymbolTable.Kinds["field"]))
				self.MyVMWriter.writeCall("Memory.alloc", 1)
				self.MyVMWriter.writePop("pointer", 0)
			elif self.isMethod:
				self.MyVMWriter.writePush(SymbolTable.Arg, 0)
				self.MyVMWriter.writePop("pointer", VMWriter.This)
			
			self.compileStatements(ParentToken)

		self.insert(ParentToken, "}", Token.Symbol)

	def compileVarDec(self, ParentToken):
		# 'varDec'
		ParentToken = self.insert(ParentToken, None, None, "varDec")

		symbolKind=self.token().text()
		self.insert(ParentToken, "var", Token.Keyword)

		# type
		symbolType=self.token().text()
		self.insert(ParentToken)

		# varName
		symbolName=self.token().text()
		self.varNames.append(self.token().text())
		self.insert(ParentToken, None, Token.Identifier)

		# add to corrent subroutine symbol table
		self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

		# (type varName)*
		while self.token().text() != ";":
			self.insert(ParentToken, ",", Token.Symbol)
			symbolName=self.token().text()
			self.varNames.append(self.token().text())
			self.insert(ParentToken, None, Token.Identifier)
			self.MySymbolTable.insert(symbolName, SymbolTable.Kinds[symbolKind], symbolType)

		# ';'
		self.insert(ParentToken, ";", Token.Symbol)

	def compileStatements(self, ParentToken):
		# 'statements'
		ParentToken = self.insert(ParentToken, None, None, "statements")

		while self.token().text() in self._statementOpenings:
			self.compileStatement(ParentToken)

	def compileStatement(self, ParentToken):

		if self.token().text() == "let":
			self.compileLet(ParentToken)
		elif self.token().text() == "if":
			self.compileIf(ParentToken)
		elif self.token().text() == "while":
			self.compileWhile(ParentToken)
		elif self.token().text() == "do":
			self.compileDo(ParentToken)
		elif self.token().text() == "return":
			self.compileReturn(ParentToken)
		else:
			try:
				raise Exception("staement expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return
			
	def compileLet(self, ParentToken):
		# 'letStatement'
		ParentToken = self.insert(ParentToken, None, None, "letStatement")
		
		# 'let'
		self.insert(ParentToken, "let", Token.Keyword)

		# need to check if it is a varname
		# varName
		varName = self.token().text()
		self.insert(ParentToken)
		isArray = False
		if self.token().text() == "[" and self.token().type() == Token.Symbol:
			self.insert(ParentToken, "[", Token.Symbol)
			isArray = True			
			if self.MySymbolTable.exists(varName):
				self.MyVMWriter.writePush(self.MySymbolTable.kindOf(varName), self.MySymbolTable.indexOf(varName))

				self.compileExpression(ParentToken)
				self.insert(ParentToken, "]", Token.Symbol)
				self.MyVMWriter.writeArithmetic("add")
				segment = "that"
				index = 0
		else:
			segment = self.MySymbolTable.kindOf(varName)
			index = self.MySymbolTable.indexOf(varName)

		self.insert(ParentToken, "=", Token.Symbol)
		self.compileExpression(ParentToken)
		
		if isArray:
			self.MyVMWriter.writePop("temp", 0)
			self.MyVMWriter.writePop("pointer", VMWriter.That)
			self.MyVMWriter.writePush("temp", 0)

		self.MyVMWriter.writePop(segment, index)
		self.insert(ParentToken, ";", Token.Symbol)

	def compileIf(self, ParentToken):
		# 'ifStatement'
		ParentToken = self.insert(ParentToken, None, None, "ifStatement")

		trueLabel = "IF_TRUE" + str(self.LabelNum)
		falseLabel = "IF_FALSE" + str(self.LabelNum)
		exitLabel = "IF_END" + str(self.LabelNum)
		self.LabelNum += 1

		self.insert(ParentToken, "if", Token.Keyword)
		self.insert(ParentToken, "(", Token.Symbol)
		self.compileExpression(ParentToken)
		self.insert(ParentToken, ")", Token.Symbol)
		self.MyVMWriter.writeIf(trueLabel)
		self.MyVMWriter.writeGoto(falseLabel)
		self.MyVMWriter.writeLabel(trueLabel)
		self.insert(ParentToken, "{", Token.Symbol)
		self.compileStatements(ParentToken)
		self.insert(ParentToken, "}", Token.Symbol)

		if self.token().text() == "else":
			self.MyVMWriter.writeGoto(exitLabel)
			self.MyVMWriter.writeLabel(falseLabel)
			self.insert(ParentToken, "else", Token.Keyword)
			self.insert(ParentToken, "{", Token.Symbol)
			self.compileStatements(ParentToken)
			self.insert(ParentToken, "}", Token.Symbol)
			self.MyVMWriter.writeLabel(exitLabel)
		else:
			self.MyVMWriter.writeLabel(falseLabel)

	def compileWhile(self, ParentToken):
		# 'whileStatement'
		ParentToken = self.insert(ParentToken, None, None, "whileStatement")

		startLabel = "WhileBegin" + str(self.LabelNum)
		endLabel = "WhileEnd" + str(self.LabelNum)
		self.LabelNum += 1

		self.insert(ParentToken, "while", Token.Keyword)
		self.insert(ParentToken, "(", Token.Symbol)
		self.MyVMWriter.writeLabel(startLabel)
		self.compileExpression(ParentToken)
		self.MyVMWriter.writeArithmetic("not")
		self.MyVMWriter.writeIf(endLabel)
		self.insert(ParentToken, ")", Token.Symbol)
		self.insert(ParentToken, "{", Token.Symbol)
		self.compileStatements(ParentToken)
		self.MyVMWriter.writeGoto(startLabel)
		self.insert(ParentToken, "}", Token.Symbol)
		self.MyVMWriter.writeLabel(endLabel)

	def compileDo(self, ParentToken):
		# 'doStatement'
		ParentToken = self.insert(ParentToken, None, None, "doStatement")

		self.insert(ParentToken, "do", Token.Keyword)
		self.compileSubroutineCall(ParentToken)
		self.MyVMWriter.writePop("temp", 0)
		self.insert(ParentToken, ";", Token.Symbol)

	def compileReturn(self, ParentToken):
		# 'returnStatement'
		ParentToken = self.insert(ParentToken, None, None, "returnStatement")

		# 'return'
		self.insert(ParentToken, "return", Token.Keyword)
		if self.token().text() != ";":
			self.compileExpression(ParentToken)
		else:
			self.MyVMWriter.writePush("constant", 0)
		# ';'
		self.insert(ParentToken, ";", Token.Symbol)
		self.MyVMWriter.writeReturn()

	def compileExpression(self, ParentToken):
		# 'expression'
		ParentToken = self.insert(ParentToken, None, None, "expression")

		functionSymbols = { "*":"Math.multiply",
							"/":"Math.divide"
							}

		operatorSymbols = {	"+":"add",
							"-":"sub",
							"&":"and",
							"|":"or",
							"<":"lt",
							">":"gt",
							"=":"eq"
							}

		# term
		self.compileTerm(ParentToken)

		while self.token().type() == Token.Symbol and self.token().text() in self._operators:
			# operator
			operator = self.token().text()
			self.insert(ParentToken, None, Token.Symbol)
			# term
			self.compileTerm(ParentToken)

			if operator in operatorSymbols.keys():
				self.MyVMWriter.writeArithmetic(operatorSymbols[operator])
			else:
				self.MyVMWriter.writeCall(functionSymbols[operator], 2)


	def compileTerm(self, ParentToken):
		# 'term'
		ParentToken = self.insert(ParentToken, None, None, "term")

		# be aware that this also handles subroutineCall!
		# there is no external call to compile subroutine here
		identifierName = self.token().text()
		if self.token().type() in Token.Identifier:
			
			# this is varName or subroutineName or className
			self.insert(ParentToken)

			# case for varName [ expression ]
			if (self.token().text() == "[" and self.token().type() == Token.Symbol):
				self.insert(ParentToken, "[", Token.Symbol)
				self.MyVMWriter.writePush(self.MySymbolTable.kindOf(identifierName), self.MySymbolTable.indexOf(identifierName))
				self.compileExpression(ParentToken)
				self.insert(ParentToken, "]", Token.Symbol)
				self.MyVMWriter.writeArithmetic("add")
				self.MyVMWriter.writePop("pointer", VMWriter.That)
				self.MyVMWriter.writePush("that", 0)
			# case for className | varName '.' subroutineName ( expressionList )
			elif(self.token().text()=="." and self.token().type() == Token.Symbol):
				self.insert(ParentToken, ".", Token.Symbol)
				# subroutineName
				subroutineName = self.token().text()
				self.insert(ParentToken)

				if self.MySymbolTable.exists(identifierName):
					self.MyVMWriter.writePush(self.MySymbolTable.kindOf(identifierName), self.MySymbolTable.indexOf(identifierName))

				self.numExpressions = 0
				self.insert(ParentToken, "(", Token.Symbol)
				self.compileExpressionList(ParentToken)
				self.insert(ParentToken, ")", Token.Symbol)

				if self.MySymbolTable.exists(identifierName):
					self.MyVMWriter.writeCall(self.MySymbolTable.typeOf(identifierName) + "." + subroutineName, self.numExpressions + 1)
				else:
					self.MyVMWriter.writeCall(identifierName + "." + subroutineName, self.numExpressions)

			# case for subroutineName ( expressionList )
			elif(self.token().text() == "(" and self.token().type() == Token.Symbol):
				self.insert(ParentToken, "(", Token.Symbol)
				self.MyVMWriter.writePush("pointer", VMWriter.This)
				self.compileExpressionList(ParentToken)
				self.numExpressions += 1
				self.insert(ParentToken, ")", Token.Symbol)
				self.MyVMWriter.writeCall(self.CurrentClass +  "." + identifierName, self.numExpressions)
			else:
				self.MyVMWriter.writePush(self.MySymbolTable.kindOf(identifierName), self.MySymbolTable.indexOf(identifierName))

		elif(self.token().text() == "(" and self.token().type() == Token.Symbol):
			self.insert(ParentToken, "(", Token.Symbol)
			self.compileExpression(ParentToken)
			self.insert(ParentToken, ")", Token.Symbol)

		elif self.token().text() in self._unaryOperators.keys():
			operator = self.token().text()
			self.insert(ParentToken, None, Token.Symbol)
			self.compileTerm(ParentToken)
			self.MyVMWriter.writeArithmetic(self._unaryOperators[operator])

		elif self.token().text() in self._keywordConstants:
			keywordText = self.token().text()
			if keywordText == "this":
				self.MyVMWriter.writePush("pointer", VMWriter.This) 
			elif keywordText == "null" or keywordText == "false":
				self.MyVMWriter.writePush("constant", 0)
			elif keywordText == "true":
				self.MyVMWriter.writePush("constant", 0)
				self.MyVMWriter.writeArithmetic("not")
			self.insert(ParentToken)
		elif self.token().type() == Token.IntegerConstant:
			self.MyVMWriter.writePush("constant", self.token().text())
			self.insert(ParentToken)
		elif self.token().type() == Token.StringConstant:
			stringText = self.token().text()
			self.MyVMWriter.writePush("constant", len(stringText))
			self.MyVMWriter.writeCall("String.new", 1)
			for character in stringText:
				self.MyVMWriter.writePush("constant", ord(character))
				self.MyVMWriter.writeCall("String.appendChar", 2)

			self.insert(ParentToken)
		else:
			try:
				raise Exception("Error parsing term\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

	def compileSubroutineCall(self, ParentToken):
		# the subroutineName OR className or varName
		firstToken = self.token().text()
		secondToken = ""
		self.insert(ParentToken)

		if(self.token().text()=="."):
			self.insert(ParentToken, ".", Token.Symbol)
			# subroutineName
			secondToken=self.token().text()
			self.insert(ParentToken)
			if self.MySymbolTable.exists(firstToken):
				self.MyVMWriter.writePush(self.MySymbolTable.kindOf(firstToken), self.MySymbolTable.indexOf(firstToken))
		else:
			self.MyVMWriter.writePush("pointer", VMWriter.This)

		self.insert(ParentToken, "(", Token.Symbol)
		self.compileExpressionList(ParentToken)
		self.insert(ParentToken, ")", Token.Symbol)

		if secondToken != "":
			if self.MySymbolTable.exists(firstToken):
				callName = self.MySymbolTable.typeOf(firstToken) + "." + secondToken
				self.numExpressions += 1
			else:
				callName = firstToken + "." + secondToken
		else:
			self.numExpressions += 1
			callName = self.CurrentClass + "." + firstToken

		self.MyVMWriter.writeCall(callName, self.numExpressions)

	def compileExpressionList(self, ParentToken):
		# 'subroutineCall'
		ParentToken = self.insert(ParentToken, None, None, "expressionList")
		self.numExpressions = 0
		while self.token().text() != ")":
			if self.token().text() == "," and self.token().type() == Token.Symbol:
				self.insert(ParentToken, ",", Token.Symbol)
			self.compileExpression(ParentToken)
			self.numExpressions += 1

	def insert(self, ParentToken, ExpectedText=None, ExpectedType=None, ChildTokenType=None):
		if(ChildTokenType == None):
			ChildToken=self.token()
		else:
			ChildToken=Token(ChildTokenType)
		
		ChildToken.Subroutine=self.CurrentSubroutine
		ChildToken.Class=self.CurrentClass

		if(ExpectedText != None and ChildToken.text() != None):
			if(ExpectedText != ChildToken.text()):
				try:
					raise Exception("Error parsing!  Expected: '"+ExpectedText+"'.  Received: '"+ChildToken.text()+"'.\n")
				except Exception, err:
					sys.stderr.write(str(err))
					return
		if(ExpectedType != None and ChildToken.type() != None):
			if(ExpectedType != ChildToken.type()):
				try:
					raise Exception("Error parsing!  Expected: '"+ExpectedType+"' type.  Received: '"+ChildToken.type()+"' type.\n")
				except Exception, err:
					sys.stderr.write(str(err))
					return

		ParentToken.appendChild(ChildToken)
		if(ChildToken.text() != None):
			self._MyTokenizer.advance()
		return ChildToken

	def token(self):
		return self._MyTokenizer.token()

	def outputTree(self, Node, space):
		space+="  "
		if Node.hasChildren():
			for child in Node._Children:
				self.writeVM(child, space)
		else:
				print space+Node.type() +" "+ (Node.text() if Node.text()!=None else "")
		return

