import sys
from root import root

sys.path.insert(1, f'{root}/work-folder/tools/parsers')
sys.path.insert(1, f'{root}/work-folder/tools/checkers')
import checker_HackerRank
import parser_HackerRank

cache_init = {
	"current_directory": None,
	"problem": None,
	"domain": None,
	"link": None,
	"passwords": {}
}

sites = {
	"www.hackerrank.com": {
		"name": "HackerRank",
		"full_prefix": "https://www.hackerrank.com",
		"problem_re":"/challenges/(.*)/problem",
		"pwd": f'{root}/HackerRank/solutions',
		"checker": checker_HackerRank,
		"parser": parser_HackerRank.HackerRankParser
	},
	"open.kattis.com": {
		"name": "Kattis",
		"full_prefix": "https://open.kattis.com",
		"problem_re":"/problems/(.*)",
		"pwd": f'{root}/Kattis/solutions',
		"checker": None,
		"parser": None
	}
}