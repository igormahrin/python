# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

 def my_round(number, ndigits):



 print(my_round(2.1234567, 5))
 print(my_round(2.1999967, 5))
 print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
# a = "не корректный билет"
# b = "удача!"
# g = 'не удача'
# def sum_m(x):
#     while x < 0:
#         b = 0
#         c = x %10
#         b+=c
#         x//=10
#         return b
# def lucky_ticket(ticket_number):
#     if ticket_number < 99999 or ticket_number > 999999 :
#
#         return a
#     else:
#         ticket_number = str(ticket_number)
#         str1 = int(ticket_number[0:2])
#         str2 = int(ticket_number[3:5])
#     sum_m(str1)
#     sum_m(str2)
#     if str1 == str2:
#         return b
#     else:
#         return g
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
