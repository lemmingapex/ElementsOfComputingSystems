######################
# Scott Wiedemann    #
# Project10 Token.py #
######################

################################
# Token Module                 #
################################
class Token:

	_TokenType = [	"keyword",
					"symbol",
					"identifier",
					"integerConstant",
					"stringConstant"
	]

	_Text = "";
	_Type = "";

	def __init__(self, type, text=""):
		self._Type=type
		self._Text=text
		return

	def type(self):
		return self._Type;

	def text(self):
		return self._Text;