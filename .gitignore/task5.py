# a = float(input("1:  "))
# b = float(input("2:  "))
# def calc(a, b):
    
#     operation = input("1.+\n2.-\n3.*\n4./\n\n")
#     if operation == "1":
#         print(a, '+', b, '=', (a + b))
#     elif operation == "2":
#         print(a, '-', b, '=', (a - b))
#     elif operation == "3":
#         print(a, '*', b, '=', (a * b))
#     elif operation == "4":
#         try:
#             print(a, '/', b, '=', (a / b))
#         except ZeroDivisionError:
#             print("We can't divide to 0")  
#     else:
#         print("ERRRRROOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRR")
    
# calc(a, b)

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# def is_year_leap():
#     year = int(input('Введите год: '))

#     if year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False

# print(is_year_leap())


# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def square():


#     storona = float(input('Введите сторону квадрата: '))
#     perimeter = int(storona * 4)
#     ploshad = storona * storona #S = a × a
#     diagonal = (storona + storona) ** (1 / 2) #2*площадь(квадратный корень)

#     return [perimeter, ploshad, diagonal]

# print(square())

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def bank(money,years):
#     return ((0.1 * money) * years) + money #10% это 0.1
# money = int(input('Введите сумму денег: '))
# years = int(input('Введите год: '))
# print(bank(money,years))

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def is_prime(qwe):
#     if qwe > 1000:
#         return
#     if qwe % 2 == 0:
#         print("False")
#         return
#     else:
#         print("True")
# qwe = int(input("Введите число от 1 до 1000\n"))
# is_prime(qwe)

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def date(day,month,year):
#     if day <30:
#         return True
    
#     if month <12:
#         return True
    
#     if year <2022:
#         return True
    
#     else:
#         return False



# day = int(input("введи день: "))
# month = int(input('Введите месяц: '))
# year = int(input('Введите год: '))

# print(date(day,month,year))


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# lst = input().split()
# count = []
# for i in lst:
#     counts=lst.count(i)
#     if f"{i}:{counts}" not in count:
#      count.append(f"{i}:{counts}")
# print("\n".join(count))

#/////////////////////////////////////////////////////