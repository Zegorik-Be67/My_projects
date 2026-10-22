import string
import random

def new_file():
    with open(r'password.txt', 'a', encoding="utf-8") as f:
        pass

def get_valid_num():
    while True:
        num = input("Введите нужное кол-во символов: ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        else:
            print("Неверный номер!")

def get_random(num):
    random_password = string.ascii_letters + string.digits
    password = "".join(random.choices(random_password, k=num))
    print(password)
    return password

def get_random_password(num, password):
    while True:
        refresh = input('Заменить? (Да/Нет): ').lower()
        if refresh == "да":
            password = get_random(num)
        elif refresh == "нет":
            new_file()
            with open(r'password.txt', 'r', encoding="utf-8") as file_old:
                for line in file_old:
                    if password.lower() in line.strip().lower():
                        print('Такой пароль уже существует!')
                        break
                else:
                    for_what = input('Для чего этот пароль: ')
                    with open(r'password.txt', "a", encoding="utf-8") as file_new:
                        file_new.write(f'{for_what} : {password}\n')
                    print('Пароль записан!')
                    break
            break
        else:
            print("Такой команды нет!")

while True:
    start = input('Создать пароль? (Да/Нет): ').lower()
    if start == 'да':
        valid_num = get_valid_num()
        random_letters = get_random(valid_num)
        get_random_password(valid_num, random_letters)
    elif start == 'нет':
        break
    else:
        print('Неверная команда!')