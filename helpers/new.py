from os import system, mkdir
from config import sites, pwd
from urllib.parse import urlparse
from urllib.request import urlopen
from time import time
from zipfile import ZipFile
import re

def makeReadMe(data, directory, title):
	f = open(directory+"/README.md",'w')
	f.write("# " + title + "\n\n")
	for d in data:
		if data[d]: f.write("- "+d+": "+data[d]+"\n")
	f.close()

def download(link, filename):
	data = urlopen(link).read()
	f=open(filename,'wb')
	f.write(data)
	f.close()
	print("Downloaded " + filename)

def startParser(site, html):
	print("Starting Parser...")
	parser = site["parser"](site["full_prefix"])
	parser.feed(html)
	print("Parsing Finished!\n")
	return parser

def getProblemName(site, path):
	problem_match = re.match(site["problem_re"],path)
	if problem_match==None: 
		raise ValueError("Problem regex failed match")
	problem=problem_match.group(1)
	f=open("data/problemname",'w')
	f.write(problem)
	f.close()
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
		html = urlopen(link).read().decode("utf-8")

		if domain in sites:

			site = sites[domain]
			problem = getProblemName(site, path)
			directory = makeDirectory(site, problem)
			parser = startParser(site, html)

			# process pdf
			try: download(parser.data["pdf"], directory+"/problem.pdf")
			except: print("No PDF Data")

			# process test cases
			try: 
				download(parser.data["testcases"], directory+"/test.zip")
				with ZipFile(directory+"/test.zip", 'r') as zipObj:
					zipObj.extractall(directory)
				system("rm \""+directory+"/test.zip\"")
			except: print("No Test Case Data")

			makeReadMe(parser.data, directory, parser.title)



	except ValueError as err:
		print("ERROR:",err)
		exit()
	
	print()

if __name__ == "__main__":
	main()