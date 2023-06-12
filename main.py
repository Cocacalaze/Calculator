def calculator():
    print("Калькулятор")
    try:
        while True:
            print("Выберите какое действие хотите сделать: + - * / ")
            n = input("Введите действие: ")
            if n == 'q':
                break
            if n in ('+','-','*','/'):
                a = int(input("Введите первое число: "))
                b = int(input("Введите второе число: "))

                if n == '+':
                    print(a+b)
                elif n == '-':
                    print(a-b)
                elif n == '*':
                    print(a*b)
                elif n == '/':
                    print(a/b)

    except ZeroDivisionError:
        print("На 0 делить нельзя!")

calculator()