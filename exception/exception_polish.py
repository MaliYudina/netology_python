try:
    operator = input('Введите оператор: ')
    if operator != '-' or '+' or '*' or '/':
        operator = input('Введите оператор правильно: ')
    num1 = int(input('Введите первое положительное число: '))
    num2 = int(input('Введите второе положительное число: '))

    assert (num1 > 0), 'Необходимо ввести положительное число!'
    assert (num2 >= 0), 'Необходимо ввести положительное число!'

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
