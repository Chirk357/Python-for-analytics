# *Условие 2: *
# На складе лежат разные фрукты в разном количестве.
# Нужно написать функцию, которая на вход принимает любое количество названий фруктов и их количество, 
# а возвращает общее количество фруктов на складе

def fruits(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(f'Всего: {sum(kwargs.values())}')
    
  
fruits(apple = 345, orange = 8, pear = 987)
print(fruits)