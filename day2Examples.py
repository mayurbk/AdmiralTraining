# #python functions
# def cal(x,y):
#     print(x+y)
#
# cal(2,3)
#
#
# dict1 = {'day':'monday','course':'python','version':3.9}
# def arbitraryparam(*var):
#     print(var)
#
# arbitraryparam()
#
# def keywordargsparam(**names):
#     print(names)
#
# keywordargsparam(name1 = 'Sunny', age = 30, name2 = 'Sam', name3 = 'Ziad')
#
# def age(**age):
#     print("the youngest is",age['age3'])
#
# age(age1=20,age2=30,age3=15)
#
# def defaultparam(a,country = 'India'):
#     print(country)
#     print(a)
#
# defaultparam(a=50)
# defaultparam(country= 'Yemen',a=50)
#
# var = 'Outside the function'
#
# def func3():
#     var1 = 'Inside the Function'
#     global var
#     var = 'new input'
#     print(var)
#     print(var1)
#
# func3()
#
# print(var)
#
#
#

#error handling

day = 'monday'
try:
    day1 = int(day)
    print(day1)
except:
    print("cannot be converted.")


# try:
#     num1 = int(input("enter first number"))
#     num2 = int(input("enter a second number"))
#     print("the division of the numbers is:",num1/num2)
# except ZeroDivisionError:
#     print("Cannot divide a number by zero.")
# except ValueError:
#     print("please enter a number value.")

# hours = int(input('enter hours'))
# rate = int(input('enet rate'))
# if hours>40:
#     print("amount is:",(40*rate)+((hours-40)*(rate*1.5)))
# else:
#     print("amount is:",hours*rate)
#working with for loop
# l1 = ['apple','mango',80,70,50]
# for item in l1:
#     print(item)
# val = range(5)
# for i in val:
#     print(i)
# else:
#     print('all items printed sucessfully.')
#
# startnumber = 1
# end_number = 10
#
# while startnumber<=end_number:
#     print(startnumber)
#     startnumber=startnumber+1   #stn=2, stn=3...............stn=9,stn=10,stn=11

#using break and continue statements
# for i in range(5):
#     if i== 2:
#         continue
#     print(i)
#
# n = 1
# while n<=5:
#     print('2*',n, '=',2*n)
#     if n>=3:
#         break
#     n=n+1

num1 = int(input('enter first number:'))
num2 = int(input('enter second number:'))
while num2<num1:
    print("please enter a greater number for second value.")
    num2 = int(input('enter second number:'))

result = num2-num1
print(result)

#exercise
##you have a magic number. ask user for a input number. until the input number is not equal to
# the magic number, show whether the entered number is less or greater than the input number
# the usaer will be prompted to enter the number
#in a loop.

# magic_n = 555
# user_number = int(input("please enter a number to check your magic ability:"))
#
# while:
#     #"you have not entered the magic number, enter again'
#     #if user_number >magic number
#     #entered number is greater
#     #if user_number <magic number
#     #entered number is smaller
#     #your entered number is less or greater than the magic number
#
# print("well done! The magic number is",magic_n)