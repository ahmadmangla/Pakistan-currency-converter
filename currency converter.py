currency = {'AUD': 116, 'BHD': 386.7, 'CAD': 125, 'CNY': 23.5, 'DKK': 23.2, 'EUR': 187.5, 'GBP': 222, 'USD': 161.2}
print('Welcome to the Pakistan currency converter\n')
print('Currently these currencies are avalaible : ')
i = 0

print(currency.keys())
user_inp = int(input('Please enter the amount you have: '))
user_cur = input('Please enter the currency you want to convert your amount in: ')

cur_store = 0

if user_cur == 'AUD':
    cur_store = user_inp / currency['AUD']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'BHD':
    cur_store = user_inp / currency['BHD']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'CAD':
    cur_store = user_inp / currency['CAD']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'CNY':
    cur_store = user_inp / currency['CNY']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'DKK':
    cur_store = user_inp / currency['DKK']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'EUR':
    cur_store = user_inp / currency['EUR']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'GBP':
    cur_store = user_inp / currency['GBP']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

elif user_cur == 'USD':
    cur_store = user_inp / currency['USD']
    store = f'For {user_inp}PKR you will get {cur_store} {user_cur}'
    print(store)

else:
    print('Invalid input!')









