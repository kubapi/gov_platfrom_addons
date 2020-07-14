from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://govtech.hostlab.com.pl/logout")

email = driver.find_element_by_id("inputEmail")
email.clear()
email.send_keys("0Okm!234")

password = driver.find_element_by_name("inputPassword")
password.clear()
password.send_keys("catskillz")

driver.find_element_by_name("submitButton").click()
