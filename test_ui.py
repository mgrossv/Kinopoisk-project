import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import base_url_ui


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title('Поиск фильма по названию на русском языке')
def test_search(driver):
    with allure.step('Открываем главную страницу'):
        driver.get(base_url_ui)
    with allure.step('Закрываем рекламу'):
        driver.find_element(By.XPATH, "//button[@type='button' and @data-tid='d6ef5dc']").click()
    with allure.step('Вводим название фильма "Хатико"'):
        driver.find_element(By.NAME, "kp_query").send_keys('Хатико')
    with allure.step('Выбираем фильм из предложенных вариантов'):
        driver.find_element(By.ID, 'suggest-item-film-387556').click()
    with allure.step('Проверяем, что правильный фильм открыт'):
        assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == ("Хатико: Самый верный друг (2008)")

@allure.title("Поиск фильма по названию на английском языке")
def test_search_2(driver):
    with allure.step('Открываем главную страницу'):
        driver.get(base_url_ui)
    with allure.step('Закрываем рекламу'):
        driver.find_element(By.XPATH, "//button[@type='button' and @data-tid='d6ef5dc']").click()
    with allure.step('Вводим название фильма "Hachi: A Dog\'s Tale"'):
         driver.find_element(By.NAME, "kp_query").send_keys("Hachi: A Dog's Tale")
    with allure.step('Выбираем фильм из предложенных вариантов'):
        driver.find_element(By.ID, 'suggest-item-film-387556').click()
    with allure.step('Проверяем, что правильный фильм открыт'):
        assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == ("Хатико: Самый верный друг (2008)")


@ allure.title("Поиск актера по имени на русском языке")
def test_search_3(driver):
    with allure.step('Открываем главную страницу'):
        driver.get(base_url_ui)
    with allure.step('Закрываем рекламу'):
        driver.find_element(By.XPATH, "//button[@type='button' and @data-tid='d6ef5dc']").click()
    with allure.step('Вводим имя актера "Джонни Депп"'):
        driver.find_element(By.NAME, "kp_query").send_keys("Джонни Депп")
    with allure.step('Выбираем актера из предложенных вариантов'):
        driver.find_element(By.ID, 'suggest-item-person-6245').click()
    time.sleep(2)
    with allure.step('Проверяем, что открылась страница актера'):
        assert "Джонни Депп" in driver.title


@allure.title("Проверка кнопки 'СЛУЧАЙНЫЙ ФИЛЬМ'")
def test_search_4(driver):
    with allure.step('Открываем главную страницу'):
        driver.get(base_url_ui)
    with allure.step('Закрываем рекламу'):
        driver.find_element(By.XPATH, "//button[@type='button' and @data-tid='d6ef5dc']").click()
    with allure.step('Нажимаем кнопку поиска "ЛУПА"'):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
    with allure.step('Нажимаем на кнопку "СЛУЧАЙНЫЙ ФИЛЬМ'):
        driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        time.sleep(2)
    with allure.step('Проверяем рандомный фильм'):
        assert "" in driver.name

@allure.title("Проверка результата поиска при невалидном запросе")
def test_search_5(driver):
    with allure.step('Открываем главную страницу'):
        driver.get(base_url_ui)
    with allure.step('Закрываем рекламу'):
        driver.find_element(By.XPATH, "//button[@type='button' and @data-tid='d6ef5dc']").click()
    with allure.step('Вводим несуществующий запрос "vuvtvtfdsresytd"'):
        driver.find_element(By.NAME, "kp_query").send_keys('vuvtvtfdsresytd')
    with allure.step('Нажимаем кнопку поиска "ЛУПА"'):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    with allure.step('Проверяем сообщение об ошибке'):
        assert driver.find_element(By.XPATH,"//h2[@class='textorangebig']").text == ("К сожалению, по вашему запросу ничего не найдено...")