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

	def listtoparams(self, l, x=None):
		s = ""
		comma = False
		for a in l:
			if comma:
				s += ","
			else:
				comma = True
			s += a
			if x:
				self.waitingfor.add(a)
		return s

	def _logical_OR_expression(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + " or " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _logical_AND_expression(self, tree flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + " and " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag):

	def _equality_expression(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _relational_expression(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _additive_expression(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _multiplicative_expression(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag) 

	
