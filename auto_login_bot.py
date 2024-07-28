# Used to import the webdriver from selenium
from selenium import webdriver  
import os
 
# Get the path of chromedriver which you have install
 
def startBot(username, password, url):
    
    path = "C:\\Users\\hp\\Downloads\\chromedriver"
     # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)
     
     # opening the website  in chrome.
    driver.get(url)
    
     

 
 
# Driver Code
# Enter below your login credentials
username = "Enter your username"
password = "Enter your password"
 
# URL of the login page of site
# which you want to automate login.
url = "Enter the URL of login page of website"
 
# Call the function
startBot(username, password, url)