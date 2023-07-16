# *Условие 3: *
# Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. 
# Удалите такие значения из списка и посчитайте суммарные затраты
# [100, 125, -90, 345, 655, -1, 0, 200]
# Используйте list comprehensions

my_list = [100, 125, -90, 345, 655, -1, 0, 200]

# def total_costs(data: list) -> list:
#     result = []
#     for i in range(len(data)):
#         if data[i] > 0:
#             result.append(data[i])
#     print(result)
#     all_costs = sum((result))
#     return all_costs

# print(f'Всего затрат: {total_costs(my_list)}')

# Используйте list comprehensions
new_list = [i for i in my_list if i > 0]
print(new_list)
all_costs = sum(new_list)
print(f'Всего затрат: {all_costs}')