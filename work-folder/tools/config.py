import sys, os
root = "/".join(os.path.realpath(__file__).split("/")[:-3])
sys.path.insert(1, f'{root}/work-folder/tools/parsers')
sys.path.insert(1, f'{root}/work-folder/tools/checkers')
import checker_HackerRank
import parser_HackerRank

cache_init = {
	"directory": None,
	"problem": None,
	"domain": None,
	"link": None,
	"profile": None
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

help_string = """
- new [link]            : create new directory with problem pdf and sample i/o (ignored by git)
- open [link]           : open directory associated with link
- vim [ext?]            : open code.[ext] in vim (default ext=py)
- login                 : logs in to current domain
- save [ext?] [fname?]  : saves to solutions folder (default fname=time())
- clear                 : clear work-folder code and copy templates
- rm                    : remove file from directory (choose in next prompt)
- post [ext?]           : post solution online (headless) and return feedback
- check	[ext?]          : check solution against sample input and output (diff)
- run [ext?]            : run solution using sample input (no diff)
- help                  : print possible commands
"""

view_prompt = [
	"Problem PDF",
	"Sample Input",
	"Sample Ouptut",
	"Saved Solutions"
]

view_prompt_ans = [
	"pdf",
	"i",
	"o",
	"sol"
]