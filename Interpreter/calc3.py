# Token types
#
#EOF token is used to indicate that 
#there is no more input left for lexical analysis
INTEGER,PLUS,MINUS,MULTI,DIVISION,EOF='INTEGER','PLUS','MINUS','MULTI','DIVISION','EOF'

class Token(object):
	def __init__(self,type,value):
		#token type:INTEGER,PLUS,or EOF
		self.type=type
		self.value=value
	def __str__(self):
		"""String representation of the class instance.
		Examples:
			Token(INTEGER,3)
			Token(PLUS '+')
		"""
		return 'Token({type},{value})'.format(
			type=self.type,
			value=self.value
		)
	#__repr__=__str__
class Interpreter(object):
	def __init__(self,text):
		#client string input,e.g."3+5"
		self.text=text
		#self.pos is an index into self.text
		self.pos=0
		self.current_token=None
		self.current_char=text[self.pos]
	#####################################
	#Lexer Code                         #
	#####################################
	def error(self):
		raise Exception('Error parsing input')
		#手工引发异常

	def advance(self):
		"""
		Advance the 'pos' Pointer and set the 'current_char' Variable.
		"""
		self.pos+=1
		if self.pos>len(self.text)-1:
			self.current_char=None
		else:
			self.current_char=self.text[self.pos]

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def integer(self):
		"""
		Return a (multidigit) integer consumed form the input.
		"""
		result=''
		while self.current_char is not None and self.current_char.isdigit():
			result+=self.current_char
			self.advance()
		return int(result)
	
	def get_next_token(self):
		"""
		Lexical analyzer(also known as scanner or tokenizer)
		This method is responsible for breaking a sentence 
		apart into tokens.One token at a time.
		"""
		while self.current_char is not None:
			if self.current_char.isspace():
				self.skip_whitespace()
				continue
			if self.current_char.isdigit():
				return Token(INTEGER,self.integer())
			if self.current_char=='+':
				self.advance()
				return Token(PLUS,'+')
			if self.current_char=='-':
				self.advance()
				return Token(MINUS,'-')
			if self.current_char=='*':
				self.advance()
				return Token(MULTI,'*')
			if self.current_char=='/':
				self.advance()
				return Token(DIVISION,'/')		
			self.error()
		return Token(EOF,None)
	###########################
	#Parser/Interpreter Code  #
	###########################
	def eat(self,token_type):
		# compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
		if self.current_token.type==token_type:
			self.current_token=self.get_next_token()
		else:
			self.error()

	def term(self):
		'''
		Return an INTERGER token value.
		'''
		token=self.current_token
		self.eat(INTEGER)
		return token.value

	def expr(self):
		'''
		Arithmetic expression parser/Interpreter.
		'''
		# set current token to the first token taken from the input
		self.current_token = self.get_next_token()

		result=self.term()
		while self.current_token.type in(PLUS,MINUS):
			token=self.current_token
			if token.type==PLUS:
				self.eat(PLUS)
				result=result+self.term()
			elif token.type==MINUS:
				self.eat(MINUS)
				result=result-self.term()
		return result
	
def main():
	while True:
		try:
			text=input('calc>')
		except EOFError:
			break
		if not text:
			continue
		interpreter=Interpreter(text)
		result=interpreter.expr()
		print(result)

if __name__=='__main__':
	main()