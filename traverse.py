from MAPlexer import *
from yacc import *
import sys
from asciitree import *

class Traverse(object):
	
	def __init__(self, tree, file=sys.stdout):
		self.f = file
		
		#self.flist = {"Edge": "Edge",
		#			  "Text": "Text"}
		self.fargs = {"Edge": [str], 
					  "Node": [str],
					  "Text": "every",
					  "Path": [str],
					  "Numeric": "every",
					  "List": "every",
					  "None": "every"}
		self.class_meths = {"LIST": {
								'append': "every",
								'get': [int],
								'delete': [int]
								}
							}
		self.class_meth_impls = {"LIST": {
				'append': (lambda name, params : '%s.append(%s)' % (name, params)),
				'get': (lambda name, params : '%s[%s]' % (name, params)),
				'delete': (lambda name, params : 'del %s[%s]' % (name, params))
				}
			}
		
		# used for scope checking
		self.var_scopes = [[]]
		self.scope_depth = 0
		

		self.relops = {'<','>','<=','>=','==','!=','+','-','*','/','%'}
		self.future_imports = []
		self.tempPoints = set()

		# type table for variables
		self.symbols = {}
		self.values = {}
		self.waitingfor = set()
		self._indent = 0
		self.x = self.dispatch(tree)
		self.f.write("")
		self.f.flush()
		print draw_tree(tree)


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
		print "dispatch type: ", tree.type
		print tree
		#try:
		method = getattr(self,"_"+tree.type)
		x = method(tree, flag)
		return x
		#except AttributeError:
		#print "failed tree:{0} flag:{1}".format(tree,flag)
		#return
		#else:
		#print "not attribute error"
		#return 

	def flatten(self, x):
		result = []
		for y in x:
			if hasattr(y, "__iter__") and not isinstance(y, basestring):
				result.extend(self.flatten(y))
			else:
				result.append(y)
		return result

# do we need external declaration stuff? translation unit? not in yacc but in our grammer

	# function definition
	def _funcdef(self, tree, flag=None):
		print "got here"
		print "tree", tree
		fname = tree.name
		print "fname: ", fname
		s = "def ",tree.name,"("
		if len(tree.children) == 2:
			self.enter()
			params = self.dispatch(tree.children[0], flag)
			print "params: ", params

			# gets stuck here, we need to figure out why
			print self.fargs
			print fname
			self.fargs[fname] = self.get_param_types(params, tree.children[1])
			print self.fargs[fname]
			# from here on doesn't print
			print "get param types of child 1"
			print self.fargs
			for (param, param_type) in zip(params, self.fargs[fname]):
				print (param, param_type)
				self.symbols[param] = param_type
				self.var_scopes[self.scope_depth].append(param)
			comma = False
			print "got here"
			for a in params:
				if comma:
					s += ","
				else:
					comma = True
				s += a
				print "a: ", a
				self.waitingfor.add(a)
			s = s + "):\n"
			print "first kid: ", tree.children[1]
			r = self.dispatch(tree.children[1], flag)
			r += "\npass"
			s += self.fill(r)
			self.leave()
		else:
			p = self.dispatch(tree.children[0], flag)
			comma = False
			for a in p:
				if comma:
					s += ","
				else:
					comma = True
				s += a
				self.waitingfor.add(a)
			s = s + "):\n"
			self.enter()
			self.fill("pass")
		return s

	def _funcexp(self,tree,flag=None):
		print "fsadhs"
		if self.symbols.get(flag) == "MAP":
			if tree.name == "add":
				return self.add_method(tree,flag)
			else:
				return flag + "." + self.flist[tree.name] + "()"
		elif flag:
			if self.symbols.get(flag) in self.class_meths:
				class_methods = self.class_meths[self.symbols.get(flag)]
				print tree.name
                if tree.name in class_methods:
                    params = self.dispatch(tree.children[0],flag)
                    typed_params = [self.num_or_str(param) for param in params]
                    init_args = [self.get_type(param) for param in typed_params]
                    if class_methods[tree.name] != "every":
                        for (e_p, p) in zip(class_methods[tree.name], init_args):
                            if e_p != "all" and e_p != p:
                                raise Exception("Class Method %s of %s excepted %s but got %s"
                                    % (tree.name, flag, class_methods[tree.leaf], init_args))

                    s = self.listtoparams(params)
                    s = self.class_meth_impls[self.symbols.get(flag)][tree.name](flag, s)
                    print s
                    return s
		elif tree.name in self.flist:
			if tree.name in self.flistsymbol:
				if not self.symbols.get(flag) == self.flistsymbol[tree.name]:
					raise Exception(tree.name + " method called on a non " + self.flistsymbol[tree.leaf] + " type")
			return flag + "." + self.flist[tree.name] + "()"
		else:
			if tree.name not in self.fargs:
				raise Exception("Function %s is not user-defined nor is it part of the MineTime library"
                    % (tree.name))
			if len(tree.children)==1:
				params = self.dispatch(tree.children[0],flag)
                if tree.name in self.fargs:
                    typed_params = [self.num_or_str(param) for param in params]
                    init_args = [self.get_type(param) for param in typed_params]
                    print tree.name, init_args, params, self.symbols
                    if self.fargs[tree.name] != "every" and init_args != self.fargs[tree.leaf]:
                        raise Exception("Function Type Check Error for %s, expected %s but got %s" 
                            % (tree.name, str(self.fargs[tree.leaf]), str(init_args)))
                        s = self.listtoparams(params)
                    else:
            			s = ""
				return tree.name + "(" + s + ")"

	def _param_list(self, tree, flag=None):
		if len(tree.children) == 0:
			return ""
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		else:
			x = self.dispatch(tree.children[0], flag)
			y = self.dispatch(tree.children[1], flag)
			z = [x] + [y]
			return self.flatten(z)

	def _typedec(self, tree, flag=None):
		print "hey sandya"
		return self.dispatch(tree.children[0], flag)

	
	def _statement_list(self, tree, flag=None):
		print "hey alf"
		if len(tree.children) == 0:
			print "no kids"
			return ""
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		else:
			return self.dispatch(tree.children[0], flag) + "\n" + self.dispatch(tree.children[1], flag)

	def _statement(self, tree, flag=None):
		print "hey serena"
		return self.dispatch(tree.children[0], flag)

	def _expr(self, tree, flag=None):
		print "hey expression"
		return self.dispatch(tree.children[0], flag)

	# identifier
	def _id(self, tree, flag=None):
		print "hey identifier"
		s = tree.name
		print s
		return s

	def _primary_expression(self, tree, flag=None):
		print "hey primary expression"
		return self.dispatch(tree.children[0], flag)

	def _assignment_expression(self, tree, flag=None):
		print "hey assignment expression"
		return self.dispatch(tree.children[0], flag)

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

	def get_param_types(self, params, tree):
		typed_params = []
		for param in params:
			typed_params.append(self.get_param_type(param, tree))
		return typed_params

	def get_param_type(self, param, tree):
		if tree.name == param:
			if tree.type == "class_method_expression":
				for obj in self.class_meths:
					if tree.children[0].name in self.class_meths[obj]:
						return obj
			else:
				return True
		for child in tree.children:
			return_val = self.get_param_type(param, child)
			if return_val:
				if tree.name in self.relops:
					params = self.dispatch(tree.children[0])
					return int
				if tree.name in self.fargs:
					params = self.dispatch(tree.children[0])
					print params
				return return_val

'''
	# logical expressions
	def _logical_or_expr(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + " or " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _logical_and_expr(self, tree flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + " and " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag):

	# equality expression
	def _equality_expression(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + tree.name + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# relational expression
	def _relational_expression(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + tree.name + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# additive expression
	def _additive_expression(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + tree.name + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	# multiplicative expression
	def _multiplicative_expression(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + tree.name + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag) 

	# primary expression
	def _primary_expression(self, tree, flag=None):


	# function call
	def _function_call(self, tree, flag=None): #params here?

	def _func_args():

	def _arg():

	def _function_name():


'''
l = MAPlex()
m = MAPparser(l,"func main(Text hi, Numeric bye){hi = 4;}")
def main():
	t = Traverse(m.ast)
	t.enter()

if __name__ == "__main__":
	main()
