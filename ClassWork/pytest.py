# pip install pytest = устанавили пай-тест (в консоли)
import pytest
#import webdriver
# def test_capital_case():
#     result = "qa".upper()
#     expected_result = "QA"
#     assert result == expected_result
#
# def test_raises_exeption_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         "semaphore".capitalize(9)

#--------------------------------------------------------------#
# # ТЕСТИРОВАНИЕ функции существования треугольника
# #  Функции намеренно неправильно
# def is_triangle(a,b,c):
#     return a + b > c # return bool
#
# # test_case
# def test_is_triangle_base_test():
#     result = is_triangle(2,4,5)
#     expected_result = True
#     assert expected_result == result
#
# def test_is_triangle_isnot_exist():
#     result = is_triangle(7,1,1)
#     expected_result = False
#     assert expected_result == result
#
# def test_is_triangle_negative_test():
#     result = is_triangle(-2, -4, -5)
#     expected_result = False
#     assert expected_result == result



#-------------------------------------------------------#
import requests

# response = requests.request(url="https://calcus.ru/kalkulyator-ipoteki", method='GET')
# print(type(response.status_code), response.status_code)

# def test_status_code_200():
#
#     result = response.status_code
#     assert  200 <= result < 400


def test_status_code_200():
    date = "2023-10-10"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  200 <= result < 400

# #-------------------------------------------------------------------------------#
# response = requests.request(url="https://jsonplaceholder.typicode.com/posts", method="GET")
# print(type(response.status_code), response.status_code)


import requests

url="https://jsonplaceholder.typicode.com/posts"
#------------------------------------------------------------------------#
# data = {
#     "title": 'НАША статья',
#     "body": 'Текст статьи',
#     "userId": 1, # кому принадлежит
# }
#
# response = requests.post(url, json=data)
#
# # print("Status Code", response.status_code)
# # print("JSON Response ", response.json()) # response.json() -> превратит в словарь

#----------------------------------------------------------------#

# # # 1 отправить запрос на получение последний статьи
# # posts = requests.get(url)# get запрос
#
#
# #print("Status Code", posts.status_code)
# #print("JSON Response ", posts.json()) # [{}, {} ...]
# # posts = posts.json()
# #post = list(filter(lambda el: el[0]['id'] > 100, posts)) # !!!!!!!!!!!!!
#
# # УСЛОВНОСТЬ: последний элемент отсортирован
# last_old_post = posts[-1]['id']


# # 2 создать статью
# data = {
#     "title": 'НАША статья',
#     "body": 'Текст статьи',
#     "userId": 1, # кому принадлежит
# }
#
# response = requests.post(url, json=data) # post запрос
# new_posts = response.json() # сразу дает словарь {}
# last_new_post = new_posts['id']
# print(last_new_post, last_old_post, last_new_post > last_old_post )

# 3 отправить запрос на получение последний статьи

def test_add_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    # 1 отправить запрос на получение последний статьи
    posts = requests.get(url)  # get запрос
    posts = posts.json()# [{},{}....{}]
    # УСЛОВНОСТЬ: последний элемент маскимальный
    last_old_post = posts[-1]['id'] # 100

    # 2 создать статью
    data = {
        "title": 'НАША статья',
        "body": 'Текст статьи',
        "userId": 1,  # кому принадлежит
    }# задаем параметры

    response = requests.post(url, json=data)  # post запрос
    new_posts = response.json()  # сразу дает словарь {}
    last_new_post = new_posts['id'] # 101

    # 3  новый_id > старый_id
    assert last_new_post > last_old_post(type(response.status_code), response.status_code)
