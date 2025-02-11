"""Создание и настройка опций запуска браузера и открытия страниц"""

import time
from selenium import webdriver

options = webdriver.ChromeOptions()    # (!) создание объекта для опций и их указание происходит ПЕРЕД инициализацией драйвера
# from selenium.webdriver.chrome.options import Options - альтернативный способ инициализации объекта опций c импортом класса
# options = Options()                                   - ..туда же вторым шагом

options.add_argument('--window-size=1920,1080')        # задает размер окна браузера ((!) пробелы внутри скобок не допустимы)
# options.page_load_strategy = 'eager'                 # ожидание загрузки только DOM (html-структуры) перед началом работы со стр.
# options.add_argument('--headless')                   # запуск браузера в фоне (без GUI, напр. при исп. CI/CD)
# options.add_argument('--disable-cache')              # откл. кэширования (все ресурсы на странице будут загружаться всегда)
# options.add_argument('--incognito')                  # запуск браузера в режиме инкогнито (без сохранения данных)
# options.add_argument('--ignore-certificate-errors')  # игнорирует ошибки сертификата SSL у защищенных HTTPS страниц
# options.add_argument('--disable-blink-features=AutomationControlled')   # откл. режима WebDriver-mode (имит. человека)(Lesson_11*)
# options.add_argument("--user-agent=нужный юзер-агент")    # подмена юзер-агента (Lesson_11*)
# options.add_extension('extensions/name_extension.crx')    # установка расширения в браузер с указанием пути к файлу (Lesson_22*)

driver = webdriver.Chrome(options=options)  # (!) инициализация драйвера с добавлением в него ОПЦИЙ (происходит вторым шагом)

driver.get('https://ya.ru/')
time.sleep(1)
print('test passed')

'Стратегия загрузки страницы (normal, eager, none) - так же передается в опциях'
# options.page_load_strategy = 'X'
# normal (используется по умолчанию) - full page load
# eager ("нетерпеливый") - interactive (ожидание загрузки только DOM (html-структуры страницы))
# none ничего не ждет вообще (хз зачем это))
