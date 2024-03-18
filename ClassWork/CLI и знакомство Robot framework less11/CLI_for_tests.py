import argparse  # Импортируем библиотеку argparse для обработки аргументов командной строки
import pytest    # Импортируем библиотеку pytest для запуска тестов
import sys       # Импортируем библиотеку sys для управления выходом из программы


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="CLI for running tests")

    # Определяем аргументы командной строки

    # Позиционный аргумент - список файлов с тестами
    # в tests записываем какие модули надо запустить
    parser.add_argument("tests", nargs="*", help="Specify test files to run")

    # Опциональный аргумент для генерации HTML-отчета
    parser.add_argument("--html-report", help="Generate HTML report")

    # Парсим переданные аргументы командной строки
    args = parser.parse_args()

    # Запускаем тесты с переданными аргументами
    run_tests(args)

'''
run_tests 
определить аргументы
и произвести непосреведнный запуск тестированию по заданной команде
'''
def run_tests(args):
    # Формируем список аргументов для передачи в pytest
    pytest_args = []

    # Если указаны тестовые файлы, добавляем их в список аргументов
    if args.tests: # args.tests - записываем какие модули надо запустить
        pytest_args.extend(args.tests) # преобразование и записи


    # Если указана опция для генерации HTML-отчета, добавляем соответствующий аргумент
    if args.html_report:
        pytest_args.append("--html={}".format(args.html_report))

    # Запускаем тесты с использованием pytest и переданных аргументов
    exit_code = pytest.main(pytest_args)

    # Завершаем выполнение программы с кодом возврата, полученным от pytest
    sys.exit(exit_code)


if __name__ == "__main__":
    main() # python CLI_for_tests.py  == pytest