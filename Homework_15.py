import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("window-size=1920x1080")


driver = webdriver.Chrome(options = options)
driver.get("https://demoqa.com/upload-download")
print(driver.current_url)
print(driver.title)
assert driver.title == "DEMOQA", "ERROR"

field_input = ("xpath", "//input[@id='uploadFile']")
upload_file = driver.find_element(*field_input)
upload_file.send_keys(r"C:\Users\ShashlichoK\PycharmProjects\Spiridonova_V\picture.jpg")
time.sleep(5)

