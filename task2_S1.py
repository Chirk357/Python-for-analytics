# Задание 2.
# Напишите функцию, которая из двух списков, делает один словарь, где
# элементы из первого списка - ключи, а элементы из второго списка -
# значения. Используя цикл for.
# 2.1 Используя цикл for
# 2.2 Используя dict comprehensions

keys = ['one', 'two', 'three']
values = [1, 2, 3]

# 2.1 Используя цикл for
def oneDictionary(k: list, v: list) -> dict:
    dictionary = {}
    for i in range(len(k)): 
        dictionary[k[i]] = v[i]
    return dictionary

print(oneDictionary(keys, values))

## 2.2 Используя dict comprehensions
# newDict = {keys[i]: values[i] for i in range(len(keys))}
# print(newDict)



