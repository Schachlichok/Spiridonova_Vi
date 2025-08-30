import time

from selenium import webdriver

# Опции
options = webdriver.ChromeOptions() #TODO: инициализация атирибута класса Options, который имеет стандартные настройки,
#TODO: для дальнейшего изменения параметров класса
# options.add_argument("--headless=new") #TODO: добавление в стандартные настройки нужную опцию (Работа без интерфейса, база докера)
options.add_argument("--incognito") #TODO: добавление в стандартные настройки нужную опцию (Не скапливаются кэш и куки)
#options.add_argument('--ignore-certificate-errors') #TODO: добавление в стандартные настройки нужную опцию (Обходим лишние действия на странице)
options.add_argument("--window-size=1920,1080") #TODO: изменение в стандартных настройках параметры экрана
options.page_load_strategy = "eager" #TODO: ожидает готовность только html структуры и ничего больше (DOM, без стилей и прочего)

# Локаторы
field_upload_field = ("xpath", "//input[@id='uploadFile']") # Если не ищется, то возможно он скрыт в button, искать через type = file

# Инициализация
driver = webdriver.Chrome(options = options) #TODO По умолчанию опции отключены,переприсваем на атрибут класса с измен. настр-ми

driver.get("https://demoqa.com/upload-download") # Переходим на сайт
print(driver.current_url) #Выводим текущий url
print(driver.title) # Выводим тайтл
assert driver.title == "DEMOQA", "error title" # Проверяем ожидаемый тайтл и фактический

upload_field = driver.find_element(*field_upload_field) #TODO присваиваем переменной объект веб-страницы через локатор
upload_field.send_keys(r"C:\Users\ShashlichoK\PycharmProjects\Spiridonova_V\screen\example.jpg") #TODO вводим абсолютный
# путь до файла, чтоб загрузить картинку
time.sleep(5)