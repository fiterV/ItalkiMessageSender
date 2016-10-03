#!/usr/bin/env python
from selenium import webdriver
from time import sleep
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--email', help='Your email address')
parser.add_argument('-p', '--password', help='Password to your email account')
parser.add_argument('-M', '--message', help = 'Message that you want to send to all of the natives')
args = parser.parse_args()

if (None in [args.email, args.password, args.message]):
	print('Provide full infomation please(for that read the help)')
	exit(0)

browser = webdriver.Firefox()
sleep(1)
browser.get('https://www.italki.com/signin')
username = (browser.find_element_by_id('username_id'))
password = (browser.find_element_by_id('password_id'))
username.send_keys(args.email)
sleep(0.5)
password.send_keys(args.password)
sleep(1)
browser.find_element_by_tag_name('button').click()
sleep(0.5)
file = open('natives.txt', 'r')
natives = file.read()
natives = natives.split('\n')
for i in natives:
	link = 'https://www.italki.com'+i
	browser.get(link)
	html = browser.page_source
	if (html.find('Sorry, this profile has been removed or deactivated.')>0):
		continue
	if (html.find('You must be friends with ')>0):
		continue
	if (html.find('Switch to Teacher Profile')>0):
		print 'This is a teacher ' + link
		break
	send = browser.find_element_by_xpath("//*[@class='fa fa-comment']")
	send.click()
	sleep(1)
	messageField = browser.find_element_by_tag_name('textarea')
	messageField.click()
	sleep(1)
	name = (browser.find_element_by_class_name('no-margin').get_attribute('innerHTML')).split(' ')[0]
	
	messageField.send_keys(args.message)
	sleep(1)
	sendMessage = browser.find_element_by_xpath("//*[@class='btn btn-primary with-spinner hidden-phone pull-left']")
	sendMessage.click()
	sleep(2)
