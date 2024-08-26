# Kinopoisk-project
## Описание
Проект включает в себя создание набора автоматизированных тестов для проверки функциональности веб-приложения "Кинопоиск". 
### UI - тест кейсы:
test_search Поиск фильма по названию на русском языке,test_search_2 Поиск фильма по названию на английском языке,test_search_3 Поиск актера по имени на русском языке,test_search_4 Проверка кнопки 'СЛУЧАЙНЫЙ ФИЛЬМ,test_search_5 Проверка результата поиска при невалидном запросе.
### API - тест кейсы:
test_get_movie_by_name Получить список по названию фильма,test_get_movie_by_date Получить список фильмов по году выпуска,test_get_movie_by_rating Получить список фильмов по рейтингу,test_movie_by_type Получить список по жанру, test_get_list_top_250 Получить список топ 250 на кинопоиске.
## Зависимости
Все необходимые зависимости requirements.txt - установка pip install -r requirements.txt
## Конфигурация
Файл config.py содержит настройки окружения: URL, X-API-KEY. 
