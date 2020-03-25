import time, os, sys, json
from lang import languages

driver = None
login_page = "https://www.hackerrank.com/auth/login"

def add_code(fname):
	driver.find_element_by_class_name("upload-file").click()
	driver.find_element_by_class_name("confirm-button").click()
	driver.find_element_by_class_name("d-none").send_keys(fname)
	driver.find_elements_by_class_name("ui-btn-primary")[-1].click()
	print("Uploading...")

def processCases():
	total = {}
	cases = driver.find_elements_by_class_name("testcase-item")
	for tab in cases:
		tab.click()
		err = driver.find_elements_by_class_name("compiler-message__value")
		while len(err)==0: 
			time.sleep(0.1)
			err = driver.find_elements_by_class_name("compiler-message__value")

		if len(err):
			if err[0].text not in total: 
				total[err[0].text]=0
			total[err[0].text]+=1

	for e in total:
		print(f"{e}: {total[e]}")

def select_language(lang):
	driver.find_element_by_id("react-select-2-input").send_keys(lang+u'\ue007')

def keep_adding_code(fname):
	add_code(fname)
	time.sleep(1)
	ct = 0
	while(len(driver.find_elements_by_id("hr-monaco-loading-language"))):
		ct+=1
		time.sleep(1)
		if ct==5: ct=0
		add_code(fname)

def click_submit():
	time.sleep(1)
	driver.find_element_by_class_name("hr-monaco-submit").click()
	time.sleep(1)
	print("Waiting for Submission...")
	while len(driver.find_elements_by_class_name("tc-live-status-wrapper")): 
		time.sleep(1)
	print("Finished Submitting")
	time.sleep(1)

def checkFeedback(saveSolution, ext):
	if len(driver.find_elements_by_class_name("congrats-heading")): 
		ans = ""
		while True:
			ans=input("Submission Passed All Test Cases! Save? (Y/N): ")
			if ans=="Y":
				name = input("Name: ")
				if name=="": saveSolution(ext,f"{int(time.time())}-Pass")
				else: saveSolution(ext,f"{name}-Pass")
				break
			elif ans=="N":
				break
	else:
		err = driver.find_elements_by_class_name("compile-error")
		if len(err): print(err[0].text)
		processCases()

def upload(saveSolution, fname, link, main_driver, root):
	try:
		if driver==None: login(main_driver, root)
		driver.get(link)

		ext = fname.split(".")[-1]
		lang = languages[ext]
		select_language(lang)
		keep_adding_code(fname)
		click_submit()
		checkFeedback(saveSolution, ext)

	except: print(
				f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} "+
				f"line: {sys.exc_info()[2].tb_lineno}")

	print("----------------")

def promptCredentials(fname, credentials):
	credentials["HackerRank"] = [input("username: "), input("password: ")]
	f=open(fname,'w')
	f.write(json.dumps(credentials, indent=4))
	f.close()
	return credentials["HackerRank"]

def getCredentials(root):
	fname = f'{root}/work-folder/passwords.json'
	credentials = {}
	try:
		f=open(fname,'r')
		credentials = json.loads(f.read())
		f.close()
		if "HackerRank" not in credentials: 
			return promptCredentials(fname, credentials)

	except FileNotFoundError: 
		return promptCredentials(fname, {})

	return credentials["HackerRank"]

def login(main_driver, root):

	global driver

	driver = main_driver

	print("LOGGING IN...")
	try:
		username,password = getCredentials(root)
		driver.get(login_page)
		
		driver.find_element_by_id('input-1').send_keys(username)
		driver.find_element_by_id('input-2').send_keys(password)
		driver.find_elements_by_class_name("auth-button")[0].click()
		time.sleep(2)
	except: print("Already logged in")

	print("Logged In")