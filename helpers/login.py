from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from post import upload
import time, os

def login():

	print("OPEN NEW")

	driver = webdriver.Chrome()

	driver.get('https://www.hackerrank.com/challenges/queens-attack-2/problem')

	try:
		f=open("data/password.txt")
		username,password=f.read().split()
		f.close()
	except: print("Add username and password (on separate lines) in data/password.txt")
	
	driver.find_element_by_id("auth-login").click()
	driver.find_element_by_id('input-4').send_keys(username)
	driver.find_element_by_id('input-5').send_keys(password)
	driver.find_elements_by_class_name("auth-button")[0].click()
	time.sleep(2)

	url = driver.command_executor._url
	session_id = driver.session_id

	f=open("data/latest_session.txt",'w')
	f.write(f"{session_id}\n{url}")
	f.close()

	print("Logged In")

	return driver

if __name__ == "__main__":
	driver = login()
	ans = ""
	while ans!="end":
		ans = input("Command (post/end): ")
		if ans == "post": 
			response = upload(driver)