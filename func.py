# # def Hello():
# #     print('Hello americans')

# # def Buy():
# #     print('Hello NIGGERS')

# # Buy()
# # Hello()

# # def Hello2(mes):
# #     print("Hello ", mes)

# # Hello2(input("Введите текст"))

# # a = int(input("Введите Число:  "))
# # abs(a)
# # print(-a)



# # def ngrs (a):
# #     if a > 0:
# #         return True
# #     else:
# #         return False




# # a = [2, 4,  -4, -323, 323, -32, 12, -4, 12]
# # p = []
# # for i in a:
# #     if ngrs(i):
# #         p.append(i)
# # print(p)



# # a=int(input(":"))
# # b=int(input(":"))
# # def sum(a, b):
# #    result = a + b
# #    return result
# # print(a+b)

# def addition(x, y):
#    return x + y


# def subtraction(x, y):
#    return x - y

# def multiplication(x, y):
#    return x * y


# def division(x, y):
#    return x / y


# print("""Выберите: """)
# print("1. Плюс")
# print("2. Минус")
# print("3. Умножение")
# print("4. Деление")

# choice = input("Твой выбор:  ")

# num1 = int(input("Первая цифра: "))
# num2 = int(input("Вторая цифра: "))



# if choice == '1':
#    print(num1, "+" ,num2, "=", addition(num1, num2))

# elif choice == '2':
#    print(num1, "-", num2, "=", subtraction(num1, num2))

# elif choice == '3':
#    print(num1, "*", num2, "=", multiplication(num1, num2))

# elif choice == '4':
#    print(num1, "/", num2, "=", division(num1, num2))

# else:
#    print("Проверьте на правильность написания")



lst = input().split()
count = []
for i in lst:
    counts=lst.count(i)
    if f"{i}:{counts}" not in count:
     count.append(f"{i}:{counts}")
print("\n".join(count))