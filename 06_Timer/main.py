import re, time

watch = {'hours': 0, 'minutes': 0, 'seconds': 0,}

def get_time(h, m, s):
    return h * 3600 + m * 60 + s

def watch_go():
    watch['seconds'] += 1
    if watch['seconds'] >= 60:
        watch['seconds'] = 0
        watch['minutes'] += 1
        if watch['minutes'] >= 60:
            watch['minutes'] = 0
            watch['hours'] += 1

user_input = input('Задайте таймер h,m,s: ')
numbers = re.split(r'[\s,:]+', user_input.strip())
try:
    n_tuple = tuple(int(x) for x in numbers if x)
    if len(n_tuple) != 3:
        raise ValueError('Неверный формат таймера!')
    if n_tuple[0] > 99 or n_tuple[1] >= 60 or n_tuple[2] >= 60:
        raise ValueError('Значения слишком большие!')
except ValueError as e:
    print(f'Ошибка ввода: {e}')
else:
    target_time = get_time(*n_tuple)
    current_time = 0

    time_str = f'{watch["hours"]:02d}:{watch["minutes"]:02d}:{watch["seconds"]:02d}'
    print(time_str, end='\r', flush=True)

    while target_time > current_time:
        current_time = get_time(watch['hours'], watch['minutes'], watch['seconds'])
        time_str = f'{watch["hours"]:02d}:{watch["minutes"]:02d}:{watch["seconds"]:02d}'
        print(f'\r\x1b[K{time_str}', end='', flush=True)
        time.sleep(1)
        watch_go()

    print('\nВремя вышло!')