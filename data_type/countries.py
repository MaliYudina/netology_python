budget = int(input('Введите ваш максимальный бюджет: '))
temp = int(input('Введите желаемую температуру курорта: '))

print(f'Наш бюджет: {budget} RUB \n Подбираем варианты путешествий...')

countries = {

    'Thailand': {'country_sea': True, 'country_schengen': False,
                 'exchange_rate': 2, 'temperature': 28, 'living_cost': 600},
    'Germany': {'country_sea': True, 'country_schengen': True,
                'exchange_rate': 70, 'temperature': 10, 'living_cost': 150},
    'Poland': {'country_sea': True, 'country_schengen': True,
               'exchange_rate': 70, 'temperature': 8, 'living_cost': 100},
    'Russia': {'country_sea': True, 'country_schengen': False,
               'exchange_rate': 1, 'temperature': 5, 'living_cost': 500},
    'France': {'country_sea': True, 'country_schengen': True,
               'exchange_rate': 70, 'temperature': 10, 'living_cost': 850},
    'Vietnam': {'country_sea': True, 'country_schengen': False,
                'exchange_rate': 3, 'temperature': 30, 'living_cost': 330},
    'UK': {'country_sea': True, 'country_schengen': False,
           'exchange_rate': 89, 'temperature': 7, 'living_cost': 1030},

}

print('Страны Шенгена: \nСтрана | Дней всего')

for country, data in countries.items():

    if data['country_schengen'] == True:
        if (data['exchange_rate'] * 7 * data['living_cost']) <= budget:
            print(country, '-', round(budget / data['living_cost']), ' дней')

print('Морские страны: \nСтрана | Дней всего')

for country, data in countries.items():

    if data['country_sea'] == True:
        if (data['exchange_rate'] * 10 * data['living_cost']) <= budget:
            if data['temperature'] >= temp:
                print(country, '-', round(budget / data['living_cost']), ' дней')
