from html.parser import HTMLParser
from os import system
from zipfile import ZipFile
from urllib.request import urlopen
from json import dumps, loads

class HackerRankParser(HTMLParser):

	"""
	Interested Data:
		- Title
		- Difficulty
		- Max Points
		- PDF (problem statement) link
		- Test cases link
	"""
	def __init__(self, prefix, link, directory):
		super().__init__()

		self.prefix = prefix		# used for download links
		self.curr = None			# last seen data category
		self.level = 0				# level in sidebar

		self.data = {}
		self.load("init.json")
		self.data["Links"]["Problem"] = link
		self.data["Directory"] = directory

	def feed(self):
		html = urlopen(self.data["Links"]["Problem"]).read().decode("utf-8")
		super().feed(html)

	def handle_starttag(self, tag, attrs):

		d = {x:y for x,y in attrs}
		if "id" not in d : d["id"]=None
		if "class" not in d : d["class"]=None

		# Page Name
		if tag=="meta" and d["id"]=="meta-og-title" and "content" in d:
			self.data["Title"] = d["content"]

		# Difficulty, Max Score
		elif self.level: self.level+=1
		elif d["class"]=="difficulty-block":
			self.level += 1

		# pdf link
		elif d["id"]=="pdf-link" and "href" in d:
			self.data["Links"]["PDF"] = d["href"]
			if d["href"][0]=="/": 
				self.data["Links"]["PDF"]=self.prefix+d["href"]

		# sample test case link
		elif d["id"]=="test-cases-link" and "href" in d:
			self.data["Links"]["Test Case"] = d["href"]
			if d["href"][0]=="/": 
				self.data["Links"]["Test Case"]=self.prefix+d["href"]
				
	def handle_endtag(self, tag):
		if self.level: self.level-=1

	def handle_data(self, data):
		if self.curr: self.data["Data"][self.curr] = data
		elif self.level:
			if data in self.data["Data"]: 
				self.curr = data
				return
		self.curr = None

	def download(self, link, filename):		# generic
		data = urlopen(link).read()
		f=open(filename,'wb')
		f.write(data)
		f.close()
		print("Downloaded " + filename)
	
	def downloadPDF(self):
		try: self.download(self.data["Links"]["PDF"], self.data["Directory"]+"/problem.pdf")
		except: print("No PDF Data")

	def downloadTestCases(self):
		try: 
			fname = self.data["Directory"]+"/test.zip"
			self.download(self.data["Links"]["Test Case"], fname)
			with ZipFile(fname, 'r') as zipObj:
				zipObj.extractall(self.data["Directory"])
			system("rm \""+fname+"\"")
		except: print("No Test Case Data")

	def save(self):
		f = open(self.data["Directory"]+"/problem.json", 'w')
		f.write(dumps(self.data, indent=4))
		f.close()

	def load(self, fname=None):
		if fname==None: fname=self.data["Directory"]+"/problem.json"
		f = open(fname, 'r')
		self.data = loads(f.read())
		f.close()

	def makeLinkString(self, link, name):
		return (f'<a href="{link}" target="_blank" rel="noopener noreferrer">{name}</a>')

	def makeReadMe(self):
		f = open(self.data["Directory"]+"/README.md",'w')
		f.write("# " + self.data["Title"] + "\n\n")
		for d in self.data["Data"]:
			if self.data["Data"][d]: 
				f.write(f'- {d}: {self.data["Data"][d]}\n')
		for l in self.data["Links"]:
			if self.data["Links"][l]:
				f.write(f'- {l}: {self.makeLinkString(self.data["Links"][l],"link")}\n')
		f.close()

	def process(self):
		self.downloadPDF()
		self.downloadTestCases()
		self.makeReadMe()
		self.save()