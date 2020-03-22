from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = None

def getDriver(cache):
	if driver==None: new(cache)
	return driver

def new(cache):
	global driver
	options = Options()
	options.add_argument("--headless")
	if cache["profile"]!=None: 
		options.add_argument(f'user-data-dir={cache["profile"]}')
	capabilities = options.to_capabilities()
	driver = webdriver.Firefox(desired_capabilities=capabilities)
	if cache["profile"]==None: getProfile(cache)

def getProfile(cache):
	driver.get("about:profiles")
	l=driver.find_elements_by_tag_name("tr")
	for i in l: 
		inn = i.get_attribute('innerHTML')
		if "Root Directory" in inn:
			cache["profile"] = inn.split("<td")[1].split(">")[1].split("<")[0]
			break
	