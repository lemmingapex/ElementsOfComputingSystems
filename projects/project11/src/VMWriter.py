#!/usr/bin/python -O

#########################
# Scott Wiedemann	    #
# Project11 VMWriter.py #
#########################

# libraries
import sys

###################
# VMWriter Module #
###################
class VMWriter:

	_commands = [	"add",
					"sub",
					"neg",
					"eq",
					"gt",
					"lt",
					"and",
					"or",
					"not"
	]

	This=0
	That=1

	_MyOutputFile = 0

	def __init__(self, OutputFile):

		self._MyOutputFile=OutputFile

		return

	def writePush(self, segment, index):
		self._MyOutputFile.write("push "+segment+" "+str(index)+"\n")
		return

	def writePop(self, segment, index):
		self._MyOutputFile.write("pop "+segment+" "+str(index)+"\n")
		return

	def writeArithmetic(self, command):
		if command in self._commands:
			self._MyOutputFile.write(command+"\n")
		else:
			try:
				raise Exception("'"+command+"' not valid command.\n")
			except Exception, err:
				sys.stderr.write(str(err))
				return
		return

	def writeLabel(self, label):
		self._MyOutputFile.write("label "+label+"\n")
		return

	def writeGoto(self, label):
		self._MyOutputFile.write("goto "+label+"\n")
		return

	def writeIf(self, label):
		self._MyOutputFile.write("if-goto "+label+"\n")
		return

	def writeCall(self, name, nArgs):
		self._MyOutputFile.write("call "+name+" "+str(nArgs)+"\n")
		return

	def writeFunction(self, name, nLocals):
		self._MyOutputFile.write("function "+name+" "+str(nLocals)+"\n")
		return

	def writeReturn(self):
		self._MyOutputFile.write("return\n")
		return
