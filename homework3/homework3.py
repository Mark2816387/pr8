size = 10  

while True:
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)  
        else:
            print("*" + " " * (size - 2) + "*") 

    answer = input("Нарисовать квадрат еще раз?(да/если нет введите любой символ, букву или число): ")
    if answer.lower() != "да":
        print("Завершение программы.")
        break
