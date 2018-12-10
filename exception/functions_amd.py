# Расширить домашние задание из лекции 1.4 «Функции — использование
# встроенных и создание собственных» новой функцией, выводящей имена
# всех владельцев документов. С помощью исключения KeyError проверяйте,
# если поле “name” и документа.


DOCUMENTS = [
    {"type": "passport", "number": "2207 876234",},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

DIRECTORIES = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['12564675']
}


def name_failure(documents):
    for document in documents:
      try:
          print("Document №{} belongs to {}" .format(document["number"], document["name"]))
      except KeyError as key:
          print("Error: {} was not found.".format(key))


name_failure(DOCUMENTS)


def people():
    document_number_input = input("введите номер документа\n")
    for document in DOCUMENTS:
        for document_number in document.values():
            if document_number == document_number_input:
                return document['name']
    raise ValueError('Unable to find document by the given number')


def all_list():
    for dirs in DOCUMENTS:
        return dirs["type"], dirs["number"], dirs["name"]


def shelf():
    document_number_input = input("введите номер документа\n ")
    for shelf_number, doc_numbers in DIRECTORIES.items():
        if document_number_input in doc_numbers:
            return shelf_number
    raise ValueError('Shelf is not found')


def add_new():
    new_type = input("Введите тип нового документа\n")
    new_number = input("Введите номер нового документа\n")
    new_name = input("Введите имя владельца нового документа\n")
    new_shelf = input("Введите полку, где лежит новый документ\n")
    new_dict = {
        'type': new_type,
        'number': new_number,
        'name': new_name,
    }
    DOCUMENTS.append(new_dict)
    try:
        DIRECTORIES[new_shelf].append(new_number)
    except KeyError:
        DIRECTORIES[new_shelf] = [new_number]
    return list(DIRECTORIES.values())


def user_command():
    user_command_input = input(
        "Введите вашу команду\np - вывести владельца документа\n"
        "l - вывести все документы в формате № паспорта, Имя владельца\n"
        "s - вывести № полки хранения документов\n"
        "a - добавить новый документ\n")
    if user_command_input == "p":
        return people()
    if user_command_input == "l":
        return all_list()
    if user_command_input == "s":
        return shelf()
    if user_command_input == "a":
        return add_new()
    raise ValueError('Unknown command')


while True:
    try:
        print(user_command())
    except ValueError as err:
        print(err)