import Token
#!/usr/bin/python -O

##################################
# Scott Wiedemann                #
# Project10 CompilationEngine.py #
##################################

# some libraries we will use
import sys
import os
import re

from xml.dom.minidom import Document
from xml.dom import getDOMImplementation

from JackTokenizer import JackTokenizer
from Token import Token

################################
# CompilationEngine Module     #
################################
class CompilationEngine:

	_MyTokenizer = 0
	_MyOutputFile = 0
	_MyXMLDocument = 0

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

	_operators = [	"+",
					"-",
					"*",
					"/",
					"&",
					"|",
					"<",
					">",
					"="
	]

	_unaryOperators = [	"-",
						"~"
	]

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
		self._MyXMLDocument=Document()
		#self._MyXMLDocument=getDOMImplementation().createDocument(None, None ,None)
		#self._MyXMLDocument.documentElement.unlink()
		

		return

	def compileClass(self):
		classText="class"

		if self._MyTokenizer.token().text() != classText:
			try:
				raise Exception("Keyword '"+classText+"' expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

		# first insert of xml doc 'class'
		Element = self._MyXMLDocument.createElement(classText)
		#self._MyXMLDocument=getDOMImplementation().createDocument(None, classText, None)
		self._MyXMLDocument.appendChild(Element)
		#Element=self._MyXMLDocument.documentElement

		# insert 'class'
		self.insert(Element, self._MyTokenizer.token())
		# insert class name
		self.classNames.append(self._MyTokenizer.token().text())
		self.insert(Element, self._MyTokenizer.token())
		# insert '{'
		self.insert(Element, self._MyTokenizer.token())

		while(	self._MyTokenizer.hasMoreTokens() and
				self._MyTokenizer.token().text() in self._classVarDecOpenings):
			self.compileClassVarDec(Element)

		while(	self._MyTokenizer.hasMoreTokens() and
				self._MyTokenizer.token().type() == Token._TokenType[0] and
				self._MyTokenizer.token().text() in self._subroutineDecOpenings):
			self.compileSubroutineDec(Element)

		# insert '}'
		self.insert(Element, self._MyTokenizer.token())

	def compileClassVarDec(self, Element):
		classVarDecText="classVarDec"
		# insert 'classVarDec'
		Element = self.insert(Element, Token(classVarDecText))

		# insert ('static' | 'field')
		if(self._MyTokenizer.token().text() in self._classVarDecOpenings):
			self.insert(Element, self._MyTokenizer.token())

		# need to break out logic, to catch more errors
		# insert "type varName (',' varName)*"
		while(self._MyTokenizer.token().text() != ";" and self._MyTokenizer.hasMoreTokens()):
			self.insert(Element, self._MyTokenizer.token())

		# insert ';'
		self.insert(Element, self._MyTokenizer.token())

	def compileSubroutineDec(self, Element):
		subroutineDecText="subroutineDec"
		# insert 'subroutineDec'
		Element = self.insert(Element, Token(subroutineDecText))

		# insert ('constructor' | 'function' | 'method')
		if(self._MyTokenizer.token().text() in self._subroutineDecOpenings):
			self.insert(Element, self._MyTokenizer.token())

		if(	self._MyTokenizer.token().text() == "void" or
			self._MyTokenizer.token().text() in self._classTypes or
			self._MyTokenizer.token().text() in self.classNames):
			self.insert(Element, self._MyTokenizer.token())
		else:
			try:
				raise Exception("type expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

		# insert subroutineName
		self.subroutineNames.append(self._MyTokenizer.token().text())
		self.insert(Element, self._MyTokenizer.token())

		# insert '('
		self.insert(Element, self._MyTokenizer.token())

		self.compileParameterList(Element)

		# insert ')'
		self.insert(Element, self._MyTokenizer.token())

		self.compileSubroutineBody(Element)


	def compileParameterList(self, Element):
		parameterListText="parameterList"
		# insert 'parameterList'
		Element = self.insert(Element, Token(parameterListText))

		while(	self._MyTokenizer.token().type() != Token._TokenType[1] or
				self._MyTokenizer.token().text() != ")"):

			# insert ',' ?
			if self._MyTokenizer.token().text() == ",":
				self.insert(Element, self._MyTokenizer.token())

			# insert type
			self.insert(Element, self._MyTokenizer.token())

			# insert varName
			self.insert(Element, self._MyTokenizer.token())


	def compileSubroutineBody(self, Element):
		subroutineBodyText="subroutineBody"
		# insert 'subroutineBody'
		Element = self.insert(Element, Token(subroutineBodyText))

		# insert '{'
		self.insert(Element, self._MyTokenizer.token())

		if self._MyTokenizer.token().text() != "}":
			while self._MyTokenizer.token().text() == "var":
				self.compileVarDec(Element)
			self.compileStatements(Element)

		# insert '}'
		self.insert(Element, self._MyTokenizer.token())

	def compileVarDec(self, Element):
		varDecText="varDec"
		# insert 'varDec'
		Element = self.insert(Element, Token(varDecText))

		# insert 'var'
		self.insert(Element, self._MyTokenizer.token())

		# insert type
		self.insert(Element, self._MyTokenizer.token())

		while self._MyTokenizer.token().text() != ";":

			# insert ',' ?
			if self._MyTokenizer.token().text() == ",":
				self.insert(Element, self._MyTokenizer.token())

			# insert varName
			self.subroutineNames.append(self._MyTokenizer.token().text())
			self.insert(Element, self._MyTokenizer.token())

		# insert ';'
		self.insert(Element, self._MyTokenizer.token())

	def compileStatements(self, Element):
		statementsText="statements"
		# insert 'statements'
		Element = self.insert(Element, Token(statementsText))

		while self._MyTokenizer.token().text() in self._statementOpenings:
			self.compileStatement(Element)

	def compileStatement(self, Element):

		if self._MyTokenizer.token().text() == "let":
			self.compileLet(Element)
		elif self._MyTokenizer.token().text() == "if":
			self.compileIf(Element)
		elif self._MyTokenizer.token().text() == "while":
			self.compileWhile(Element)
		elif self._MyTokenizer.token().text() == "do":
			self.compileDo(Element)
		elif self._MyTokenizer.token().text() == "return":
			self.compileReturn(Element)
		else:
			try:
				raise Exception("staement expected\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return
			
	def compileLet(self, Element):
		letStatementText="letStatement"
		# insert 'letStatement'
		Element = self.insert(Element, Token(letStatementText))
		
		# insert 'let'
		self.insert(Element, self._MyTokenizer.token())

		# need to check if it is a varname
		# insert varName
		self.insert(Element, self._MyTokenizer.token())

		if self._MyTokenizer.token().text() == "[":
			# insert '['
			self.insert(Element, self._MyTokenizer.token())
			self.compileExpression(Element)
			# insert ']'
			self.insert(Element, self._MyTokenizer.token())

		# insert '='
		self.insert(Element, self._MyTokenizer.token())
		self.compileExpression(Element)
		# insert ';'
		self.insert(Element, self._MyTokenizer.token())

	def compileIf(self, Element):
		ifStatementText="ifStatement"
		# insert 'ifStatement'
		Element = self.insert(Element, Token(ifStatementText))

		# insert 'if'
		self.insert(Element, self._MyTokenizer.token())
		# insert '('
		self.insert(Element, self._MyTokenizer.token())
		self.compileExpression(Element)
		# insert ')'
		self.insert(Element, self._MyTokenizer.token())
		# insert '{'
		self.insert(Element, self._MyTokenizer.token())
		self.compileStatements(Element)
		# insert '}'
		self.insert(Element, self._MyTokenizer.token())

		if(	self._MyTokenizer.hasMoreTokens() and
			self._MyTokenizer.token().text() == "else"):
			# insert 'else'
			self.insert(Element, self._MyTokenizer.token())
			# insert '{'
			self.insert(Element, self._MyTokenizer.token())
			slef.compileStatements(Element)
			# insert '}'
			self.insert(Element, self._MyTokenizer.token())

	def compileWhile(self, Element):
		whileStatementText="whileStatement"
		# insert 'whileStatement'
		Element = self.insert(Element, Token(whileStatementText))

		# insert 'while'
		self.insert(Element, self._MyTokenizer.token())
		# insert '('
		self.insert(Element, self._MyTokenizer.token())
		self.compileExpression(Element)
		# insert ')'
		self.insert(Element, self._MyTokenizer.token())
		# insert '{'
		self.insert(Element, self._MyTokenizer.token())
		self.compileStatements(Element)
		# insert '}'
		self.insert(Element, self._MyTokenizer.token())


	def compileDo(self, Element):
		doStatementText="doStatement"
		# insert 'doStatement'
		Element = self.insert(Element, Token(doStatementText))

		# insert 'do'
		self.insert(Element, self._MyTokenizer.token())
		self.compileSubroutineCall(Element)
		# insert ';'
		self.insert(Element, self._MyTokenizer.token())

	def compileReturn(self, Element):
		returnStatementText="returnStatement"
		# insert 'returnStatement'
		Element = self.insert(Element, Token(returnStatementText))

		# insert 'return'
		self.insert(Element, self._MyTokenizer.token())
		if self._MyTokenizer.token().text() != ";":
			self.compileExpression(Element)
		# insert ';'
		self.insert(Element, self._MyTokenizer.token())

	def compileExpression(self, Element):
		expressionText="expression"
		# insert 'expression'
		Element = self.insert(Element, Token(expressionText))

		# insert term
		self.compileTerm(Element)

		while(	self._MyTokenizer.token().type() == Token._TokenType[1] and
				self._MyTokenizer.token().text() in self._operators):
			# insert operator
			self.insert(Element, self._MyTokenizer.token())
			# insert term
			self.compileTerm(Element)

	def compileTerm(self, Element):
		termText="term"
		# insert 'term'
		Element = self.insert(Element, Token(termText))

		# be aware that this also handles subroutineCall!
		# there is no external call to compile subroutine
		if self._MyTokenizer.token().type() in Token._TokenType[2]:
			
			# this is varName or subroutineName or className
			self.insert(Element, self._MyTokenizer.token())

			# case for varName [ expression ]
			if (self._MyTokenizer.token().text() == "["):
				# insert '['
				self.insert(Element, self._MyTokenizer.token())
				# insert expression
				self.compileExpression(Element)
				# insert ']'
				self.insert(Element, self._MyTokenizer.token())
			# case for className | varName '.' subroutineName ( expressionList )
			elif(self._MyTokenizer.token().text()=="."):
				# insert '.'
				self.insert(Element, self._MyTokenizer.token())
				# insert subroutineName
				self.insert(Element, self._MyTokenizer.token())

				# insert '('
				self.insert(Element, self._MyTokenizer.token())
				self.compileExpressionList(Element)
				# insert ')'
				self.insert(Element, self._MyTokenizer.token())
			# case for subroutineName ( expressionList )
			elif(self._MyTokenizer.token().text() == "("):
				# insert '('
				self.insert(Element, self._MyTokenizer.token())
				self.compileExpressionList(Element)
				# insert ')'
				self.insert(Element, self._MyTokenizer.token())

		elif(self._MyTokenizer.token().text() == "("):
			# insert '('
			self.insert(Element, self._MyTokenizer.token())
			# insert expression
			self.compileExpression(Element)
			# insert ')'
			self.insert(Element, self._MyTokenizer.token())

		elif self._MyTokenizer.token().text() in self._unaryOperators:
			self.insert(Element, self._MyTokenizer.token())
			self.compileTerm(Element)

		elif(	self._MyTokenizer.token().text() in self._keywordConstants or
			self._MyTokenizer.token().type() == Token._TokenType[3] or
			self._MyTokenizer.token().type() == Token._TokenType[4]):
			self.insert(Element, self._MyTokenizer.token())
		else:
			try:
				raise Exception("Error parsing term\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return

	def compileSubroutineCall(self, Element):
		# insert the subroutineName OR className or varName
		self.insert(Element, self._MyTokenizer.token())

		if(self._MyTokenizer.token().text()=="."):
			# insert '.'
			self.insert(Element, self._MyTokenizer.token())
			# insert subroutineName
			self.insert(Element, self._MyTokenizer.token())

		# insert '('
		self.insert(Element, self._MyTokenizer.token())
		self.compileExpressionList(Element)
		# insert ')'
		self.insert(Element, self._MyTokenizer.token())

	def compileExpressionList(self, Element):
		expresionListText="expressionList"
		# insert 'subroutineCall'
		Element = self.insert(Element, Token(expresionListText))

		while( not(	self._MyTokenizer.token().text() == ")")):
			if self._MyTokenizer.token().text() == ",":
				# insert ','
				self.insert(Element, self._MyTokenizer.token())
			self.compileExpression(Element)

	def insert(self, Element, Token):
		tokenType = self._MyXMLDocument.createElement(Token.type())
		token = self._MyXMLDocument.createTextNode(" "+Token.text()+" ")
		tokenType.appendChild(token)
		if(Token.text() != ""):	
			self._MyTokenizer.advance()
		Element.appendChild(tokenType)
		return tokenType


	def writeXML(self):
#		xmlDocument = Document()
#		while self._MyTokenizer.hasMoreTokens():
#			tokenType = xmlDocument.createElement(self._MyTokenizer.token().type())
#			token = xmlDocument.createTextNode(" "+self._MyTokenizer.token().text()+" ")
#			tokenType.appendChild(token)
#			tokens.appendChild(tokenType)
#			self._MyTokenizer.advance()

		# fix line spaceing
		text_re = re.compile('>\n\s*([^<>\s*].*?)\n\s*</', re.DOTALL)

		uglyXML=text_re.sub('> \g<1></', self._MyXMLDocument.getElementsByTagName("class")[0].toprettyxml())
		#uglyXML=re.sub("\n\s*\n\s*</", " </", uglyXML)
		uglyXML=re.sub("\n\s*\n", "\n", uglyXML)

		self._MyOutputFile.write(uglyXML)
		#self._MyOutputFile.write(self._MyXMLDocument.toprettyxml())
		return 0

	def cleanDOM(self):
		self._MyXMLDocument.removeChild(self._MyXMLDocument.documentElement).unlink()
