# Token types
#
#EOF token is used to indicate that 
#there is no more input left for lexical analysis
INTEGER,PLUS,MINUS,EOF='INTEGER','PLUS','MINUS','EOF'

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
	def error(self):
		raise Exception('Error parsing input')
		#手工引发异常
	def deal_space(self):
		text=self.text
		self.text=text.replace(' ','')
	def get_next_token(self):
		"""Lexical analyzer(also known as scanner or tokenizer)
		This method is responsible for breaking a sentence 
		apart into tokens.One token at a time.
		"""
		self.deal_space()
		text=self.text

		if self.pos>len(text)-1:
			return Token(EOF,None)
		current_char=text[self.pos]
		digit=0
		if current_char.isdigit():
			current_digit=current_char

			while current_digit.isdigit():
		 		digit=digit*10+int(current_digit)
		 		self.pos+=1
		 		if self.pos<=len(text)-1:
		 			current_digit=text[self.pos]
		 		else:
		 			break
			token=Token(INTEGER,int(digit))
			return token
		if current_char=='+':
			token=Token(PLUS,current_char)
			self.pos+=1
			return token
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
	def expr(self):
		"""expr->INTEGER PLUS INTEGER"""
		# set current token to the first token taken from the input
		self.current_token = self.get_next_token()
        # we expect the current token to be a single-digit integer
		left=self.current_token
		self.eat(INTEGER)
        # we expect the current token to be a '+' token
		op = self.current_token
		self.eat(PLUS)
        # we expect the current token to be a single-digit integer
		right = self.current_token
		self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token
        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
		result = left.value + right.value
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