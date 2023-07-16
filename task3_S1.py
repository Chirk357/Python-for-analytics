# 3.1 Напишите функцию с циклом for
# Извлеките только два ключа name и age из представленного словаря
# Функция на вход принимает: 
# -исходный словарь 
# -ключи, которые нужно извлечь (аргумент по умолчанию)
# На выходе словарь с нужными ключами Используйте аннотирование типов

# 3.2 Используя dict comprehensions


# 3.1 Напишите функцию с циклом for
client_dict = {
	"name": "John",
	"age": 25,
	"salary": 5000,
	"city": "Moscow"
}

def getKeys(dictionary: dict, keys: list=["name", "age"]) -> dict:
    result={}
    for k in keys:
        result[k] = dictionary[k]
    return result
    
print(getKeys(client_dict))

# 3.2 Используя dict comprehensions
# dict5 = {k: client_dict[k] for k in ["name", "age"]} #добываем значение из client dict.

# print(dict5)