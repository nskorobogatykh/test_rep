import random as r


# проверка на валидность ввода
def is_valid(n):
    while True:
        input_data = input(f"Введите число от 1 до {n}: ")
        if input_data.isdigit():
            num = int(input_data)
            if 1 <= num <= n + 1:
                return num
        print(f"А может быть все-таки введем целое число от 1 до {n}?")


# основная функция игры
def guess_the_number():
    print("Добро пожаловать в числовую угадайку!")
    print("Введите правую границу диапазона загадываемых чисел.")
    n = int(input())
    print(f"Я загадал число от 1 до {n}, попробуйте угадать его!")
    hidden_num = r.randint(1, n + 1)
    input_num = is_valid(n)
    attempt = 1  # счётчик попыток
    if input_num == hidden_num:
        print(f"Вы угадали, поздравляем! Количество ваших попыток - {attempt}")
    else:
        while input_num != hidden_num:
            if input_num < hidden_num:
                print(
                    f"Слишком мало, попробуйте еще раз. Ваше текущее число - {input_num}"
                )
                input_num = is_valid(n)
                attempt += 1
                continue
            else:
                print(
                    f"Слишком много, попробуйте еще раз. Ваше текущее число - {input_num}"
                )
                input_num = is_valid(n)
                attempt += 1
                continue
        print(
            f"Вы угадали, поздравляем! Загаданное число - {hidden_num}. Количество ваших попыток - {attempt}"
        )
    print("Спасибо за игру!")


guess_the_number()
