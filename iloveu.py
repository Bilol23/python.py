# # # # i = 57
# # # # while i != 0:
# # # #     print('I LOVE PYTHON')
# # # #     i -= 1








# # # # a=1
# # # # while True:
# # # #     print('I LOVE PYTHON №', a )
# # # #     if a==57:
# # # #         break
# # # #     a+=1







# # # # for i in range(58):
# # # #     print('I LOVE PYTHON №',i)




# # # # a = 354
# # # # b = 1
# # # # while a >= b:
# # # #     if a % 2 == 1:
# # # #         print(a)
# # # #     a = a - 1
# # # #     continue




# # # # for i in range(23,88,8):
# # # #     print (i)



# # # # books = ['harry potпатрульter', 'sherlock holmes', 'idiot','illiada', 'never give up']

# # # # books_not_idiot = " "
# # # # for book in books:
# # # #     if "idiot" != book:
# # # #         books_not_idiot += book+"         "
# # # # print(books_not_idiot)








# # # # people = ['Regina', 'Erkayim', 'Begayim'] 
# # # # country = ['Germany', 'France','Spain', 'Portugal','Holland', 'Japan', 'South Korea', 'Singapore'] 
# # # # for person in people: 
# # # #     for countries in country: 
# # # #         print(f"{person}lives in {country}") 
 
 
 
 
 
# # # # password_list = ["password", "12 3456", "12345678", "qwerty", "abc123", "monkey", "1234567"] 
# # # # while True: 
# # # #     i = input("напиши пароль") 
# # # #     if i in password_list: 
# # # #         print("Доступ открыт") 
# # # #         break 
# # # #     else: 
# # # #         print("Не верный пароль")




# # # #str, int,float,bool, list dict tuple set 
# # # # animals = {'crocodil', 'crocodil','begemot'}
# # # # animals.add('dog')
# # # # print(animals)
# # # # for i in animals:
# # # #     print(i)


# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# a = (set(list_names + get_names))
# b = list(set(list_names)-set(get_names))
# c = list(set(list_names)^set(get_names))
# d = list(set(list_names)&set(get_names))
# print(b)


# # a =( "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2")
# # b = ("1234567890")
# # c =[]
# # for i in a:
# #  if i in b:
# #   c.append(i)
# # print(c)






students = [
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},

]

# male = 0
# student=0
# for i in students:
#  if i["gender"] == "Male":
#   male = male +1
# print(male)
# print("male: ",27/38*100)
# print ("female: ",12/38*100)








# python=[]
# for i in students:
#  if i["course"] == "python":
#   python.append(i)

# print(python)


# for i in students:
#  if i in students:
#   students.remove(i)

# print(students)



age_30 = 0
student =0
for i in students:
 if i["age"] >= 30:
  age_30=age_30+1
for i in students:
 student = student +1
 
print(100/student*age_30)


python = []
for i in students:
    if['course'] == 'python':
      python.append(i)
print(python)


for i in sorted(students):
    print(sorted(students))
