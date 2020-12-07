import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description='Auto sigin and signout.')
parser.add_argument('-t', '--time', default=4, type=int, dest='time', help='set signin and signout duration(hr)')
parser.add_argument('-wid', '--work_id', default='', type=str, dest='wid', help='work id')
parser.add_argument('-a', '--account', default='', type=str, dest='acc', help='account')
parser.add_argument('-p', '--password', default='', type=str, dest='pwd', help='password')

args = parser.parse_args()

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

chrome = webdriver.Chrome(chrome_options=options)

url = 'https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create?ParttimeUsuallyId=' + args.wid

chrome.get(url)

chrome.find_element_by_id('inputAccount').send_keys(args.acc)
chrome.find_element_by_id('inputPassword').send_keys(args.pwd)

chrome.find_element_by_css_selector('button.btn.btn-primary').click()
chrome.find_element_by_css_selector('button.btn.btn-primary').click()

chrome.find_element_by_id('signin').click()
time.sleep(3600 * args.time + 60)
chrome.find_element_by_id('signout').click()
