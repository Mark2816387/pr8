while True:
    try:
        a = input("Введите первое целое число a: ")
        if not a.isdigit() and not (a.startswith('-') and a[1:].isdigit()):
            raise ValueError("Ввод должен быть целым числом.")
        a = int(a)

        b = input("Введите второе целое число b: ")
        if not b.isdigit() and not (b.startswith('-') and b[1:].isdigit()):
            raise ValueError("Ввод должен быть целым числом.")
        b = int(b)

        if a < b:
            for i in range(a + 1, b):
                print(i, end=" ")
        elif a > b:
            for i in range(b + 1, a):
                print(i, end=" ")
        else:
            print("Числа a и b равны, между ними нет целых чисел.")

        print("\n") 
        break

    except ValueError as e:
        print("Ошибка ввода:", e)
