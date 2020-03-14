from html.parser import HTMLParser

class HackerRankParser(HTMLParser):

	"""
	Interested Data:
		- Title
		- Difficulty
		- Max Points
		- PDF (problem statement) link
		- Test cases link
	"""
	def __init__(self,prefix):
		super().__init__()

		self.prefix = prefix		# used for download links
		self.curr = None			# last seen data category
		self.level = 0				# level in sidebar

		self.title = None
		self.data = {
			"difficulty": None,
			"maxscore": None,
			"pdf": None,
			"testcases": None
		}

	def handle_starttag(self, tag, attrs):

		d = {x:y for x,y in attrs}
		if "id" not in d : d["id"]=None
		if "class" not in d : d["class"]=None

		# Page Name
		if tag=="meta" and d["id"]=="meta-og-title" and "content" in d:
			self.title = d["content"]

		# Difficulty, Max Score
		elif self.level: self.level+=1
		elif d["class"]=="difficulty-block":
			self.level += 1

		# pdf link
		elif d["id"]=="pdf-link" and "href" in d:
			self.data["pdf"] = d["href"]
			if d["href"][0]=="/": 
				self.data["pdf"]=self.prefix+d["href"]

		# sample test case link
		elif d["id"]=="test-cases-link" and "href" in d:
			self.data["testcases"] = d["href"]
			if d["href"][0]=="/": 
				self.data["testcases"]=self.prefix+d["href"]
				
	def handle_endtag(self, tag):
		if self.level: self.level-=1

	def handle_data(self, data):
		if self.curr: self.data[self.curr] = data
		elif self.level:
			if data=="Difficulty": 
				self.curr = "difficulty"
				return
			elif data=="Max Score": 
				self.curr = "maxscore"
				return
		self.curr = None