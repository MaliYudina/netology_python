try:
    polish = input('Введите аргументы в формате "*,47,5": ')

    arguments_list = polish.split(',') #to divide multi-digit values
    operator = arguments_list[0]
    num1 = int(arguments_list[1])
    num2 = int(arguments_list[2])
    accept_operators = ('-', '+', '*', '/')
    if operator not in accept_operators:
        operator = input('Введите оператор правильно: ')

    assert (num1 > 0), 'Необходимо ввести положительное число!'
    assert (num2 > 0), 'Необходимо ввести положительное число!'

    if operator == '-':
        print('Ответ:', num1 - num2)
    elif operator == '+':
        print('Ответ:', num1 + num2)
    elif operator == '*':
        print('Ответ:', num1 * num2)
    elif operator == '/':
        try:
            print('Ответ:', num1 / num2)
        except ZeroDivisionError:
            print('Ошибка деления на ноль!')
    else:
        print('Оператор не найден')
except ValueError:
    print('Ошибка ввода')
