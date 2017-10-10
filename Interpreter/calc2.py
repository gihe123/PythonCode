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
		self.
		
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

	def error(self):
		raise Exception('Error parsing input')
		#手工引发异常

	def advance(self):
		self.pos+=1
		if self.pos>len(self.text)-1:
			self.current_char=None
		else:
			self.current_char=self.text[self.pos]

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def integer(self):
		result=''
		while self.current_char is not None and self.current_char.isdigit():
			result+=self.current_char
			self.advance()
		return int(result)
	
	def get_next_token(self):
		"""Lexical analyzer(also known as scanner or tokenizer)
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

	def eat(self,token_type):
		# compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
		if self.current_token.type==token_type:
			self.current_token=self.get_next_token()
		else:
			self.error()

	def baseCalc(self):
		
		self.eat(INTEGER)
        # we expect the current token to be a '+' token
		op = self.current_token
		if op.type==PLUS:
			self.eat(PLUS)
		if op.type==MINUS:
			self.eat(MINUS)
		if op.type==MULTI:
			self.eat(MULTI)
		if op.type==DIVISION:
			self.eat(DIVISION)	
        # we expect the current token to be a single-digit integer
		right = self.current_token
		self.eat(INTEGER)

        # after the above call the self.current_token is set to
        # EOF token
 
        # at this point either the INTEGER PLUS INTEGER or
        # the INTEGER MINUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding or subtracting two integers,
        # thus effectively interpreting client input
		if op.type==PLUS:
			result = self.left.value + right.value
		if op.type==MINUS:
			result = self.left.value - right.value
		if op.type==MULTI:
			result = self.left.value * right.value
		if op.type==DIVISION:
			result = self.left.value - right.value
		return result

	def expr(self):
		"""expr->INTEGER PLUS INTEGER"""
		# set current token to the first token taken from the input
		self.current_token = self.get_next_token()
        # we expect the current token to be a single-digit integer
		result=0
		while True:
			self.left=self.current_token
			if self.current_token==EOF:
				break
			else:
				result=self.baseCalc()
				print(result)
				self.current_token=Token(INTEGER,result)
		return  result		


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