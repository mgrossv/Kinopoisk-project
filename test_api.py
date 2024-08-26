import allure
from kinopoisk_apy import Kinopoisk
from config import base_url,headers


api = Kinopoisk(base_url+'movie')

@allure.title('Поиск по названию фильма')
def test_get_movie_by_name():
    with allure.step('Получить список с названием Naruto'):
        resp = api.get_by_name("Naruto",headers)
        response = resp.json()['docs'][0]['internalNames']
    with allure.step('Проверить, что полученные данные совпадают c названием фильма'):
        assert response.count('Naruto')
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('Поиск по году выпуска')
def test_get_movie_by_date():
    with allure.step('Получить список фильмов 1993 года выпуска'):
        resp = api.get_by_name(1993,headers)
        response = resp.json()['docs'][0]['year']
    with allure.step('Проверить, что полученные данные совпадают с годом выпуска'):
        assert response == 1993
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('Поиск по рейтингу на кинопоиске')
def test_get_movie_by_rating():
    with allure.step('Получить список фильмов с рейтингом 6 у кинопоиска'):
        resp = api.get_by_rating(6,headers)
        response = resp.json()['docs'][0]['rating']['kp']
    with allure.step('Проверить, что полученные данные совпадают с рейтингом 6 у кинопоиска'):
        assert response == 6
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('Получить список аниме на кинопоиске')
def test_movie_by_type():
    with allure.step('Получить список аниме на кинопоиске'):
        resp = api.get_by_type("anime",headers)
        response = resp.json()['docs'][0]['type']
    with allure.step('Проверить, что получили список аниме на кинопоиске'):
        assert response == "anime"
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('Получить список топ 250 на кинопоиске')
def test_get_list_top_250():
    with allure.step('Получить список топ 250'):
        resp = api.get_list_top_250(headers)
        response = resp.json()['docs']
    with allure.step('Проверить, что получили список топ 250'):
        assert len(response) == 250
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200