# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def chek_tranglie(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print('Треуголника с отрициательными сторонами не существует')
    elif a >= b + c or b >= a + c or c >= a + b:
        print('Трегуольник с такими сторонами не существует')
    elif a == b and b == c:
        print('Это равносторонний треугольник')
    elif a == b or a == c or b == c:
        print('Это равнобедренный треуголник')
    else:
        print('Это разносторонний треугольник')
try:
    a = int(input('Введите 1уюс торону треугольника: '))
    b = int(input('Введите 2ую торону треугольника: '))
    c = int(input('Введите 3ую торону треугольника: '))

    result = chek_tranglie(a, b, c)
    print(result)
except ValueError:
    print("Пожалуйста, введите числовые значения для сторон треугольника.")