#!/usr/bin/python -O

##############################
# Scott Wiedemann            #
# Project10 JackTokenizer.py #
##############################

# some libraries we will use
import re
import sys
from Token import Token

################################
# JackTokenizer Module         #
################################
class JackTokenizer:

	_Keywords = [	"class",
					"method",
					"function",
					"constructor",
					"int",
					"boolean",
					"char",
					"void",
					"var",
					"static",
					"field",
					"let",
					"do",
					"if",
					"else",
					"while",
					"return",
					"true",
					"false",
					"null",
					"this"
	]

	_Symbols = [	"{",
					"}",
					"(",
					")",
					"[",
					"]",
					".",
					",",
					";",
					"+",
					"-",
					"*",
					"/",
					"&",
					"|",
					"<",
					">",
					"=",
					"~",
					"\""
	]

	# stores all the _Tokens for a given text
	_Tokens = [];

	# used to store the state of the token of concern
	_CurrentIndex = 0;

	def __init__(self, InputFile):

		self._Tokens = [];
		self._CurrentIndex = 0;

		# read in the text from the input file
		jackText=InputFile.read()

		# remove comments
		jackText=re.sub("(//.*\n)|(/\*(.|\n)*?\*/)", "", jackText).strip()

		jackText=re.sub("\"", "\"\n", jackText)

		# get quoteGroups
		quoteGroups = re.findall(r"\"\n.*\"", jackText)
		i =0
		while i<len(quoteGroups):
			quoteGroups[i]=re.sub("\n", "", quoteGroups[i])
			quoteGroups[i]=re.sub("\"", "", quoteGroups[i])
			i=i+1

		# take care of Symbols #
		for symbol in self._Symbols:
			jackText=re.sub("\\"+symbol, " "+symbol+" ", jackText)

		# replace \
		jackText=re.sub(r"\\", " \ ", jackText)

		# remove white space
		#jackText=re.sub("\n\s*\n*", "\n", jackText)

		#tokenize the text and store in a temp list
		tempTokens = jackText.split()

		temptokentype="";

		i = 0
		j = 0
		# find type of token in order to make new token
		while i < len(tempTokens):
			if tempTokens[i] == "\"":
				del tempTokens[i]
				while(tempTokens[i]!="\""):
					del tempTokens[i]
				tempTokens[i]=quoteGroups[j]
				j=j+1
				temptokentype=Token._TokenType[4]
			elif tempTokens[i] in self._Keywords:
				temptokentype=Token._TokenType[0]
			elif tempTokens[i] in self._Symbols:
				temptokentype=Token._TokenType[1]
			elif re.match("\d+", tempTokens[i]):
				temptokentype=Token._TokenType[3]
			elif re.match("[a-zA-Z_]+[a-zA-Z0-9_]*", tempTokens[i]):
				temptokentype=Token._TokenType[2]
			
			else:
				temptokentype="UNKNOWN_TYPE"
				try:
					raise Exception("Unknown token type: "+tempTokens[i]+"\n")
				except Exception, err:
					sys.stderr.write(str(err))
					return
			# create Tokens of type token and store in _Tokens
			self._Tokens.append(Token(temptokentype, tempTokens[i]))
			i=i+1

		self._CurrentIndex = 0;

		return

	def advance(self):
		self._CurrentIndex = self._CurrentIndex+1

	def hasMoreTokens(self):
		if self._CurrentIndex<len(self._Tokens):
			return True
		else:
			return False

	def retreat(self):
		self._CurrentIndex = self._CurrentIndex-1

	def token(self):
		return self._Tokens[self._CurrentIndex]

	def insert(self, Index, Token):
		self._Tokens.insert(Index, Token)
		self.advance()
