import requests

currency = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()

code = input().lower()
amount = float(input())

if currency != 'usd' and currency != 'eur':
    money_dict = {'usd': r['usd']['rate'], 'eur': r['eur']['rate']}     # code: r[code]['rate']

elif currency != 'usd' and currency == 'eur':
    money_dict = {'usd': r['usd']['rate']}

elif currency == 'usd' and currency != 'eur':
    money_dict = {'eur': r['eur']['rate']}

elif code == 'usd' and code != 'eur':
    money_dict = {'eur': r['eur']['rate']}

elif code != 'usd' and code == 'eur':
    money_dict = {'usd': r['usd']['rate']}

while True:
    total = round(amount * float(r[code]['rate']), 2)
    print('Checking the cache...')
    if code not in money_dict.keys():
        print('Sorry, but it is not in the cache!')
        print(f'You received {total} {code}.')
        money_dict[code] = r[code]['rate']
    else:
        print('Oh! It is in the cache!')
        print(f'You received {total} {code}.')
    code = input().lower()
    if not code:
        break
    amount = float(input())
