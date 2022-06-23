# Практическое задание №1

# Пункт №1

# a = 1
# b = 2
# c = 3
# print(a+b+c)
#
# a = str("  ")
# name = input('name: ')
# sname = input('surname: ')
# age = input('age: ')
# print(name + a + sname + a + age)

# Пункт №2

# time = input('seconds: ')
# time = int(time)
# hours = (time // 3600)
# #print(hours)
# minutes = (time % 3600)//60
# #print(minutes)
# seconds = (time % 3600)%60
# #print(seconds)
# print(hours, ':', minutes, ':', seconds)

# #Пункт №3
# num1 = input('Please input number:' )
# num2 = str(num1 + num1)
# num3 = str(num1 + num1 + num1)
# #print(num3)
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# summ = int(num1 + num2 + num3)
# print(summ)

# #Пункт №4
#
# n = input('Введите любое число : ')
# n = int(n)
# res = 0
# nx = 0
# while n > 0:
#     last = n % 10 # последняя цифра
#     if last > nx:
#         nx = last
#     res = res + 1
#     n = n // 10 # целая часть
#
# print(nx)

# # Пункт №5
#
# vir = input('Введите выручку : ') #доход
# zat = input('Введите затраты : ') #расход
#
# vir = int(vir)
# zat = int(zat)
#
# if vir > zat:
#     print('Прибыль')
# elif vir < zat:
#     print('Убыток')

# Пункт №6

vir = input('Введите выручку : ') #доход
zat = input('Введите затраты : ') #расход

vir = int(vir)
zat = int(zat)
prib = vir - zat  #прибыль
rent = vir / prib #рентабельность
#print(rent)

pers = input('Количество сотрудников : ')
pers = int(pers)
pribpers = prib / pers  #количество прибыли на одного сотрудника
print(pribpers)

#the end:-)
