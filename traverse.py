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
					  "Graph": [str],
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
		#print self.x
		self.f.write("")
		self.f.flush()
		#print draw_tree(tree)
		#return self.x

	def complete(self):
		return self.x

	def fill(self, text=""):
		'''Indent a piece of text, according to the current indentation level.'''
		lines = text.split('\n')
		#print lines
		#print self._indent
		s = ""
		for item in lines:
			s += "\t"*self._indent + item + "\n"
		return s

	def write(self, text):
		'''Append the text passed in to the current line.'''
		return text

	def enter(self):
		'''Create a new scope associated with the corresponding : and increase to
		the appropriate indentation.'''
		#print "entering enter"
		self.scope_depth += 1
		self.var_scopes.append([])
		self._indent += 1
		return ":\n"

	def leave(self):
		'''Decrease the indentation level and remove out-of-scope symbols.'''
		#self._indent -= 1
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
		self._indent -= 1

	def dispatch(self, tree, flag=None):
		'''Dispatcher function, dispatching tree type T to method _T.'''
		if isinstance(tree, list):
			for t in tree:
				self.dispatch(t, flag)
			return
		#print "calling dispatch for "
		#print tree
 		method = getattr(self,"_"+tree.type)

		x = method(tree, flag)
		return x

	def flatten(self, x):
		result = []
		for y in x:
			if hasattr(y, "__iter__") and not isinstance(y, basestring):
				result.extend(self.flatten(y))
			else:
				result.append(y)
		return result

# do we need external declaration stuff? translation unit? not in yacc but in our grammer

	def _print(self, tree, flag=None):
		return tree.name


	def _translation_unit(self, tree, flag=None):
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		else:
			x = self.dispatch(tree.children[0], flag)
			y = self.dispatch(tree.children[1], flag)
			return x + "\n\n" + y


	def _external_declaration(self, tree, flag=None):
		return self.dispatch(tree.children[0], flag)


	# function definition
	def _funcdef(self, tree, flag=None):
		fname = tree.name
		s = "def " + tree.name + "("
		if len(tree.children) == 2:
			params = self.dispatch(tree.children[0], flag)
			self.fargs[fname] = self.get_param_types(params, tree.children[0])
			for (param, param_type) in zip(params, self.fargs[fname]):
				self.symbols[param] = param_type
				self.var_scopes[self.scope_depth].append(param)
			comma = False
			for a in params:
				if comma:
					s += ","
				else:
					comma = True
				s += a
				self.waitingfor.add(a)
			s += ")" + self.enter()
			r = self.dispatch(tree.children[1], flag)
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
			s += ")" + self.enter()
			self.fill("pass")
			self.leave()
		return s

	def _funcexp(self,tree,flag=None):
		if self.symbols.get(flag) == "MAP":
			if tree.name == "add":
				return self.add_method(tree,flag)
			else:
				return flag + "." + self.flist[tree.name] + "()"
		elif flag:
			if self.symbols.get(flag) in self.class_meths:
				class_methods = self.class_meths[self.symbols.get(flag)]
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
                    #print s
                    return s
		elif tree.name in self.flist:
			if tree.name in self.flistsymbol:
				if not self.symbols.get(flag) == self.flistsymbol[tree.name]:
					raise Exception(tree.name + " method called on a non " + self.flistsymbol[tree.leaf] + " type")
			return flag + "." + self.flist[tree.name] + "()"
		else:
			if tree.name not in self.fargs:
				raise Exception("Function %s is not user-defined nor is it part of the MAP library"
                    % (tree.name))
			if len(tree.children)==1:
				params = self.dispatch(tree.children[0],flag)
                if tree.name in self.fargs:
                    typed_params = [self.num_or_str(param) for param in params]
                    init_args = [self.get_type(param) for param in typed_params]
                    #print tree.name, init_args, params, self.symbols
                    if self.fargs[tree.name] != "every" and init_args != self.fargs[tree.leaf]:
                        raise Exception("Function Type Check Error for %s, expected %s but got %s"
                            % (tree.name, str(self.fargs[tree.leaf]), str(init_args)))
                        s = self.listtoparams(params)
                    else:
            			s = ""
				return tree.name + "(" + s + ")"

	def _param_list(self, tree, flag=None):
		if len(tree.children) == 0:
			#
			#return tree.name
			return ""
		if len(tree.children) == 1:
 			return [self.dispatch(tree.children[0], flag)]
		else:
			x = self.dispatch(tree.children[0], flag)
			y = self.dispatch(tree.children[1], flag)
			z = [x] + [y]
			return self.flatten(z)

	def _typedec(self, tree, flag=None):
		if tree.name == 'Node':
			x = self.dispatch(tree.children[0], flag) 
			y = "nx.add_node(" + x + ")"
			return y
		elif tree.name == 'Graph':
			x = self.dispatch(tree.children[0], flag) + " = nx.MultiDiGraph()"
			return x
		else:
			return self.dispatch(tree.children[0], flag)


	def _statement_list(self, tree, flag=None):
		if len(tree.children) == 0:
			return ""
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		else:
			return self.dispatch(tree.children[0], flag) + "\n" + self.dispatch(tree.children[1], flag)

	def _statement(self, tree, flag=None):
		return self.dispatch(tree.children[0], flag)

	def _expr(self, tree, flag=None):
		return self.dispatch(tree.children[0], flag)

	# identifier
	def _id(self, tree, flag=None):
		s = tree.name
		return s

	def _primary_expression(self, tree, flag=None):
		if not tree.name:
			x = self.dispatch(tree.children[0], flag)
			return x
		else:
			return str(tree.name)

	def _assignment_expression(self, tree, flag=None):
		if not tree.name:
			return self.dispatch(tree.children[0], flag)
		elif tree.name == "aexpr":
			x = self.dispatch(tree.children[0], flag)
			return x + " = " + tree.children[1]
		else:
			x = self.dispatch(tree.children[0], flag)
			y = self.dispatch(tree.children[1], flag)
			return x + " = " + y

	def _struct_assignment(self, tree, flag=None):
		# if tree.name == "new":
		if tree.children[0] == tree.children[2]:
			# types are the same
			if tree.children[0] == "Graph":
				x = self.dispatch(tree.children[1], flag)
				return x + " = nx.MultiDiGraph()"
			elif tree.children[0] == 'DirEdge':
				# x = self.dispatch(tree.children[1], flag) 
				# y = self.dispatch(tree.children[3], flag)
				return self.dispatch(tree.children[1]) + "=" + tree.children[2] + '(' + self.dispatch(tree.children[3]) + ')'
			elif tree.children[0] == 'UnDirEdge':
				print "hi"
			elif tree.children[0] == "Node":
				if len(tree.children) == 3:
					x = self.dispatch(tree.children[1], flag) 
					return x + " = " + "'" + x + "'"
				elif len(tree.children) == 4:
					x = self.dispatch(tree.children[1], flag)
					y = self.dispatch(tree.children[3], flag)
					return x + " = " + "'" + x + "'" + y 
		else:
			# we need to throw a type mismatch error
			return "type mismatch"

	def _associative_arr(self, tree, flag=None):
 		return " {" + self.dispatch(tree.children[0], flag) + "}"

	def _array_values(self, tree, flag=None):
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		elif len(tree.children) == 2:
			return self.dispatch(tree.children[0], flag) + "," + self.dispatch(tree.children[1], flag)

	def _arrayval(self, tree, flag=None):
		return tree.children[0] + ":" + self.dispatch(tree.children[1], flag)

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
		if params is not None:
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
				return return_val

	def _conditional_expression(self, tree, flag= None):
		#if tree.name:
		return self.dispatch(tree.children[0], flag)

	# logical expressions
	def _logical_or_expr(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + " or " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

	def _logical_and_expr(self, tree, flag=None):
		if tree.name:
			s = self.dispatch(tree.children[0], flag) + " and " + self.dispatch(tree.children[1], flag)
			return s
		return self.dispatch(tree.children[0], flag)

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
			s = "(" + self.dispatch(tree.children[0], flag) + tree.name + self.dispatch(tree.children[1], flag) + ")"
			return s
		return self.dispatch(tree.children[0], flag)

	def _selection_statement(self, tree, flag=None):
		x = self.dispatch(tree.children[0], flag)
		s = tree.name + " (" + x + ")" 
		s += self.enter()
		r = self.dispatch(tree.children[1], flag)
		s += self.fill(r) 
		self.leave()
		q = self.dispatch(tree.children[2], flag)
		s += self.fill(q)
		p = self.dispatch(tree.children[3], flag)
		s += self.fill(p)
		return s

	def _sel_statement(self, tree, flag=None):
		if len(tree.children) == 2:
			return self.dispatch(tree.children[0], flag) + self.dispatch(tree.children[1], flag)
		else:
			return ''

	def _else_statement(self, tree, flag=None):
		if len(tree.children) == 1:
			s = tree.name
			s += self.enter() + self.dispatch(tree.children[0], flag)
			self.leave()
			return s
		else:
			return ''

	def _elif_statement(self, tree, flag=None):
		if len(tree.children) == 2:
			x = self.dispatch(tree.children[0], flag) 
			s = tree.name + " (" + x + ")" 
			s += self.enter()
			y = self.dispatch(tree.children[1], flag)
			s += self.fill(y)
			self.leave()
			return s
		else:
			return ''

	def _for_loop(self, tree, flag=None):
		x = self.dispatch(tree.children[0], flag)
		y = self.dispatch(tree.children[1], flag)
		z = self.dispatch(tree.children[2], flag)
		self.enter()
		if x[4].isdigit():
			ini = str(int(float(x[4:])))
		else:
			ini = x[4:]
		if y[2] == "=":
			if y[3].isdigit():
				end = str(int(float(y[3:]))) + "+1"
			else: 
				end = y[3:] + "+1"
		else:
			if y[2].isdigit():
				end = str(int(float(y[2:])))
			else:
				end = y[2:]
		if z == "i = i+1.0":
			s = tree.name + " " + x[0] + " in range(" + ini + ",int(" + end + ")):\n"
		elif z[5] == "+":
			step = str(int(float(z[6:])))
			s = tree.name + " " + x[0] + " in range(" + ini + ", int(" + end + "), " + step + "):\n"
		else:
			step = str(int(float(z[6:])))
			s = tree.name + " " + x[0] + " in range(" + ini + ", " + end + ", -" + step + "):\n"
		r = self.dispatch(tree.children[3], flag)
		s += self.fill(r)
		self.leave()
		return s

	def _for_each(self, tree, flag=None):
		x = self.dispatch(tree.children[1], flag)
		y = self.dispatch(tree.children[2], flag)
		z = self.dispatch(tree.children[3], flag)
		s = "for " + x + " in " + y + ":\n" + z
		return s

	def _jump_stmt(self, tree, flag=None):
		line=""
		if tree.name== 'break':
			line=tree.name
		elif tree.name == 'continue':
			line=tree.name
		elif tree.name == 'return':
			 line=tree.name + " " + self.dispatch(tree.children[0], flag)
		return line


	# function call
	def _function_call(self, tree, flag=None):
		functions = {'add' : 'add_node', 'delete': 'remove_node', 'addEdge': 'add_edge', 'deleteEdge':'remove_edge' }
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		elif len(tree.children) == 2:
			return self.dispatch(tree.children[0], flag) + "(" + self.dispatch(tree.children[1], flag) + ")"
		# hack solution below must fix. 
		# seriously
		elif len(tree.children) == 3:
			x = self.dispatch(tree.children[1], flag)
			for child in tree.children[2].children:
				print child
			if x == "add":
				return self.dispatch(tree.children[0], flag) + "." + functions[x] + "(" + tree.children[2].name + "[0], " + tree.children[2].name + "[1]" + ")"
			elif x == "delete":
				return self.dispatch(tree.children[0], flag) + "." + functions[x] + "(" + tree.children[2].name + "[0])"
		else:
			#print "need to deal with functions with this many parameters"
			return self.dispatch(tree.children[0], flag)

	def _func_args(self, tree, flag=None):
		if len(tree.children) == 1:
			return self.dispatch(tree.children[0], flag)
		elif len(tree.children) == 2:
			return self.dispatch(tree.children[0], flag) + ', ' + self.dispatch(tree.children[1], flag)

	def _arg(self, tree, flag=None):
		if len(tree.children) == 0:
			return tree.name
		else:
			return self.dispatch(tree.children[0], flag)


	def _function_name(self, tree, flag=None):
		return tree.name

l = MAPlex()
#m = MAPparser(l,"func main(Text hi, Numeric bye) { Graph n = new Graph(); hi = 'hello'; bye = 3-4; bye = 3*4+6-(5/4); print(hi); if (5 < 7) { bye = 0; } Node no2 = new Node({'temp':45});}")


#m = MAPparser(l,
#	'''func main() { 
#		Text hi = 'hello'; 
#		Graph n = new Graph(); 
#		Node no2 = new Node({'temp':45, 'cost':300, 'weight':200, 'lol':200});
#		}
#	''')

#
test1= '''func main(){ 
	if (10 < 7) { 
		cost = 2; 
	} 
	elif (5 == 7) { 
		print('yay'); 
	} 
	elif (7 == 7) { 
		print('even more yay'); 
	} 
	else { 
		print('success'); 
	}
}'''

#m = MAPparser(l,"func main() { if (5 < 7) { cost = 5; } }")

test2= '''
	func main() {
		foreach (Node n in graph) { 
		if (10 < 7){ 
			cost = 2; 
		} 
		elif (5 == 7) { 
			break; 
		} elif (7 == 7) { 
			continue; 
		} else { 
			print('success'); 
		}
		Text n = 'hi world';
		print(n);
		}
	}'''

test3= '''
	func main(){
		Graph g = new Graph();
		Node losangeles = new Node({'temp':90, 'weather': 'cloudy with a chance'});
		g.add(no2);
		g.delete(no2); 
	}
'''

test4= '''

func factorial(Numeric n) {
	if (Numeric n == 0) {
		return 1;
	}
	Numeric x=1;
	for (Numeric i = 1; i <= n; i = i + 1) {
		 x = x * i;
	}
	return x;
}

func main() {
	Numeric fact = factorial(5);
	print(fact);
}
'''

test5= '''
	func main() {
		for (Numeric i = 0; i < 10; i = i+1) {
			print(i);
		}
		return i;
	}
'''

test6= '''
func main(){
        Graph g= new Graph();
        Node nj= new Node();
        Node ny= new Node();
        Node pa= new Node({'temp':85,'humidity':'low'});
        Node va= new Node({'temp':87,'humidity':'high'});
}
'''

test7= '''
func main(){
        Graph g=new Graph();
        Node nj=new Node();
        Node ny=new Node();
        Node pa= new Node({'temp':85,'humidity':'low'});
        Node va= new Node({'temp':87,'humidity':'high'});
        g.add(nj);
        g.add(ny);
        g.add(pa,va);
        DirEdge e = new DirEdge(no1,no2,{'cost':100});
}
'''

test8='''
func main(){
        Graph g = new Graph();
        Node no2 = new Node( {'temp':90, 'weather': 'cloudy with a chance'});
        g.add(no2, no1,no3);
        g.delete(no2);

}
'''

test9='''
func fact(Numeric hi){
	
}
func main(){
	Numeric hi= 5;
	fact(hi);
}
'''

m = MAPparser(l, test8)

def main():
	#print draw_tree(m.ast)
	t = Traverse(m.ast)
	print(t.complete())

if __name__ == "__main__":
	main()
