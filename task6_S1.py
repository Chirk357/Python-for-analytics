# Задание 6.
# Напишите функцию, которая может принимать любое
# количество трат пользователя и считать сумму и среднее.
# На вход поступают целочисленные значения в любом
# количестве
# На выходе словарь с ключами суммы трат и средней
# траты

def calc(*args):
    print(args) #находится кортеж, в круглых скобках
    sum_args = sum(args)
    count_args = len(args)
    avg_args = sum_args / count_args
    return {"сумма": sum_args, "среднее": avg_args}

print(calc(6, 2, 4))