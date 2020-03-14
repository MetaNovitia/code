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