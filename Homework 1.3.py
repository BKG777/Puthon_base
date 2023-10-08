# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код: from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Добро пожаловать в игру Угадай число от 1 до 1000!")
print(f"У вас есть {attempts} попыток.")
count = 10
for attempt in range(1, attempts + 1):
    guess = int(input("Попробуйте угадать число: "))

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
        break
    count -= 1
    print(f"Осталось {count} попыток \n")
else:
    print(f"Вы исчерпали все {attempts} попыток. Загаданное число было {secret_number}.")
