from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os, sys
from config import languages

def add_code(driver, fname="code/code.py"):
	driver.find_element_by_class_name("upload-file").click()
	driver.find_element_by_class_name("confirm-button").click()
	driver.find_element_by_class_name("d-none").send_keys(os.getcwd()+"/"+fname)
	driver.find_elements_by_class_name("ui-btn-primary")[-1].click()
	print("Uploading...")

def processCases(driver):
	total = {}
	cases = driver.find_elements_by_class_name("testcase-item")
	for tab in cases:
		tab.click()
		err = driver.find_elements_by_class_name("compiler-message__value")
		ct=0
		while len(err)==0: 
			time.sleep(0.1)
			err = driver.find_elements_by_class_name("compiler-message__value")
			ct+=1
			if(ct==5): print(tab.text+" unread")

		if len(err):
			if err[0].text not in total: 
				total[err[0].text]=0
			total[err[0].text]+=1

	for e in total:
		print(f"{e}: {total[e]}")


def upload(driver, fname="code/code.py"):
	try:
		ext = fname.split(".")[-1]
		lang = languages[ext]
		driver.find_element_by_id("react-select-2-input").send_keys(lang+"\n")
		add_code(driver, fname)
		time.sleep(1); ct = 0
		while(len(driver.find_elements_by_id("hr-monaco-loading-language"))):
			ct+=1; time.sleep(1)
			if ct==5: ct=0; add_code(driver, fname)
		driver.find_element_by_class_name("hr-monaco-submit").click(); time.sleep(1)
		print("Waiting for Submission...")
		while len(driver.find_elements_by_class_name("tc-live-status-wrapper")): time.sleep(1)
		print("Finished Submitting")

		if len(driver.find_elements_by_class_name("congrats-heading")): 
			print("Submission Passed All Test Cases!")
			save(f"{int(time.time())}-Pass",ext)
		else:
			err = driver.find_elements_by_class_name("compile-error")
			if len(err): print(err[0].text)
			processCases(driver)

	except: print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
	print("----------------")

def login():

	print("OPEN NEW")

	options = Options()
	capabilities = options.to_capabilities()

	driver = webdriver.Chrome(desired_capabilities=capabilities)

	link = load("link")

	driver.get(link)

	try: username,password=load("password").split()
	except: print("Add username and password (on separate lines) in data/password.txt")
	
	driver.find_element_by_id("auth-login").click()
	driver.find_element_by_id('input-4').send_keys(username)
	driver.find_element_by_id('input-5').send_keys(password)
	driver.find_elements_by_class_name("auth-button")[0].click()
	time.sleep(2)

	print("Logged In")

	return driver

def save(fname=None, ext="py"):
	directory=load("current_directory")
	if fname==None: fname=int(time.time())
	target = f"{directory}/{fname}.{ext}"
	try: open(target)
	except FileNotFoundError: 
		os.system(f'cp "code/code.{ext}" "{target}"')

def load(fname):
	f=open(f"data/{fname}.txt",'r')
	data = f.read().strip()
	f.close()
	return data

def main():
	driver = login()
	ans = [""]

	while ans[0]!="end" and ans[0]!="quit":
		try:
			print("Command (post/save/end/quit): ",end="")
			ans = input().split()
			if len(ans)<2: ans.append("py")

			if ans[0] == "post": upload(driver, "code/code."+ans[1])
			elif ans[0] == "save":
				if len(ans)<3: ans.append(f"{int(time.time())}-Save")
				save(ans[2], ans[1])
		
		except: print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")

	if ans[0]=="quit": driver.quit()

if __name__=="__main__":
	main()