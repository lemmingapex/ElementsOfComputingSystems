#!/usr/bin/python -O

#############################
# Scott Wiedemann           #
# Project11 JackAnalyzer.py #
#############################

# libraries
import sys
import os

from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine

# DRIVER to call CompilationEngine and JackTokenizer
def main():
	jackExtension=".jack"
	vmExtension=".vm"
	if len(sys.argv) != 2:
		print "Wrong number of arguments."
		print "Usage: " + sys.argv[0] + " <Prog"+jackExtension+"> | <Directory>\n"
		return 1
	else:
		ArgInputPath = sys.argv[1]
		InputFilePaths = []

		# discover input files and fill list InputFilePaths
		if os.path.isdir(ArgInputPath):
			for entry in os.listdir(ArgInputPath):
				fullpath=os.path.join(ArgInputPath,entry)
				if not os.path.isdir(fullpath):
					InputFilePaths.append(fullpath)
		else:
			InputFilePaths.append(ArgInputPath)

		for InputPath in InputFilePaths:
			# skip non-jack files
			if not InputPath.endswith(jackExtension):
				print "Skipping "+InputPath+". Not a "+jackExtension+" file."
				continue
			# get input file for reading
			try:
				InputFile = open(InputPath, "r")
			except IOError:
				print "The file \""+ InputPath + "\" does not exist."
				return 2

			# make a tokenizer
			MyTokenizer = JackTokenizer(InputFile)

			# close input file
			InputFile.close()

			OutputPath=os.path.splitext(InputPath)[0]+vmExtension
			# get output file for writing
			try:
				OutputFile = open(OutputPath, "w")
			except IOError:
				print "There was a problem writing to "+OutputPath+"."
				return 3

			# compilation engine
			MyCompilationEngine = CompilationEngine(MyTokenizer, OutputFile)

			# compile the class
			print "Writing to: "+OutputPath
			MyCompilationEngine.compileClass()

			# close output file
			OutputFile.close()

	return 0

# call to main
if __name__ == "__main__":
    main()

