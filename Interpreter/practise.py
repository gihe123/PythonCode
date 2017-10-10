INTEGER,PLUS,MINUS,EOF='INTEGER','PLUS','MINUS','EOF'
class Token(object):
	def __init__(self, type,value):
		super(Token, self).__init__()
		self.type = type
		self.value=value
	def __str__():
		return'Token({type},{value})'.format(
			type=self.type
			value=self.value
			)
class interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos=0
	def error(self):
		raise Exception("Wrong input")
	##############
	#lexer       #
	##############
	def go_next_token(self):
		#获得下一个标记
		self.pos+=1
		if self.pos>len(self.text)-1:
			return Token(EOF,None)
		return self.text[self.pos]
	def multi_integer(self):
		result=''
		while self.current_token.type is not None and self.current_token.isdigist():



	##############
	#parser      #
	##############
		
	def term():

	def rpre():
		self.current_token=self.go_next_token()


		
def main():
	text=input("calc_LL>")
	result=interpreter(text)
	print(result)
if __name__=="__main__":
	main()