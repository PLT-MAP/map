import sys

class Traverse(object):
	
	def __init__(self, tree, file=sys.stdout):
		self.f = file
		
		# used for scope checking
		self.var_scopes = [[]]
		self.scope_depth = 0
		

		self.relops = {'<','>','<=','>=','==','!=','+','-','*','/','%'}
		self.future_imports = []
		self.tempPoints = set()

		# type table for variables
		self.symbols = {}
		self.values = {}
		self._indent = 0
		self.x = self.dispatch(tree)
		self.f.write("")
		self.f.flush()



	def fill(self, text=""):
		'''Indent a piece of text, according to the current indentation level.'''
		self.f.write("\n" + "    "*self._indent + text)

	def write(self, text):
		'''Append the text passed in to the current line.'''
		self.f.write(text)

	def enter(self):
		'''Create a new scope associated with the corresponding : and increase to
		the appropriate indentation.'''
		self.scope_depth += 1
		self.var_scopes.append([])
		self._indent += 1
		self.f.write(":")

	def leave(self):
		'''Decrease the indentation level and remove out-of-scope symbols.'''
		self._indent -= 1
		for var in self.var_scopes[self.scope_depth]:
			del self.symbols[var]
			if (var + str(self.scope_depth)) in self.symbols:
				self.symbols[var] = self.symbols[var + str(self.scope_depth)]
				del self.symbols[var + str(self.scope_depth)]
			if var in self.values:
				del self.values[var]
				if (var + str(self.scope_depth)) in self.values:
					self.values[var] = self.values[var + str(self.scope_depth)]
					del self.values[var + str(self.scope_depth)]
		del self.var_scopes[self.scope_depth]
		self.scope_depth -= 1
		self.indent -= 1

	def dispatch(self, tree, flag=None):
		'''Dispatcher function, dispatching tree type T to method _T.'''
		if isinstance(tree, list):
			for t in tree:
				self.dispatch(t, flag)
			return
		meth = getattr(self, "_"+tree.type)
		x = meth(tree, flag)
		return x

# do we need external declaration stuff? translation unit? not in yacc but in our grammer

	# function definition
	def _fd(self, tree, flag=None):
		

	# identifier
	def _id(self, tree, flag=None):



# maybe use
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

	# logical expressions
	def _logorexpr(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + " or " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _logandexpr(self, tree flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + " and " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag):

	# equality expression
	def _eqexpr(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# relational expression
	def _relexpr(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# additive expression
	def _addexpr(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# multiplicative expression
	def _multexpr(self, tree, flag=None):
		if tree.leaf:
			s = self.dispatch(tree.children[0], flag) + tree.leaf + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag) 

	# primary expression
	def _primexp(self, tree, flag=None):


	# primary expression term
	def _primexp_term(self, tree, flag=None):


	# function call
	def _funcall(self, tree, flag=None): #params here?



