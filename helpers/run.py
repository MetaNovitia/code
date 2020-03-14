from os import system, mkdir
from config import sites, pwd
from urllib.parse import urlparse
import big_o
import re

def openParser(site, link, directory):
	print("Starting Parser...")
	parser = site["parser"](site["full_prefix"], link, directory)
	parser.feed()
	parser.process()
	print("Parsing Finished!\n")
	return parser

def getProblemName(site, path):
	problem_match = re.match(site["problem_re"],path)
	if problem_match==None: 
		raise ValueError("Problem regex failed match")
	problem=problem_match.group(1)
	return problem

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
			directory = getDirectories(site, problem)
			parser = startParser(site, link, directory)

	except ValueError as err:
		print("ERROR:",err)
		exit()
	
	print()

if __name__ == "__main__":
	try: main()
	except FileNotFoundError as err: print(err)