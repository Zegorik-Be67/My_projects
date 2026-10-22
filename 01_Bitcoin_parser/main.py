import requests as rq

cripto = input('Какая крипта?: ').lower().strip()

params = {
    'vs_currencies': 'usd',
    'ids': cripto,
}

get_url = rq.get('https://api.coingecko.com/api/v3/simple/price', params = params)

if get_url.status_code == 200:
    data = get_url.json()
    try:
        print(f'{cripto.title()}: {data[cripto]['usd']} USD')
    except KeyError:
        print('Неверное значение!')
else:
    print(f'error {get_url.status_code}')