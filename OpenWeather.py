import requests as rq

user_input = input('Название города (eng): ')
api_key = input('Ваш api ключ: ')

params = {
    'q' : user_input.lower(),
    'appid' : api_key,
    'units' : 'metric',
    'lang' : 'ru',
}

get_url = rq.get('https://api.openweathermap.org/data/2.5/weather', params=params, timeout=30)

if get_url.status_code == 200:
    data = get_url.json()
    try:
        print(f'''{data['name']}, {data['sys']['country']}
{'=' * 30}
{'Погода: ':<12} {data['weather'][0]['description']}
{'Координаты: ':<12} {data['coord']['lat']} {data['coord']['lon']} 
{'Температура: ':<12} {data['main']['temp']}℃
{'Влажность: ':<12} {data['main']['humidity']}%
{'Ветер: ':<12} {data['wind']['speed']} м/с
''')
    except KeyError:
        print('Неверное значение!')
else:
    print('Error', get_url.status_code)