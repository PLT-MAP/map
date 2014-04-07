import sys

class Traverse(object):
	
	def __init__(self, tree, file=sys.stdout):
		self.f = file
		
		self.relops = {'<','>','<=','>=','==','!=','+','-','*','/','%'}
	





	def write(self, text):
		'''Append the text passed in to the current line.'''
		self.f.write(text)

	def enter(self):
		'''Create a new scope associated with the corresponding : and appropriate indentation.'''


