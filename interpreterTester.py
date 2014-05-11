import unittest
import sys
import os

class TestInterpreterSyntax(unittest.TestCase):
	def assert_prog(self, testname, outname):
		t=open(testname,'r')
		o=open(outname,'r')
		teststr=t.read()
		outstr=o.read()
		self.assertEqual(teststr,outstr)
	
	def testhelloworld(self):
		os.system("python Map.py test/helloworld.map")
		self.assert_prog("test/helloworld.py","test/helloworld.out")

	def testfactorial(self):
		os.system("python Map.py test/factorial.map")
		self.assert_prog("test/factorial.py","test/factorial.out")
	
	def testforeach(self):
		os.system("python Map.py test/foreachtest.map")
		self.assert_prog("test/foreachtest.py","test/foreachtest.out")
	
	def testforstatement(self):
		os.system("python Map.py test/forstatementtest.map")
		self.assert_prog("test/forstatementtest.py","test/forstatementtest.out")
	
	def testifelifelse(self):
		os.system("python Map.py test/ifelifelsetest.map")
		self.assert_prog("test/ifelifelsetest.py","test/ifelifelsetest.out")
	def testifelse(self):
		os.system("python Map.py test/ifelsetest.map")
		self.assert_prog("test/ifelsetest.py","test/ifelsetest.out")

	def testif(self):
		os.system("python Map.py test/iftest.map")
		self.assert_prog("test/iftest.py","test/iftest.out")
	def testnode(self):
		os.system("python Map.py test/nodetest.map")
		self.assert_prog("test/nodetest.py","test/nodetest.out")
	def testsample1(self):
		os.system("python Map.py test/sample1.map")
		self.assert_prog("test/sample1.out","test/sample1.py")
	def testincludeinput(self):
		os.system("python Map.py test/testincludeinput.map")
		self.assert_prog("test/testincludeinput.out","test/testincludeinput.py")
	def testpathtest(self):
		os.system("python Map.py test/pathtest.map")
		self.assert_prog("test/pathtest.py","test/pathtest.out")

if __name__ == "__main__": 
	unittest.main()
