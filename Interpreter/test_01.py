import unittest
from practise import Lexer

class PractiseTestCase(unittest.TestCase):
	def test_get_next_token_lint(self):
		lexcer=Lexer("3+5")
		self.assertEquals("Token(INTEGER,3)",str(lexcer.get_next_token()))
	def test_get_next_token_op(self):
		lexcer=Lexer("3+5")
		lexcer.advance()
		self.assertEquals("Token(PLUS,'+')",str(lexcer.get_next_token()))
	def test_the_last_one(self):
		lexcer=Lexer("3+5")
		lexcer.advance()
		lexcer.advance()
		lexcer.advance()
		self.assertEquals("Token(EOF,None)",str(lexcer.get_next_token()))
if __name__=='__main__':
	unittest.main()