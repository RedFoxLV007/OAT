*** Settings ***
Library     Selenium2Library
*** Test Cases ***
Тест на сайте Яндекс
	Open Browser    https://www.ya.ru  googlechrome
   	Maximize Browser Window
	Close Browser
