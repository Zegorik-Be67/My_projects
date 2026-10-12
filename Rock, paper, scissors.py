import random

items = ['Камень','Ножницы','Бумага']

score = {
    'Player': 0,
    'Ai': 0,
    'Draw': 0,
}

def random_ai():
    return random.randint(0, 2)

while True:
    user_input = input('Ваш предмет: ').capitalize().strip()
    if user_input in items:
        user_index = items.index(user_input)
        ai_index = random_ai()
        if user_index == ai_index:
            score['Draw'] += 1
            print(f'{'='*20}\nТвой предмет: {user_input.capitalize()}\nМой предмет: {items[ai_index]}\nНичья!\n{'='*20}')
        elif (user_index == 0 and ai_index == 1) or (user_index == 1 and ai_index == 2) or (user_index == 2 and ai_index == 0):
            score['Player'] += 1
            print(f'{'='*20}\nТвой предмет: {user_input.capitalize()}\nМой предмет: {items[ai_index]}\nТы победил!\n{'='*20}')
        else:
            score['Ai'] += 1
            print(f'{'='*20}\nТвой предмет: {user_input.capitalize()}\nМой предмет: {items[ai_index]}\nТы проиграл!\n{'='*20}')
    elif user_input == '':
        print(f'{'='*20}\nИтоги:')
        for key, value in score.items():
            print(f'{key}: {value}')
        break
    else:
        print('Неправильный предмет!')