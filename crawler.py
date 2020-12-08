import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description='Auto sigin and signout.')
parser.add_argument('-t', '--time', default=4, 
	type=int, dest='time', 
	help='set signin and signout duration (hr)')
parser.add_argument('-wid', '--work_id', default='', 
	type=str, dest='wid', 
	help='work id, the id from url')
parser.add_argument('-a', '--account', default='', 
	type=str, dest='acc', 
	help='user account')
parser.add_argument('-p', '--password', default='', 
	type=str, dest='pwd', 
	help='user password')

args = parser.parse_args()

assert len(args.wid) > 0, 'work id can not be empty!'
assert len(args.acc) > 0 and len(args.pwd) > 0, 'account and password can not be empty!'

# webdriver options setting
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

chrome = webdriver.Chrome(chrome_options=options)

url = 'https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create?ParttimeUsuallyId=' \
		+ args.wid

chrome.get(url)

# Fill sign in infomation
chrome.find_element_by_id('inputAccount').send_keys(args.acc)
chrome.find_element_by_id('inputPassword').send_keys(args.pwd)

# login
chrome.find_element_by_css_selector('button.btn.btn-primary').click()

assert chrome.current_url != 'https://portal.ncu.edu.tw/login',\
		'Wrong account or password!'

# Redirection from NCU portal to human system
chrome.find_element_by_css_selector('button.btn.btn-primary').click()

# sign in and out
chrome.find_element_by_id('signin').click()
time.sleep(3600 * args.time + 60)
chrome.find_element_by_id('signout').click()
