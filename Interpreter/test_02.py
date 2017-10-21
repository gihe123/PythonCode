import unittest
from practise import Interpreter
from practise import Lexer
class PractiseTestCase(unittest.TestCase):
	def test_expr(self):
		lexcer=Lexer("3+5")
		inter=Interpreter(lexcer)
		self.assertEquals("8",str(inter.expr()))
	def test_factor(self):
		lexcer=Lexer("3")
		inter=Interpreter(lexcer)
		self.assertEquals("3",str(inter.factor()))

if __name__=='__main__':
	unittest.main()