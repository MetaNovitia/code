import sys; sys.path.insert(1, 'Parsers')
import hackerrank

pwd = "../"

sites = {
	"www.hackerrank.com": {
		"name":"HackerRank",
		"full_prefix":"https://www.hackerrank.com",
		"parser": hackerrank.HackerRankParser,
		"problem_re":"/challenges/(.*)/problem"
	}
}

languages = {
	"py": "Python 3",
	"cpp": "C++",
	"java": "Java",
	"c": "C",
	"js": "JavaScript"
}