from os import system, mkdir, listdir
from config import site, pwd
from urllib.parse import urlparse
from time import time
from parser import HackerRankParser
import re
import sys

def copyTemplates():
	system("cp ../../templates/* data")

def startParser(link, directory):
	print("Starting Parser...")
	parser = HackerRankParser(site["full_prefix"], link, directory)
	parser.feed()
	parser.process()
	print("Parsing Finished!\n")

def getProblemName(link):
	path=urlparse(link).path
	problem_match = re.match(site["problem_re"],path)
	if problem_match==None: 
		raise ValueError("Problem regex failed match")
	problem=problem_match.group(1)
	return problem

def save(data,fname):
	f=open(f"data/{fname}.txt",'w')
	f.write(data)
	f.close()

def open_dir(link):
	save(link, "link")
	problem = getProblemName(link)
	directory = getDirectories(problem)
	save(directory, "current_directory")

def getDirectories(problem):
	dirs=[]
	for solution in listdir(pwd):
		if solution.startswith(problem):
			dirs.append(solution)
	n = len(dirs)
	if n==0: return None
	if n==1: return dirs[0]

	for d in range(n): 
		print(f"{d}: {dirs[d]}")
	print()
	choice = -1
	while choice not in range(n): 
		try: choice = int(input("Choose Directory: "))
		except: pass
	return dirs[choice]

def makeDirectory(problem):
	directory = pwd+"/"+problem
	try: mkdir(directory)
	except:
		ans = input("Directory Exists! Make Another? (Y to confirm): ")
		if ans!="Y": exit()
		directory += f"-({int(time())})"
		mkdir(directory)
	mkdir(directory+"/data")
	save(directory, "current_directory")
	return directory

def main(link):

	print()
	save(link, "link")
	print("Retrieving Problem Data")

	try: 
		problem = getProblemName(link)
		directory = makeDirectory(problem)
		startParser(link, directory)

	except ValueError as err:
		print("ERROR:",err)
		exit()
	
	print()

if __name__ == "__main__":

	try: link = sys.argv[1]
	except: exit("python3 new.py [link]")

	main(link)