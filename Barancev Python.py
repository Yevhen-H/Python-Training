from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/Users/yhurt/WEB(Barancev)/geckodriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()