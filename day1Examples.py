# print("hello world")
# print("hello \"mayur\"")
#
# '''
# hello
# world
#
# Welcome to python classes.today is our first day.
# '''
# print("hello \nworld")
# print("deepak ","abhinav", "deepak.j","harendra","mohit","nikhil",sep=",")
# print("Welcome to python classes.",end="*")
# print("today is our first day.")
#
# '''
# /n - go to next line in the same print statement
# end- join two print statements
# sep - separate each of the strings in a line by the symbol given in the separator.
# '''
#
# print("\"I\'m\" \n\"\"learning\"\" \n\"\"\"Python\"\"\"")
# print(2+3)
# name = "mayur"  '''  string'''
# print("hello",name)
# number = 30.78 ;       '''integers'''
# print("there are",number, "apples in the basket")
# print(type(number))
# result = True
# print(type(result))

#floor division gives the quotient
# num1 = 20
# num2 = 3
# print(num1//num2)
#
# #modulus  gives the remainder of the division
# print(num1%num2)
#
# #xponentiation
# print(3**3)
#
# ##variable example1
# john = '3'
# mary = '5'
# adam = '6'
# print("john has:"+john,"mary has",mary,"adam has",adam,sep=",")
# total_apples = int(john)+int(mary)+int(adam)
# print("total apples are:",total_apples)
#
# print(chr(89))     #ASCII codes - 128- 52 alphabets
# print(ord("."))
# print(max("PYthon"))
# print(ord("P"))

#using string methods
# mystrng = "This is our python training.python is interesting."
# print(mystrng)
# print(mystrng.count('java'))
#
# #taking input from user
# fname = str(input("please enter your name:"))
# if fname.isalpha() == True:
#     print("Hello",fname)
# else:
#     print("please enter a valid name.")
# fnum = int(input("please enter a number:"))
# print("entered number is:",fnum)

#working with lists
# mylist = ['laptop','computer','books',90,29,True,'python programming','laptop']
# print(mylist)
# print(type(mylist))
# #mylist.append('car')
# print(mylist)
# print(mylist[3:7])
# #mylist.pop()
# print(mylist)
# mylist.insert(2,'java')
# print(mylist)
# newlist = []
# name1 = input("please enter a name:")
# name2 = input('please enter a name:')
# newlist.append(name1)
# newlist.append(name2)
# print(newlist)

#working with tuples
# mytuple = ('books','pens','cars',True,40)
# print(type(mytuple))
# mylist = list(mytuple)
# print(mylist)
# mylist.append('laptop')
# print(mylist)
# mytuple = tuple(mylist)
# print(mytuple)

#working with dictionaies
# mydict = {'sub':'python','version':3.9,'editor':'pycharm','day':1,'status':True}
# print(type(mydict))
# print(mydict)
# print(mydict.popitem())
# print(mydict)
# print(mydict.popitem())
# print(mydict)
# mydict.update({'day':2})
# print(mydict.get('sub'))
# mydict[1]='saturday'
# mydict[1]='sunday'
# print(mydict)
#
# dict1 = {1:'monday',2:'tuesday',3:'wednesday'}
# dict2 = {1:'sunday',5:'thursday'}
# print(dict1)
# dict2.update(dict1)
# print(dict2)

#working with control flow
# x = int(input("please enter a number:"))
# if x>=2:
#     print("greater than 2")
#     if x<=4:
#         print('x is between 2 and 4')
# else:
#     print('x is not between 2 and 4')

#no.ofprojects(U/I), no.of o/s projects(U/I), %of o/s project >80, bonus will be 100%, o/s project 50-80, bonus 50%, if o/s <30, bonus 20 %
# no_of_projects = int(input("Enter the number of projects."))
# no_of_OS_feedbacks = int(input("Entr the number of O/S feedbacks you recieved."))
# percent = (no_of_OS_feedbacks/no_of_projects)*100
# print("your O/S feedback is ",percent, "%")
# if percent>80:
#     print("your bonus amount will be 100%.")
# if 50<percent<80:
#     print("bonus will be 50%")
# if 30<percent<50:
#     print("bonus is 20%")
# elif percent<30:
#     print("bonus is 5%")

#working with functions
def greet():
    print("welcome to the training sesssions.")

greet()

def add(x,y):
    print(x+y)

add(2,3)