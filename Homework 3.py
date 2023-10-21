# Условие
# 1. Решить задачи, которые не успели решить на семинаре.

# 2. Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import string
from collections import Counter
import itertools
from itertools import islice

list_2 = [1, 1, 2, 2, 2, 'b', 'b', 5, 6, 7, 7, 7]
# Вариант 1
new_dict_2 = Counter(list_2)
new_list_2_1 = set()
for i in list_2:
    if new_dict_2[i] >= 2:
        if i not in new_list_2_1:
            new_list_2_1.add(i)
print(f'Входной список: {list_2}', type(list_2))
print(f'Словарь: {new_dict_2}', type(new_dict_2))
print('Символы встречающиеся более 1го раза:')
print(f'Вариант 1. {new_list_2_1}', type(new_list_2_1))

# Вариант 2 (похож на предыдущий)
new_dict_2_1 = Counter(list_2)
new_list_2_2 = [i for i in new_dict_2_1 if new_dict_2_1[i] >= 2]
print(f'Вариант 2. {new_list_2_2}', type(new_list_2_2))

# Вариант 3 (длинный путь)
new_list_2_3 = [i for i in set(list_2) if list_2.count(i) >= 2]
print(f'Вариант 3. {new_list_2_3}', type(new_list_2_3))
print('')

# 3. В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text_3 = '1. Списки, list. List, список является самой часто используемой коллекцией в Python. Прежде чем ' \
         'говорить о списках, я напомню, что такое массив в информатике. Массив - это ' \
         'непрерывная область в оперативной памяти компьютера, поделённая на ячейки ' \
         'одинакового размера хранящие данные одного типа. Массивы могут быть ' \
         'статическими, то есть размер массива нельзя изменить, и динамическими, когда ' \
         'размер массива изменяется при добавлении или удалении элементов. Один из ' \
         'самых больших плюсов в работе с массивами - это доступ к любой из его ячеек за ' \
         'константное время. ' \
         'Массив — упорядоченный набор элементов, каждый из которых хранит одно ' \
         'значение, идентифицируемое с помощью одного или нескольких индексов. В ' \
         'простейшем случае массив имеет постоянную длину и хранит единицы данных ' \
         'одного и того же типа, а в качестве индексов выступают целые числа. ' \
         'В информатике, список (англ. list) — это абстрактный тип данных, представляющий ' \
         'собой упорядоченный набор значений, в котором некоторое значение может ' \
         'встречаться более одного раза. Экземпляр списка является компьютерной ' \
         'реализацией математического понятия конечной последовательности. Экземпляры ' \
         'значений, находящихся в списке, называются элементами списка (англ. item, entry ' \
         'либо element); если значение встречается несколько раз, каждое вхождение ' \
         'считается отдельным элементом. '
# Заменим знаки пунктуации на пусто и разделим текст на слова.
new_text_3 = ''.join((el if el not in string.punctuation else '' for el in text_3))
# print(new_text_3)
# Сделаем список. Разделим текст на слова по пробелу.
new_text_3_1 = new_text_3.split()
# print(new_text_3_1)
# print(set(new_text_3))
# Сделаем словарь из списка по имени и количеству повторов.
new_dict_3 = Counter(new_text_3_1)
print(type(new_dict_3), new_dict_3)
# При этом он автоматически его сортирует, но можно прописать сортировку
new_dict_3_1 = dict(sorted(new_dict_3.items(), key=lambda x: x[1], reverse=True))
print(type(new_dict_3_1), new_dict_3_1)
# new_dict_3_2 = sorted(new_dict_3.items(), key=lambda x: x[1], reverse=True)
# print(type(new_dict_3_2), new_dict_3_2)
# Выберем первые 10 значений словаря
new_dict_3_10 = dict(list(new_dict_3_1.items())[:10])
print(f'Вариант 1: {new_dict_3_10}')
print('Вариант 2:')
i = 0
for key, value in new_dict_3_10.items():
    i += 1
    print(f'{i:<2}. {key:>10} = {value}')

# 4. Создайте словарь со списком вещей для похода в качестве ключа и
# их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things_4 = {
    "термос": 1.0,
    "спички": 0.01,
    "топор": 1.5,
    "нож": 0.4,
    "компас": 0.1,
    "повер_банк": 0.5,
    "палатка": 2.0,
    "сменка": 1.1,
    "кастрюля": 0.5,
    "вода": 1.5,
}
# Можно прописать сортировку от меньшего веса до большего
things_4_sort = dict(sorted(things_4.items(), key=lambda x: x[1], reverse=False))
print(f'Отсортированный список по весу: {things_4_sort}')
max_weight = int(input('Введите максимальный грузоподьемность рюкзака от 1 до 7: '))
weight_1 = 0
weight_2 = 0
i = 1
# print(f'При максимальном весе= {max_weight:.1f}')
print(f'{"№":<2}. {"Имя":<10} {"Масса":<5} {"Нак.Масса"}')
for key, value in things_4_sort.items():
    if weight_1 <= max_weight:
        print(f'{i:<2}. {key:>10}= {value:<5} {weight_1:.1f}')
    else:
        break
    weight_2 = weight_1
    weight_1 += value
    i += 1
print(
    f'Итого вместилось {i - 1} предметов с суммарным весом: {weight_2:.1f} не превышающие грузоподьемность рюкзака: {max_weight:.1f}')

print('\n Вариант с *Верните все возможные варианты комплектации рюкзака')
import itertools


def compbination_things_4(things_4, max_weight):
    val_compinations = []
    for r in range(1, len(things_4) + 1):
        for combination in itertools.combinations(things_4, r):
            combination_weight = sum(things_4[1] for things_4 in combination)
            if combination_weight <= max_weight:
                val_compinations.append([things_4[0:2] for things_4 in combination])
    return val_compinations


i = 1
possible_combinations = compbination_things_4(list(things_4.items()), max_weight)
for combination in possible_combinations:
    print(
        f'Комбинация № {i:>2}. Общая масса: {round(float(sum((dict(combination)).values())), 2):<5} {dict(combination)}')
    i += 1
