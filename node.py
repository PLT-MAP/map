class Expr : pass

class Node(Expr):
	def __init__(self,name='',t='',children=None,token=None):
		self.type = t

		if children:
			self.children = children
		else:
			self.children = []
			
		self.token = token
		self.name = name
	

	def addChild(self,c):
		self.children.append(c)

	def __str__(self):
		return "name:{0}  type:{1}".format(self.name,self.type)


