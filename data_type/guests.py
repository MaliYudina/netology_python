from pprint import pprint

persons = int(input('Количество гостей: '))
cook_book = {
    'салат':
        [
            ['картофель', 100, "гр"],
            ['морковь ', 50, "гр"],
            ['огурцы', 50, "гр"],
            ['горошек', 30, "гр"],
            ['майонез', 70, "гр"],
            ['руккола', 60, "гр"]
        ],
    'пицца':
        [
            ['сыр', 50, "гр"],
            ['томаты', 50, "гр"],
            ['тесто', 100, "гр"],
            ['бекон', 30, "гр"],
            ['колбаса', 30, "гр"],
            ['руккола', 60, "гр"],
            ['сахар', 10, "ст.л."]
        ],
    'фруктовый десерт':
        [
            ['хурма', 2, "шт"],
            ['киви', 60, "гр"],
            ['творог', 60, "гр"],
            ['сахар', 10, "ст.л."],
            ['мёд', 50, "ст.л."],
        ]
}

result = {}

for dish, ingridients in cook_book.items():
    for items in ingridients:
        veggie = items[0]
        weight = items[1]
        if veggie in result:
            result[veggie] = result[veggie] + weight * persons
        else:
            result[veggie] = weight * persons

print('Общий список на всех гостей:')
pprint(result)
