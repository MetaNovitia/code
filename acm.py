from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys,time
from os import system

def scrape():
	problems = []

	link = "http://acm-uci.org/Puzzle/"
	options = Options()
	options.add_argument("--headless")
	capabilities = options.to_capabilities()
	driver = webdriver.Firefox(desired_capabilities=capabilities)
	driver.get(link)
	time.sleep(4)
	buttons = driver.find_elements_by_tag_name('button')
	for b in buttons:
		if b.text=="Week 9":
			b.click()
			time.sleep(1)
			links = driver.find_elements_by_tag_name('a')
			for m in links:
				l = m.get_attribute("href")
				if( l and not l.startswith("http://acm-uci.org/") and 
					l!="https://github.com/ACM-UCI/ACM-UCI-Website/issues" ):
					problems.append(l)
	print("-- Done --")
	return problems

def main():
	problems = scrape()
	"""
	Do something
	"""

try: main()
except: 
	print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
	system("rm geckodriver.log")