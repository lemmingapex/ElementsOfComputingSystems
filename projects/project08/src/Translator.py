#!/usr/bin/python -O

#####################################
# Scott Wiedemann                   #
# Project08 Translator.py           #
#####################################

# some libraries we need
import sys
import os

################################
# Parser Module                #
################################
class Parser:
	def __init__(self, InputFiles, OutputFile):
		# commands
		self.Commands = [ "add",
					"sub",
					"neg",
					"eq",
					"gt",
					"lt",
					"and",
					"or",
					"not",
					"push",
					"pop",
					"label",
					"goto",
					"if-goto",
					"function",
					"return",
					"call" ]

		# command types for each command
		self.CommandType = { "add":"ARITHMETIC",
					"sub":"ARITHMETIC",
					"neg":"ARITHMETIC",
					"eq":"ARITHMETIC",
					"gt":"ARITHMETIC",
					"lt":"ARITHMETIC",
					"and":"ARITHMETIC",
					"or":"ARITHMETIC",
					"not":"ARITHMETIC",
					"push":"STACK",
					"pop":"STACK",
					"label":"MEMORY",
					"goto":"MEMORY",
					"if-goto":"MEMORY",
					"function":"MEMORY",
					"return":"MEMORY",
					"call":"MEMORY" }

		# vm to asm memory segment names
		self.SegmentMap = {	"local":"LCL",
							"argument":"ARG",
							"this":"THIS",
							"that":"THAT",
							"pointer":"3",
							"static":"",
							"temp":"5",
							"constant":"SP" }

		# vm to asm memory segment names
		self.ASMFileNames = {	"":"",
								"local":"_local",
								"argument":"_argument",
								"this":"_this",
								"that":"_that",
								"pointer":"_pointer",
								"static":"_static",
								"temp":"_temp",
								"constant":"_constant",
								"label":"label",
								"goto":"goto",
								"if-goto":"if-goto",
								"function":"function",
								"return":"return",
								"call":"call" }

		unquieID=0
		currentFunction="Sys.init"

		# bootstrap
		self.boot_strapper(OutputFile, InputFiles)

		for inputFile in InputFiles:
			OutputFile.write("// from " + inputFile.name.split("/")[-1] + "\n")
			inputFile.seek(0)
			for line in inputFile:
				line=line.strip()
				# ignore comments and white space
				if(line == "\n" or line[0:2] == "//" or len(line) == 0):
					continue
				line = self.parse_line(line)

				lineArgs = line.split(' ')
				while(len(lineArgs)<3):
					lineArgs.append("")

				if self.CommandType[lineArgs[0]] == "ARITHMETIC" or self.CommandType[lineArgs[0]] == "STACK": # add, sub, neg, eq, gt, lt, and, or, not, push, pop
					asmFileName = "./translations/"+lineArgs[0]+ self.ASMFileNames[lineArgs[1]] +".asm"
				else: # label, goto, if-goto, function, return, call
					asmFileName = "./translations/"+self.ASMFileNames[lineArgs[0]] +".asm"

				# open asm file for current command
				try:
					asmCommandFile = open(asmFileName, "r")
				except IOError:
					print "The file \""+asmFileName+"\" does not exist.\n"
					return
				# get asm text
				asmCommand = asmCommandFile.read()

				# close asm file
				try:
					asmCommandFile.close()
				except IOError:
					print "File writing error\n"

				# push or pop
				if lineArgs[0] in self.Commands[9:11]:
					asmCommand = asmCommand.replace("%%INDEX%%", lineArgs[2])
					asmCommand = asmCommand.replace("%%SEGMENT%%", self.SegmentMap[lineArgs[1]])
					if lineArgs[1].lower() == "static":
						asmCommand = asmCommand.replace("%%FILENAME%%", inputFile.name.split("/")[-1][0:-3])
						asmCommand = asmCommand.replace("%%STATICADDRESS%%", lineArgs[2])

				# eq, lt, gt
				if lineArgs[0] in self.Commands[3:6]:
					asmCommand = asmCommand.replace("%%ID%%", str(unquieID))
					unquieID=unquieID+1

				# label, goto, if-goto
				if lineArgs[0] in self.Commands[11:14]:
					asmCommand = asmCommand.replace("%%LABEL%%", currentFunction+"$"+lineArgs[1])

				# function
				if lineArgs[0] == self.Commands[14]:
					currentFunction = lineArgs[1]
					asmCommand = asmCommand.replace("%%FUNCTIONLABEL%%", lineArgs[1])
					asmCommand = asmCommand.replace("%%K%%", lineArgs[2])

				# call
				if lineArgs[0] == self.Commands[16]:
					asmCommand = asmCommand.replace("%%F%%", lineArgs[1])
					asmCommand = asmCommand.replace("%%N%%", lineArgs[2])
					asmCommand = asmCommand.replace("%%ID%%", str(unquieID))
					unquieID=unquieID+1

				# wirte command to file
				OutputFile.write(asmCommand)
			print inputFile.name+" processed"
		print OutputFile.name+" written"
		return

	# remove unnecessary characters
	def parse_line(self, Line):
		# ignore end of line comments
		if Line.find("//") > -1:
			Line = Line[0:Line.find("//")]
		# Line=Line.lower()
		return Line

	def boot_strapper(self, OutputFile, InputFiles):
		#############################
		# bootstrapper and sys.init #
		#############################

		writebootstrap=False

		# check for Sys.init in all in inputfiles
		for inputFile in InputFiles:
			inputFile.seek(0)
			for line in inputFile:
				line=line.strip()
				# ignore comments and white space
				if(line == "\n" or line[0:2] == "//" or len(line) == 0):
					continue
				line = self.parse_line(line)
				lineArgs = line.split(' ')
				while(len(lineArgs)<3):
					lineArgs.append("")
				if(lineArgs[1] == "Sys.init"):
					writebootstrap=True
					break

		if(writebootstrap==True):
			# bootstrapper
			bootStrapFileName="./translations/bootstrap.asm"

			try:
				bootStrapFile = open(bootStrapFileName, "r")
			except IOError:
				print "The file \""+bootStrapFileName+"\" does not exist.\n"
				return
			# get asm text
			bootStrapCode = bootStrapFile.read()

			# close file
			try:
				bootStrapFile.close()
			except IOError:
				print "File writing error\n"

			OutputFile.write(bootStrapCode)

			OutputFile.write("// Sys.init \n")
			# sys.init
			sysInitFileName="./translations/call.asm"

			try:
				sysInitFile = open(sysInitFileName, "r")
			except IOError:
				print "The file \""+sysInitFileName+"\" does not exist.\n"
				return
			# get asm text
			sysInitCode = sysInitFile.read()

			# close file
			try:
				sysInitFile.close()
			except IOError:
				print "File writing error\n"

			sysInitCode = sysInitCode.replace("%%F%%", "Sys.init")
			sysInitCode = sysInitCode.replace("%%N%%", "0")
			sysInitCode = sysInitCode.replace("%%ID%%", "0")

			OutputFile.write(sysInitCode)
			OutputFile.write("// end Sys.init\n")

			#################################
			# end bootstrapper and sys.init #
			#################################

# main (DRIVER)
def main():
	if len(sys.argv) != 2:
		print "Wrong number of arguments."
		print "Usage: " + sys.argv[0] + " <Prog.asm> | <Directory>\n"
		return 1
	else:
		InputFileName = sys.argv[1]
		InputFiles = []
		if os.path.isdir(InputFileName):
			Directory = os.listdir(InputFileName)
			if InputFileName.endswith("/"):
				InputFileName=InputFileName[:-1]
			OutputFileName=InputFileName + "/" + InputFileName.split("/")[len(InputFileName.split("/"))-1] + ".asm"
			for FileName in Directory:
				FullPath = InputFileName+"/"+FileName
				if FileName.endswith(".asm"):
					continue
				try:
					# read file
					InputFile = open(FullPath, "r")
				except IOError:
					print "The file \""+ FullPath + "\" does not exist.\n"
					return 2
				if not FileName.endswith(".vm"):
					print FileName + " is not a .vm file.\n"
					continue
				InputFiles.append(InputFile)
		else:
			OutputFileName=InputFileName[0:len(InputFileName)-3] + ".asm"
			try:
				# read file
				InputFile = open(InputFileName, "r")
			except IOError:
				print "The file \""+ InputFileName + "\" does not exist.\n"
				return 2
			if not InputFileName.endswith(".vm"):
				print InputFileName + " is not a .vm file.\n"
				return 3
			InputFiles.append(InputFile)
		try:
			# write file
			OutputFile = open(OutputFileName, "w")
		except IOError:
			print "There was a problem writing to file\n"
			return 3

		myParser = Parser(InputFiles, OutputFile)
	return 0

# call to main
if __name__ == "__main__":
    main()

