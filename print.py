# # # # # # # # # # # # # # # # # # # # # # # # print("hello")
# # # # # # # # # # # # # # # # # # # # # # # # m=2
# # # # # # # # # # # # # # # # # # # # # # # # n=4
# # # # # # # # # # # # # # # # # # # # # # # # print(m+n)
# # # # # # # # # # # # # # # # # # # # # # # # print(m*n)


# # # # # # # # # # # # # # # # # # # # # # # # Переменные - Variable
# # # # # # # # # # # # # # # # # # # # # # # hello = 245
# # # # # # # # # # # # # # # # # # # # # # # first = 43
# # # # # # # # # # # # # # # # # # # # # # # first = 'hello bilol'
# # # # # # # # # # # # # # # # # # # # # # # print(first+hello)

# # # # # # # # # # # # # # # # # # # # # # name = "John"
# # # # # # # # # # # # # # # # # # # # # # surname = "Doe"
# # # # # # # # # # # # # # # # # # # # # # name +surname
# # # # # # # # # # # # # # # # # # # # # # print(name + " " + surname)
# # # # # # # # # # # # # # # # # # # # # # name = 'Mark'
# # # # # # # # # # # # # # # # # # # # # # surname = 'Twain'
# # # # # # # # # # # # # # # # # # # # # # print(name + " " + surname)
 

# # # # # # # # # # # # # # # # # # # # #  #Типы данных
# # # # # # # # # # # # # # # # # # # # #  integer - 1, 300, 34875
# # # # # # # # # # # # # # # # # # # # #  float - 1.4 , 3.7
# # # # # # # # # # # # # # # # # # # # #  string - 'rating'
# # # # # # # # # # # # # # # # # # # # #  bool - True, False

# # # # # # # # # # # # # # # # # # # # one = 1
# # # # # # # # # # # # # # # # # # # # two = 1.354
# # # # # # # # # # # # # # # # # # # # third = "hello person"
# # # # # # # # # # # # # # # # # # # # four = True
# # # # # # # # # # # # # # # # # # # # print(type(two))
# # # # # # # # # # # # # # # # # # # num1, num2, num3 = 1, 2, 3
# # # # # # # # # # # # # # # # # # # num1

# # # # # # # # # # # # # # # # # # num1 = 10
# # # # # # # # # # # # # # # # # # num2 = 20
# # # # # # # # # # # # # # # # # # num1, num2 = num2, num1
# # # # # # # # # # # # # # # # # # print(num1)


# # # # # # # # # # # # # # # # # name = "John"   #  двойные кавычки
# # # # # # # # # # # # # # # # # surname = 'Natasha she\'s \nbeautiful boy'  #  используем одинарные кавычки
# # # # # # # # # # # # # # # # # bio = """
# # # # # # # # # # # # # # # # # John Nash is a talented Python developer.
# # # # # # # # # # # # # # # # # He works at Google.
# # # # # # # # # # # # # # # # # """
# # # # # # # # # # # # # # # # # print(surname)


# # # # # # # # # # # # # # # # # name = 'John'
# # # # # # # # # # # # # # # # # surname = 'Nash'
# # # # # # # # # # # # # # # # # company = 'Google'
# # # # # # # # # # # # # # # # # bio = """
# # # # # # # # # # # # # # # # # {1} {0}  is a talented Python developer.
# # # # # # # # # # # # # # # # # He works at {0}.
# # # # # # # # # # # # # # # # # """.format(name, surname, company)

# # # # # # # # # # # # # # # # # print(bio)

# # # # # # # # # # # # # # # # name = 'John'
# # # # # # # # # # # # # # # # surname = 'Nash'
# # # # # # # # # # # # # # # # company = 'Google'
# # # # # # # # # # # # # # # # bio = f"{name} {surname} is a talented Python developer. \nHe works at {company}"
# # # # # # # # # # # # # # # # print(bio)


# # # # # # # # # # # # # # # name = input("Ваше имя: ")
# # # # # # # # # # # # # # # age = int(input("Возраст? "))
# # # # # # # # # # # # # # # print("Добро Пожаловать "+name,"!", "Вам" ,+age)

# # # # # # # # # # # # # # bio = 'John Nash'
# # # # # # # # # # # # # # print(bio)

# # # # # # # # # # # # # a = 'Python'
# # # # # # # # # # # # # print(a[3])

# # # # # # # # # # # # b = 'birthday cake'
# # # # # # # # # # # # print(b[:4])
# # # # # # # # # # # # print(b[4:])
# # # # # # # # # # # # print(b[-3])
# # # # # # # # # # # # print(b[::2])

# # # # # # # # # # # name = 'Vasya'
# # # # # # # # # # # # print ("My name is %s" % (name))

# # # # # # # # # # # print ("My name is %10s. That's my name." % (name))

# # # # # # # # # # s='hello world'
# # # # # # # # # # print (s[6])

# # # # # # # # # s='hello world'
# # # # # # # # # print(s [:4]+'a'+s[5:])

# # # # # # # # #methods

# # # # # # # # # print('hello'.upper())
# # # # # # # # # print('hello123$'.upper())
# # # # # # # # # print('hello'.lower())
# # # # # # # from this import d


# # # # # # # s='hello world'
# # # # # # # # print(s.count('o'))
# # # # # # # # print(s.count('o',7))


# # # # # # # # print(s.find('o'))

# # # # # # # # print(s.rfind('h'))

# # # # # # # # print(s.index('e'))

# # # # # # # # print(s.replace('o', 'ALI'))
# # # # # # # # print(s.replace('l', ''))
# # # # # # # # print(s.replace(' ', ''))
# # # # # # # # print(s.replace('l','',2))
# # # # # # # # print(s.isalpha())
# # # # # # # # print('1213'.isdigit())
# # # # # # # # print('121 3'.isdigit())

# # # # # # # d='111'
# # # # # # # print(d.rjust(5))
# # # # # # # print(d.rjust(5,'1'))
# # # # # # # print(d.rjust(5,'-'))

# # # # # # w='azimov bilol bahadyrovich'
# # # # # # print(w.split())
# # # # # # print (len(w.split()))
# # # # # # print(w.split('i'))
# # # # # # print('454, 8786, 4545,122'.split('4'))


# # # # # #условия

# # # # # if 2>11:
# # # # #     print('Верно')
# # # # # elif 23 > 18:
# # # # #     print('DSADASD')
# # # # # else: 
# # # # #     print('Неверно')    



# # # # age = int(input("Возраст:"))
# # # # if age <17:
# # # #     print("Ты малыш")
# # # # elif age >= 18 and age < 40:
# # # #     primt('Иди служить')
# # # # elif age >= 40 and anumber_int=int(673.3123)
# print(number_int)
# number_float=(512)
# print(number_float)
# number=int(float(str(192)))
# print(number)
# number_abc=float(173) + 5
# print(number_abc)
# number_str=193.00000000001
# print(number_str)


# bilol_str = "Calling"
# bilol_int = 911
# print(bilol_str + str(bilol_int))
# a='abc'
# b='xyz'
# print(f"Будет это: {a + b}")


# a = 589
# b=932.901
# c='Hello World'
# d='892.01'

# print(f"Будет это: {a + b}, мы тут соединяем цифры")
# print(f"Будет это: {c + d} , мы тут соединяем строки ")
# print(f"Будет это: {b + a}, мы тут соединяем цифры")
# print(f"Будет это: {d + c} , мы тут соединяем строки ")


# a, b, c, d = c, a, d, b
# print(a+str(b)+" "+ c + str(d))
# # # else:
# # #     print('Нечетный')

# number_int=int(673.3123)rfr cvtifnm cnhjrb d pytho
# print(number_int)
# number_float=(512)
# print(number_float)
# number=int(float(str(192)))
# print(number)
# number_abc=float(173) + 5
# print(number_abc)
# number_str=193.00000000001
# print(number_str)


# bilol_str = "Calling"
# bilol_int = 911
# print(bilol_str + str(bilol_int))
# a='abc'
# b='xyz'
# print(f"Будет это: {a + b}")


# a = 589
# b=932.901
# c='Hello World'
# d='892.01'

# print(f"Будет это: {a + b}, мы тут соединяем цифры")
# print(f"Будет это: {c + d} , мы тут соединяем строки ")
# print(f"Будет это: {b + a}, мы тут соединяем цифры")
# print(f"Будет это: {d + c} , мы тут соединяем строки ")


# a, b, c, d = c, a, d, b
# print(a+str(b)+" "+ c + str(d))


# a = 'одинарные'
# b = ""




# my_list = [1,2,3, True, "stringsd", 1.45]
# my_list.insert(4,'Привет')
# print(my_list)

# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# list_2  =  ['шесть',  'семь']
# my_list.extend(list_2)
# print(my_list)



# my_list = ['cde', '3', 'abc', 'klm', 'opq'] 
# list_2 = [3, 5, 2, 4, 1]
# my_list.sort()
# list_2.sort()
# print(my_list)
# print(list_2)



# contact_name = ['Aidana','Aziret', 'Almaz', 'baha','jaka', 'maga']
# contact = input('введи имя: ')
# contact = contact.title()
# if contact in contact_name:
#     print('В списке есть такой контакт')
# else:
#     print('В списке нет такого контакта')

# for name in contact_name:
#     print(name+'ALI')


# a = [1, 3, 4, 5] 
# b = [4, 5, 6, 7]

# for x in a:
#    for y in b:
#       if x == y:
#          b.remove(y)
# print(b)




# for i in range(10):
#     print('bilol')


# #while
# i = 10
# while i != 0:
#     print('aziret')
#     i -= 1


# list - spiski -[1,2,3,'strr', True] #изменяемые
# tuple - kortji - (1,2,3, 'strt', True)#НЕизменяемые
# dict - slovari - {1:2 3:'strt'}#изменяемые
# set - mnojestva - {3,3,4,5,3,5,4}#изменяемые, ХРАНИТ ТОЛЬКО УНИКАЛЬНЫЕ ЗНАЧЕНИЯ(не одинаковые)
 



# student = {1:'Aziret', 'age':55}
# stud2 = dict(name="Aziret2", age=56)
# student[1]='Radik'
# print(student[1])


# contact_name = {"Aidana":7718787877, 'Aziret': 3432342342, 'Almaz':212121212, 'Baha': 77787787, 'Jaka':223331212, 'Maga':78788898089}
# while True:
#     command = input("1 - добавляем новый контакт \n 2 - удаляем контакт \n 3 - поиск контакта \n 4 - просмотр \n")
#     if command == '1':
#         add_name = input("Введи имя: ")
#         add_number = int(input("Номер: "))
#         contact_name.items()
#         print(f"Контакт {add_name} успешно добавлен")
#     elif command == '2':
#         delete_cont = input("Какой контакт хотите удалить:")
#         if delete_cont in contact_name:
#             contact_name.pop(delete_cont)
#             print("Контакт успешно удалён")
#         else:
#             print("Такого контакта нет")
#     elif command == '3':
#         find_name = input("Какой контакт хотите найти? ")
#         title_find = find_name.title()
#         if title_find in contact_name:
#             print("Контакт найден")
#             print(contact_name[title_find])
#         else:
#             print("Контакт не найден")
#     elif command == '4':
#         print(contact_name)
#     else:
#         print("Неверная команда")

























































# contact_name = {"Aidana":7718787877, 'Aziret': 3432342342, 'Almaz':212121212, 'Baha': 77787787, 'Jaka':223331212, 'Maga':78788898089}


# while True:
#     command = input("1 - добавляем новый контакт \n 2 - удаляем контакт \n 3 - поиск контакта \n 4 - просмотр \n:" )

#     if command == '1':
#         add_name = input("Введи имя: ")
#         add_number = int(input("Введи Номер:  "))
#         contact_name[add_name] = add_number
#         print(f'Контакт {add_name} был добавлен')
#         print(contact_name)
#     elif command == '2':
#         delete_contacts = input("Напишите имя для Удаления:  ")
#         contact_name.pop(delete_contacts)
#         print('Контакт был успешно удалён', contact_name)
#     elif command == '3':
#         search_contact = input('Поиск контакта: ')
#         if search_contact in contact_name:
#             print('Контакт {search_contact} успешно найден его номер {contact_name.get(search_contact)}\n')
#     elif command == '4':
#         print(contact_name)
#     if command > '5':
#         print("Проверьте правильность данных")


# contact_name = {
#     'Jeka': 771231231,
#     'Bilol': 712321312,
# }




# while True:
#     print('Добавить контакт-1,\nУдалить контакт-2,\nПоиск-контакта-3,\nПросмотр контакта-4,\nДля выхода - 5\n')
#     enter_value = int(input(': '))
#     if enter_value == 1:
#         name = input('Name: ').title()
#         number = input('Number: ')
#         contact_name[name] = number
#         print(f'Контакт {name} был успешно добавлен \n')
#         print(contact_name)
#     elif enter_value == 2:
#         print(f'Все контакты {contact_name}')
#         delete_contact = input('Enter name to delete: ').title()
#         contact_name.pop(delete_contact)
#         print(f'Пользоваьтель {delete_contact} успешно удален\n', contact_name)
#     elif enter_value == 3:
#         search_contact = input('Поиск контакта: ').title()
#         if search_contact in contact_name:
#             print(f'Контакт {search_contact} успешно найден его номер {contact_name.get(search_contact)}\n')
#     elif enter_value == 4:
#         search_contact = input('Кого хотите просмотреть: ').title()
#         print(f'Данные контакта {search_contact}: {contact_name.get(search_contact)}\n')
#     elif enter_value == 5:
#         Bilol = False
#     else:
#         print('Проверьте правильность данных\n')



all_books = 20
history = int(all_books / 100 * 5)
chemistry = int(all_books / 100 * 25)
physics = int(all_books / 100 * 35)
 
print(f'history: {history}, chemistry: {chemistry}, physics: {physics}')

































