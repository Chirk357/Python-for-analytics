# # Задание 1.
# 1.1 Соедините два словаря в один
# dict1 = {'One': 1, 'Two': 2, 'Three': 3}
# dict2 = {'Four': 4, 'Five': 5, 'Six': 6}

# 1.2 Напишите функцию, которая на вход принимает два словаря и возвращает один объединенный словарь
# Используйте аннотирование типов

# Задание 1.
# способ1
dict1 = {'One': 1, 'Two': 2, 'Three': 3}
dict2 = {'Four': 4, 'Five': 5, 'Six': 6}

# dict1.update(dict2)
# dict1

# dict1 = {'One': 1, 'Two': 2, 'Three': 3}
# dict2 = {'Four': 4, 'Five': 5, 'Six': 6}
# dict1

# заменяет исходный словарь

# способ2
# for key, value in dict2.items():
#     dict1[key] = value
# print(dict1)

# способ 3
# dict3 = {**dict1, **dict2}
# print(dict3)

# способ 4
# dict3 = dict1 | dict2
# print(dict3)

# 1.2 
def dictOne(d1: dict, d2: dict) -> dict:
    return d1 | d2
dictOne(dict1, dict2)





