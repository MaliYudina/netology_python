from pprint import pprint

RS = '|'
NAME = 0
QTY = 1
UNIT = 2


def parse_record(ingridients):
    vals = ingridients.split(RS)
    toget = {
        'ingridient_name': vals[NAME].strip(),
        'quantity': int(vals[QTY].strip()),
        'measure': vals[UNIT].strip(),
    }
    return toget


def get_shop_list_by_dishes(cbk, dishes, person_count):
    """
    список блюд из cook_book и количество персон для кого мы будем готовить
    """
    result_dict = {}

    for dish in dishes:
        for ingr in cbk[dish]:
            name = ingr['ingridient_name']
            if name in result_dict:
                result_dict[name]['quantity'] += ingr['quantity'] * person_count
            else:
                result_dict[name] = {
                    'measure': ingr['measure'],
                    'quantity': ingr['quantity'] * person_count,
                }
    return result_dict


def main():
    cookbook = {}
    current_name = None
    records_left = 0

    text_file = open('text')
    for line in text_file:
        line = line.strip()
        if line == '':
            continue

        if records_left != 0:
            records_left -= 1
            try:
                cookbook[current_name].append(parse_record(line))
            except KeyError:
                cookbook[current_name] = [parse_record(line)]
            continue

        if line.isnumeric():
            records_left = int(line)
        else:
            current_name = line

    pprint(
        get_shop_list_by_dishes(cookbook, ['Омлет', 'Фахитос'], 2))


if __name__ == '__main__':
    main()