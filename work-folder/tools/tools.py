from os import system, mkdir, listdir
from config import sites, cache_init
from urllib.parse import urlparse
from time import time
from root import root
import re, sys, json

site = {}
cache = cache_init

# copy new templates to code
def copyTemplates():
	system(f"cp {root}/templates/* {root}/work-folder/code")

# start parsing site for new directory
def startParser(link, directory):
	print("Starting Parser...")
	parser = site["parser"](site["full_prefix"], link, directory)
	parser.feed()
	parser.process()
	print("Parsing Finished!\n")

# get problem name from link for directory
def getProblemName(link):
	path=urlparse(link).path
	problem_match = re.match(site["problem_re"],path)
	if problem_match==None: 
		print("Problem regex failed match")
		return None
	problem=problem_match.group(1)
	return problem

# save to cache
def saveCache():
	f=open(f"{root}/work-folder/cache.json",'w')
	f.write(json.dumps(cache, indent=4))
	f.close()

# load from cache
def loadCache():
	try:
		f=open(f"{root}/work-folder/cache.json",'r')
		cache = json.loads(f.read())
		f.close()
	except: saveCache()

# open directory and copy data
def open_dir(link):
	cache["link"] = link
	problem = getProblemName(link)
	directory = getDirectories(problem)
	cache["current_directory"] = directory
	system(f'cp -r "{site["pwd"]}/{directory}/data/" {root}/work-folder/data')
	system(f'cp -r "{site["pwd"]}/{directory}/code/" {root}/work-folder/code')

# get list of possible directories
def getDirectories(problem):
	dirs=[]
	for solution in listdir(site["pwd"]):
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

# make new directory
def makeDirectory(problem):
	directory = site["pwd"]+"/"+problem
	""" no multiple directory support for now
	try: mkdir(directory)
	except:
		ans = input("Directory Exists! Make Another? (Y to confirm): ")
		if ans!="Y": exit()
		directory += f"-({int(time())})"
		mkdir(directory)"""
	mkdir(directory)
	mkdir(directory+"/data")
	mkdir(directory+"/code")
	cache["current_directory"] = directory
	return directory

# make new problen
def new(link):

	global site

	print()
	cache["link"] = link
	print("Retrieving Problem Data")

	domain = urlparse(link).netloc
	if domain in sites:
		site = sites[domain]
		try: 
			problem = getProblemName(link)
			directory = makeDirectory(problem)
			startParser(link, directory)
			open_dir(link)

		except: 
			print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
			try: system(f'rm -rf {directory}')
			except: pass
	else: print("no such domain")
	
	print()

# save solution to database
def saveSolution(fname=None, ext="py"):
	directory=load("current_directory")
	if fname==None: fname=int(time.time())
	target = f"{directory}/{fname}.{ext}"
	try: open(target)
	except FileNotFoundError: 
		os.system(f'cp "code/code.{ext}" "{target}"')

if __name__ == "__main__":

	try: link = sys.argv[1]
	except: exit("python3 new.py [link]")

	new(link)