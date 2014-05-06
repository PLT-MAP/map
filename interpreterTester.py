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


if __name__ == "__main__": 
	unittest.main()





