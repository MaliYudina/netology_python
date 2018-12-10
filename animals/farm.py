import animals

# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"

def work_with_geese(geese):
    for goose in geese:
        goose.feed()
        goose.pickeggs()
        goose.talk()


def work_with_cow(cow):
    for one_cow in cow:
        one_cow.feed()
        one_cow.milk()
        one_cow.talk()


def work_with_sheep(sheep):
    for one_sheep in sheep:
        one_sheep.feed()
        one_sheep.cut()
        one_sheep.talk()


def work_with_chicken(chicken):
    for one_chick in chicken:
        one_chick.feed()
        one_chick.pickeggs()
        one_chick.talk()


def work_with_goat(goat):
    for one_goat in goat:
        one_goat.feed()
        one_goat.milk()
        one_goat.talk()


def work_with_duck(duck):
    for one_duck in duck:
        one_duck.feed()
        one_duck.pickeggs()
        one_duck.talk()


duck_list = [animals.Duck('Kryakva', 5)]
goat_list = [animals.Goat('Roga', 46), animals.Goat('Kopyta', 34)]
chicken_list = [animals.Chicken('Ko-Ko', 1), animals.Chicken('Kukareku', 1.5)]
sheep_list = [animals.Sheep('Barashek', 50), animals.Sheep('Kudryaviy', 67)]
cow_list = [animals.Cow('Manka', 140)]
geese_list = [animals.Geese('Seryi', 3), animals.Geese('Belyi', 2.5)]


work_with_geese(geese_list)
work_with_cow(cow_list)
work_with_sheep(sheep_list)
work_with_chicken(chicken_list)
work_with_goat(goat_list)
work_with_duck(duck_list)


#добавляем для доработки ДЗ


animals_list = [cow_list, sheep_list, goat_list, geese_list, chicken_list, duck_list]

total_weight = 0
weights = []
for specie in animals_list:
    for animal in specie:
        weights.append(animal.weight)
print(
    'Самое тяжелое животное весит {}кг. Общий вес: {}кг.'.format(
        max(weights),
        sum(weights)))