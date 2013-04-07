import sys
import os.path

def parsepdb(path):
	fileisNotOK=True
	while  fileisNotOK:
		if os.path.exists(path) and os.path.isfile(path):
			print "The file",path,"has been successfully loaded"
			fileisNotOK=False
			f = open(path, "r")
			lines = f.readlines()
			for line in path:
    				if len(lines) < 80:
					print "The file",path,"does not follow the PDB format"
					return
			#print "ok"
		else:
			print "ERROR: The file doesn't exist"
			path=raw_input("Path of the file: ")
