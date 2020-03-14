from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os, sys
from config import languages

driver = None
fname = os.getcwd()+"/data/code.py"
lang = languages[fname.split(".")[-1]]

options = Options()
options.add_argument("--headless")
capabilities = options.to_capabilities()

def add_code(driver):
	driver.find_element_by_class_name("upload-file").click()
	driver.find_element_by_class_name("confirm-button").click()
	driver.find_element_by_class_name("d-none").send_keys(fname)
	driver.find_elements_by_class_name("ui-btn-primary")[-1].click()

def upload(driver):
	try:

		driver.find_element_by_id("react-select-2-input").send_keys(lang+"\n")
		add_code(driver)
		time.sleep(1)
		ct = 0
		while(len(driver.find_elements_by_id("hr-monaco-loading-language"))):
			ct+=1
			time.sleep(1)
			if ct==5:
				ct=0
				add_code(driver)
		
		driver.find_element_by_class_name("hr-monaco-submit").click()
		
		time.sleep(1)
		while len(driver.find_elements_by_class_name("tc-live-status-wrapper")):
			time.sleep(1)
		
		print("Finished Submitting")

	except: print("ERR")

def main():
	f=open("data/latest_session.txt",'r')
	session_id,url = f.read().split()
	f.close()
	driver = webdriver.Remote(url, desired_capabilities=capabilities)
	driver.session_id = session_id
	upload(driver)
	
if __name__=="__main__":
	main()
	print("Finished")