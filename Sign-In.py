from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #so we don't have to install the chrome driver on our own
from selenium.webdriver.common.keys import Keys #gives access to type keys like escape, 'j', etc

import time

with open('passwords.txt', 'r') as file:
    legitPass = file.read().rstrip('\n')

with open('usernames.txt', 'r') as file:
    legitUser = file.read().rstrip('\n')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jomaclass.com/login") #the url we're opening

username = driver.find_element_by_id("member_email") #find username field
password = driver.find_element_by_id("member_password") #find password field
sign_in = driver.find_elements_by_name("commit")


## configure username and password parameter so that it take a specific element from a list of usernames and passwords based on the site title.
username.send_keys(legitUser)
password.send_keys(legitPass)

password.send_keys(Keys.RETURN)

time.sleep(10) #wait 10s before continuing further in code
driver.quit() #this closes everything

#search by id -> name -> class (this is in best to worst case order)
#this closes the tab driver.close()

