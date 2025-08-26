from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

field_full_name = driver.find_element("xpath", "//input[@id = 'userName']")
field_email = driver.find_element("xpath", "//input[@id = 'userEmail']")
field_current_address =  driver.find_element("xpath", "//textarea[@id='currentAddress']")
field_permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")

field_full_name.clear()
field_email.clear()
field_current_address.send_keys(Keys.CONTROL+"A")
field_current_address.send_keys(Keys.BACKSPACE)
field_permanent_address.send_keys(Keys.CONTROL+"A")
field_permanent_address.send_keys(Keys.BACKSPACE)

assert field_full_name.get_attribute("value") == "", "Не стерты данные"
assert field_email.get_attribute("value") == "", "Не стерты данные"
assert field_current_address.get_attribute("value") == "", "Не стерты данные"
assert field_permanent_address.get_attribute("value") == "", "Не стерты данные"

field_full_name.send_keys("Собака-Кусака")
field_email.send_keys("Dogger33@gmail.com")
field_current_address.send_keys("г.Томск, село Зеленое, д. 3")
field_permanent_address.send_keys("г.Томск, село Зеленое, д. 3")

assert field_full_name.get_attribute("value") == "Собака-Кусака", "Error value"
assert field_email.get_attribute("value") == "Dogger33@gmail.com", "Error value"
assert field_current_address.get_attribute("value") == "г.Томск, село Зеленое, д. 3", "Error value"
assert field_permanent_address.get_attribute("value") == "г.Томск, село Зеленое, д. 3", "Error value"