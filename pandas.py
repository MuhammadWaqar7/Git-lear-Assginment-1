selenium == 3.141.0
pandas
urllib3>2.0.0
# from selenium import webdriver
# from selenium.webdriver.chrome.service
from selenium import webdriver
from selenium.webdriver.chrome.service. import Service
website='https://www.365scores.com/football/team/fc-barcelona-132'
path=r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# Set up the ChromeDriver
service = Service(path)
service.start()
#create a new instance of the Chrome driver
driver = webdriver.Chrome(path)

# Open a webpage
driver.get(website)
driver.find_element_by_xpath('//h1')
s=driver.find_elements_by_xpath('//h1')
standings =driver.find_elemints_by_xpath('//table[]') 
# git clone https://github.com/MuhammadUzair1/Selenium-MasterProject
# cd Selenium-MasterProject
path = '/path/to/chromedriver'  # Replace with your actual path
python script.py



# Locate an element using XPath
# element = driver.find_element(By.XPATH, '//h1')

# # Print the text of the element
# print(element.text)

# # Close the browser
# driver.quit()
