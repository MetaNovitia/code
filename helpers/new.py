from os import system, mkdir
from config import sites, pwd
from urllib.parse import urlparse
from time import time
import re

def startParser(site, link, directory):
	print("Starting Parser...")
	parser = site["parser"](site["full_prefix"], link, directory)
	parser.feed()
	parser.process()
	print("Parsing Finished!\n")

def copyTemplates():
	system("cp templates/* data")

def getProblemName(site, path):
	problem_match = re.match(site["problem_re"],path)
	if problem_match==None: 
		raise ValueError("Problem regex failed match")
	problem=problem_match.group(1)
	return problem

def makeDirectory(site, problem):
	directory = pwd+site["name"]+"/"+problem
	try: mkdir(pwd+site["name"])
	except: pass
	try: mkdir(directory)
	except:
		ans = input("Directory Exists! Make Another? (Y to confirm): ")
		if ans!="Y": exit()
		directory = pwd+site["name"]+"/"+problem+"-("+str(int(time()))+")"
		mkdir(directory)
	
	f=open("data/current_directory.txt",'w')
	f.write(directory)
	f.close()

	return directory

def main():

	print()

	f = open("data/link")
	link = f.read().strip()
	f.close()

	print("Retrieving Problem Data")

	try: 
		domain = urlparse(link).netloc
		path = urlparse(link).path

		if domain in sites:

			site = sites[domain]
			problem = getProblemName(site, path)
			# directory = makeDirectory(site, problem)
			# startParser(site, link, directory)
			copyTemplates()

	except ValueError as err:
		print("ERROR:",err)
		exit()
	
	print()

if __name__ == "__main__":
	main()