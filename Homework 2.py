# Задание 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def convert_namber_1(num_1):
    base = 16
    upper = False
    digits = '0123456789abcdef'
    result = ''
    while num_1 > 0:
        result = digits[num_1 % base] + result
        num_1 //= base
    return result.upper() if upper else result


# Перевод с помощью встроенной функции hex

def convert_namber_2(num_1):
    hex_str = hex(num_1)[2:]  # Преобразование в шестнадцатеричную строку и удаление префикса '0x'
    return hex_str


try:
    num_1 = int(input("Введите целое число: "))
    result_1 = convert_namber_1(num_1)
    result_2 = convert_namber_2(num_1)
    print(f"Шестнадцатеричное представление при вычислении: {result_1}")
    print(f"Шестнадцатеричное представление с встроенной функцией hex: {result_1}")

except ValueError:
    print("Пожалуйста, введите целое число.")

# Задание 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def namber_1(a1, b1, a2, b2):
    f1 = fractions.Fraction(a1, b1)
    f2 = fractions.Fraction(a2, b2)
    summ_1 = f1 + f2
    multiplication_1 = f1 * f2
    return print(f'Сумма чисел равна: {summ_1}\nПроизведение равно: {multiplication_1}')


try:
    a1, b1 = map(int, input("Введите 1ую дробь: a1/b1: ").split('/'))
    a2, b2 = map(int, input("Введите 1ую дробь: a2/b2: ").split('/'))
    print(namber_1(a1, b1, a2, b2))
except ValueError:
    print("Пожалуйста, введите дробь в формате: a/b.")
