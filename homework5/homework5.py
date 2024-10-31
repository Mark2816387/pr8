total_sum = 0  

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")

    if user_input.lower() in ["stop", "end"]:
        print("Сумма введенных чисел:", total_sum)
        break

    try:
        if user_input.count(",") > 1 or any(c.isalpha() for c in user_input.replace(",", "")):
            raise ValueError("Ввод должен содержать только цифры, запятую, точку(для не целого числа) или знак минуса.")

        number = float(user_input.replace(",", "."))
        total_sum += number  

    except ValueError as e:
        print("Ошибка ввода:", e)
