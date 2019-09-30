import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
a = ["яблоко", "банан", "киви", "арбуз"]
max_len = 0
score= 0
for fruit in a:
    if len(fruit)> max_len:
        max_len = len(fruit)
for idx, fruit in enumerate(a,start = 1):
    print(f'{idx}. {fruit.rjust(max_len)}')
# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
a =[ random.randint(1,5) for c in range(1,7)]
b = [ random.randint(1,5) for c in range(1,7)]
i = 0
print (a)
print (b)
for c in range(len(a)):
    if a[c] in b:
         a[c] = None
a = [item for item in a if item != None]
print(a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
a =[ random.randint(1,5) for c in range(1,7)]
print (a)
for c in range(len(a)):
    if a[c]%2==0:
        a[c] /= 4
    else:
        a[c] *= 2
print (a)