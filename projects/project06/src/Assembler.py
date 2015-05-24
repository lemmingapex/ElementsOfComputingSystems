#!/usr/bin/python -O

#####################################
# Scott Wiedemann                   #
# Project06 Assembler.py            #
#####################################

# some libraries we need
import string, sys

################################
# Parser Module                #
################################
class Parser:
	def __init__(self, InputFile, OutputFile):
		# command types
		self.CommandTypes = [ "A_COMMAND","C_COMMAND","L_COMMAND","ERROR" ]

		# what line number are we on?
		CurrentLineNumber = -1
		# what is the current address index for RAM?
		self.AddressIndex = 16

		# our symbol table
		self.ST = SymbolTable()

		# first pass
		for line in InputFile:
			# ignore comments and white space
			if(line == "\n" or line[0:2] == "//"):
				continue
			line = self.parseLine(line)
			# link commands?
			if self.CommandTypes[2] == self.commandType(line):
				self.ST.Table[line[1:-2]] = CurrentLineNumber
			# a and c commands
			else:
				CurrentLineNumber += 1

		# return to begining of file
		InputFile.seek(0);

		# code per line to be written to file
		binaryCode=""

		# second pass
		for line in InputFile:
			# ignore comments and white space
			if(line == "\n" or line[0:2] == "//"):
				continue
			line = self.parseLine(line)
			# is this an a or c command
			commandType = self.commandType(line)
			if self.CommandTypes[0] == commandType:
				binaryCode = self.aInstruction(line[1:-1])
				OutputFile.write(binaryCode+"\n")
			elif self.CommandTypes[1] == commandType:
				binaryCode = self.cInstruction(line)
				# write it to file
				OutputFile.write(binaryCode+"\n")
		return

	# remove unnecessary characters
	def parseLine(self, Line):
		# ignore white space
		Line = string.join(Line.split(), "")
		# ignore end of line comments
		if Line.find("//") > -1:
			Line = Line[0:Line.find("//")]
		Line=Line+"\n"
		return Line

	# instruction type
	def commandType(self, Instruction):

		# c-instruction, a-instruction,	label or error?
		if Instruction[0] == "@":
			return self.CommandTypes[0] 	# a instruction
		elif Instruction.find(";") > -1 or Instruction.find("=") > -1:
			return self.CommandTypes[1]	# c instruction
		elif Instruction.find("(") > -1 and Instruction.find(")") > -1 and Instruction.find("(") < Instruction.find(")"):
			return self.CommandTypes[2]	# link
		else:
			return self.CommandTypes[3]	# doesn"t fit regex

	def aInstruction(self, Instruction):
		if Instruction.isdigit(): # it's a number
			value = Instruction
		elif Instruction in self.ST.Table.keys(): # is it a key in the symbolTable?
			value = self.ST.Table[Instruction]
		else: # it is a new variable
			self.ST.Table[Instruction] = self.AddressIndex
			value = self.AddressIndex
			self.AddressIndex += 1
		# convert to binary and pad to 15 chars
		return '0' + str(bin(int(value))[2:].zfill(15))

	def cInstruction(self, Instruction):
		CM = Code()
		# handle each part of the instruction
		return "111" + CM.comp(Instruction) + CM.dest(Instruction) + CM.jump(Instruction)

################################
# Code Module                  #
################################
class Code:
	def __init__(self):
		return

	# comp for c instructions
	def comp(self, Instruction):
		if Instruction.find("=") > -1:
			Instruction = Instruction[Instruction.find("=")+1:-1]
		elif Instruction.find(";") > -1:
			Instruction = Instruction[0:Instruction.find(";")]
		else:
			return "0000000"
		
		code = {"0"  :"0101010",
			"1"  :"0111111",
			"-1" :"0111010",
			"D"  :"0001100",
			"A"  :"0110000",
			"!D" :"0001101",
			"!A" :"0110001",
			"-D" :"0001111",
			"-A" :"0110011",
			"D+1":"0011111",
			"A+1":"0110111",
			"D-1":"0001110",
			"A-1":"0110010",
			"D+A":"0000010",
			"D-A":"0010011",
			"A-D":"0000111",
			"D&A":"0000000",
			"D|A":"0010101",
			"M"  :"1110000",
			"!M" :"1110001",
			"-M" :"1110011",
			"M+1":"1110111",
			"M-1":"1110010",
			"D+M":"1000010",
			"D-M":"1010011",
			"M-D":"1000111",
			"D&M":"1000000",
			"D|M":"1010101"}

		return code[Instruction]

	# dest for c instructions
	def dest(self, Instruction):
		if Instruction.find("=") == -1:
			return "000"

		code = {"M"  :"001",
			"D"  :"010",
			"MD" :"011",
			"A"  :"100",
			"AM" :"101",
			"AD" :"110",
			"AMD":"111"}

		return code[Instruction[0:Instruction.find("=")]]

	# jump for c instructions
	def jump(self, Instruction):
		if Instruction.find(";") == -1:
			return "000"

		code = {"JGT":"001",
			"JEQ":"010",
			"JGE":"011",
			"JLT":"100",
			"JNE":"101",
			"JLE":"110",
			"JMP":"111"}

		return code[Instruction[Instruction.find(";")+1:-1]]

################################
# SymbolTable Module           #
################################
class SymbolTable:
	ST = { }
	# used to hold all symbol info
	def __init__(self):
		self.Table = {"SP":"0\n",
			"LCL" :"1\n",
			"ARG" :"2\n",
			"THIS":"3\n",
			"THAT":"4\n",
			"R0"  :"0\n",
			"R1"  :"1\n",
			"R2"  :"2\n",
			"R3"  :"3\n",
			"R4"  :"4\n",
			"R5"  :"5\n",
			"R6"  :"6\n",
			"R7"  :"7\n",
			"R8"  :"8\n",
			"R9"  :"9\n",
			"R10" :"10\n",
			"R11" :"11\n",
			"R12" :"12\n",
			"R13" :"13\n",
			"R14" :"14\n",
			"R15" :"15\n",
			"SCREEN":"16384\n",
			"KBD" :"24576\n"}
		return

# main (DRIVER)
def main():
	if len(sys.argv) != 2:
		print "Wrong number of arguments."		
		print "Usage: " + sys.argv[0] + " Prog.asm\n"
		return 1
	else:
		InputFileName = sys.argv[1]
		try:
			# read file
			InputFile = open(InputFileName, "r")
		except IOError:
			print "The file \""+ InputFileName + "\" does not exist.\n"
			return 2
		if not InputFileName.endswith(".asm"):
			print "This is not an .asm file.\n"
			return 3
		try:
			# write file
			OutputFile = open(InputFileName[0:len(InputFileName)-4] + ".hack", "w")
		except IOError:
			print "There was a problem writing to file\n"
			return 4
		myParser = Parser(InputFile, OutputFile)
	return 0

# call to main
if __name__ == "__main__":
    main()

