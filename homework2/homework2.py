while True:
    try:
        num1 = input("Введите первое целое число (или 'exit' для выхода): ")
        if num1.lower() == "exit":
            print("Завершение программы.")
            break
        if not num1.isdigit() and not (num1.startswith('-') and num1[1:].isdigit()):
            raise ValueError("Ввод должен быть целым числом.")

        num2 = input("Введите второе целое число (или 'exit' для выхода): ")
        if num2.lower() == "exit":
            print("Завершение программы.")
            break
        if not num2.isdigit() and not (num2.startswith('-') and num2[1:].isdigit()):
            raise ValueError("Ввод должен быть целым числом.")

        num1 = int(num1)
        num2 = int(num2)
        print("Сумма:", num1 + num2)

    except ValueError as e:
        print("Ошибка ввода:", e)
