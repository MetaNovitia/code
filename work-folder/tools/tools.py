from os import system, mkdir, listdir, strerror
from config import sites, cache_init, root, view_prompt, view_prompt_ans
from urllib.parse import urlparse
from time import time
import re, sys, json, errno, driver, webbrowser
from checker_helper import cpp_checker, py_checker

site = {}
cache = cache_init

# copy new templates to code
def copyTemplates():
	system(f"rm -rf {root}/work-folder/code/*")
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
	global cache, site
	try:
		f=open(f"{root}/work-folder/cache.json",'r')
		cache = json.loads(f.read())
		site = sites[cache["domain"]]
		f.close()
	except: saveCache()

# open directory and copy data
def open_dir(link):
	if checkLink(link):
		system(f'rm -r {root}/work-folder/data/*')
		system(f'rm -r {root}/work-folder/code/*')
		system(f'cp -r "{cache["directory"]}/data/" {root}/work-folder/data')
		system(f'cp -r "{cache["directory"]}/code/" {root}/work-folder/code')
		copyTemplates()

def vim(ext=None):
	fname = f"code.{ext}"
	if ext==None:
		choice=-1
		code_dir = f"{root}/work-folder/code"
		files = listdir(code_dir)
		n = len(files)
		prompt = "\n".join([f"{i} {files[i]}" for i in range(n)])
		print(prompt)
		while choice not in range(n):
			try: choice = int(input("Choice: "))
			except: choice = -1
		fname = files[choice]

	system(f'bash {root}/work-folder/tools/vim.sh {root}/work-folder/code/{fname}')

# get list of possible files/directories
def choose(directory,re_string=".*"):
	dirs=[]
	for solution in listdir(directory):
		if re.match(re_string, solution):
			dirs.append(solution)
	n = len(dirs)
	if n==0: raise FileNotFoundError(errno.ENOENT, strerror(errno.ENOENT), directory)

	for d in range(n): print(f"{d}: {dirs[d]}")
	print()
	choice = -1
	while choice not in range(n): 
		try: choice = int(input("Choose Directory/File: "))
		except: choice = -1
	return directory+"/"+dirs[choice]

# make new directory TODO: multiple for one problem
def makeDirectory(directory):
	mkdir(directory)
	mkdir(directory+"/data")
	mkdir(directory+"/code")
	return directory

# check if link is valid
def checkLink(link):
	global site
	domain = urlparse(link).netloc
	if domain in sites:
		site = sites[domain]
		cache["domain"] = domain
		cache["link"] = link
		cache["problem"] = getProblemName(link)
		cache["directory"] = site["pwd"]+"/"+cache["problem"]
		saveCache()
		return True
	print("no such domain")
	return False

# save solution to database
def saveSolution(ext="py", fname=None):
	if fname==None: fname=f'{int(time())}-Save'
	target = f'{cache["directory"]}/code/{fname}.{ext}'
	try: 
		f=open(target,'r')
		f.close()
	except FileNotFoundError: 
		system(f'cp "{root}/work-folder/code/code.{ext}" "{target}"')

# remove solution
def removeFile():
	target = choose(f'{cache["directory"]}/code')
	system(f'mv "{target}" "{root}/trash"')

def login():
	site["checker"].login(driver.getDriver(cache), root)

def post(ext="py"):
	site["checker"].upload(
		saveSolution, 
		f"{root}/work-folder/code/code.{ext}",
		cache["link"],
		driver.getDriver(cache),
		root
	)

def check(diff=False, ext="py"):
	if   ext=="py": py_checker(root, diff)
	elif ext=="cpp": cpp_checker(root, diff)

def view(choice=None):

	n = len(view_prompt)
	prompt = "\n".join([f"{i} {view_prompt[i]}" for i in range(n)])

	try: n_choice = int(choice)
	except: n_choice = -1
	while( 	n_choice not in range(n) and 
			choice not in view_prompt_ans):
		try: 
			print(prompt+"\n")
			choice = input("Choice: ")
			n_choice = int(choice)
		except: n_choice = -1
		if choice=="": return
	if n_choice in range(n): choice = view_prompt_ans[n_choice]
	
	# opener = f'{root}/work-folder/tools/file_opening.sh'
	if   choice=="pdf":
		pdf_name = f'{root}/work-folder/data/problem.pdf'
		system(f'open {pdf_name}')

	elif choice=="i" or choice=="o" or choice=="sol":
		if choice=="sol": data_dir = f'{cache["directory"]}/code'
		else: data_dir = f'{root}/work-folder/data/{["in","out"][choice=="o"]}put'
		files = listdir(data_dir)

		n = len(files)
		prompt = "\n".join([f"{i} {files[i]}" for i in range(n)])
		print(prompt)
		n_choice=-1
		while n_choice not in range(n):
			try: 
				choice = input("Choice: ")
				n_choice = int(choice)
			except: 
				if choice == "": return
				n_choice = -1

		system(f'vim -R {data_dir}/{files[n_choice]}')



# make new problen
def new(link):

	print("\nRetrieving Problem Data...\n")

	if checkLink(link):
		try: 
			makeDirectory(cache["directory"])
			startParser(cache["link"], cache["directory"])
			open_dir(cache["link"])
			copyTemplates()

		except FileExistsError:
			print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
		except: 
			print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
			try: system(f'rm -rf {cache["directory"]}')
			except: pass
	
	print()

if __name__ == "__main__":

	try: link = sys.argv[1]
	except: exit("python3 new.py [link]")

	new(link)