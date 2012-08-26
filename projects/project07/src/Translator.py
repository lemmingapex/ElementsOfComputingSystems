#!/usr/bin/python -O

#####################################
# Scott Wiedemann                   #
# Project07 Translator.py           #
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
					"push":"MEMORY",
					"pop":"MEMORY",
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

		unquieID=0
		for inputFile in InputFiles:
			OutputFile.write("// from " + inputFile.name.split("/")[-1] + "\n")
			for line in inputFile:
				line=line.strip()
				# ignore comments and white space
				if(line == "\n" or line[0:2] == "//" or len(line) == 0):
					continue
				line = self.parse_line(line).lower()

				lineArgs = line.split(' ')
				while(len(lineArgs)<3):
					lineArgs.append("")

				# open file
				asmFileName = "./translations/"+lineArgs[0]+ ("_"+lineArgs[1] if lineArgs[1] != "" else lineArgs[1]) +".asm"
				try:
					asmCommandFile = open(asmFileName, "r")
				except IOError:
					print "The file \""+asmFileName+"\" does not exist.\n"
					return
				# get asm text
				asmCommand = asmCommandFile.read()

				if lineArgs[0] in self.Commands[9:11]: # push or pop
					asmCommand = asmCommand.replace("%%INDEX%%", lineArgs[2])
					asmCommand = asmCommand.replace("%%SEGMENT%%", self.SegmentMap[lineArgs[1]])
					if lineArgs[1] == "static":
						asmCommand = asmCommand.replace("%%FILENAME%%", inputFile.name.split("/")[-1][0:-3])
						asmCommand = asmCommand.replace("%%STATICADDRESS%%", lineArgs[2])

				if lineArgs[0] in self.Commands[3:6]: # eq, lt, gt
					asmCommand = asmCommand.replace("%%ID%%", str(unquieID))
					unquieID=unquieID+1

				OutputFile.write(asmCommand)

				asmCommandFile.close()
		print OutputFile.name+" written"
		return

	# remove unnecessary characters
	def parse_line(self, Line):
		# ignore end of line comments
		if Line.find("//") > -1:
			Line = Line[0:Line.find("//")]
		Line=Line
		return Line

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

