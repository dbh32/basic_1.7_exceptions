def count():
    if action == '+':
        print(op1 + op2)
    elif action == '-':
        print(op1 - op2)
    elif action == '*':
        print(op1 * op2)
    else:
        try:
            print(op1 / op2)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
            return 'Ошибка'


def user_input():
    global action, op1, op2, num1, num2

    try:
        action, num1, num2 = input('Что считаем: ').split()
    except ValueError:
        print('Некорректный формат ввода!')
        return 'Ошибка'

    possible_actions = ['+', '-', '*', '/']
    assert action in possible_actions, 'Введена некорректная операция!'

    try:
        op1 = float(num1)
        op2 = float(num2)
    except TypeError:
        print('Введены некорректные операнды!')
        return 'Ошибка'
    else:
        count()

    assert op1 > 0 and op2 > 0, 'Введено отрицательное число!'


def main():
    while True:
        command = input('Считаем? Y/N ')
        if command == ('y' or 'Y'):
            user_input()
        elif command == ('n' or 'N'):
            print('До скорого!')
            break
        print()


print()
print('Формат ввода: "оператор операнд1 операнд2" '
      '(без кавычек)')
print()

if __name__ == "__main__":
    main()
