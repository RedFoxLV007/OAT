import argparse

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Пример использования argparse')

    # Добавляем аргументы
    parser.add_argument('--name', type=str, default='Мир', help='Приветственное сообщение с именем')
    parser.add_argument('--doublestr', type=str, help='удвоение строки')

    # Парсим аргументы
    args = parser.parse_args()

    # Используем аргументы
    if args.name != 'Мир': # если задана пустая строка -> default
        print(f'Привет, {args.name}!')# --name -> args.name
    if args.doublestr != None:
        print(f'{args.doublestr}'*2)

if __name__ == '__main__':
    main()