import sys; sys.path.insert(1, 'Parsers')
import os

pwd = "../solutions"

site = {
	"full_prefix":"https://www.hackerrank.com",
	"problem_re":"/challenges/(.*)/.*"
}

languages = {
	"py": "Python 3",
	"cpp": "C++",
	"java": "Java",
	"c": "C",
	"js": "JavaScript"
}

init = {
	"Title": None,
	"Directory": None,
	"Links": {
		"Problem": None,
		"PDF": None,
		"Test Case": None
	},
	"Data": {
		"Difficulty": None,
		"Max Score": None
	},
	"Status": {
		"Best Time Complexity": None,
		"Best Space Complexity": None,
		"Best CodeGolf Length": None,
		"Solve Status": None,
		"Languages Used": None
	}
}