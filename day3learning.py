# # # #using lambdda
# # #
# # # list1 = [12,221,23,4,34,32,55,67,79,21]
# # # for i in list1:
# # #     if i%2==0:
# # #         print("even numbers are",i)
# # #     else:
# # #         print("odd numbers are",i)
# # #
# # #
# # # #higher prder functions, map,filter,reduce
# # #
# # # x = lambda a,b : a if(a>b) else b
# # # print(x(4,5))
# # #
# # # y = input("enter a day")
# # # l = lambda y: print("close") if y=="sunday" else print("open")
# # #
# # # print(l(y))
# # #
# # # filter
# # list1 = [12,221,23,4,34,32,55,67,79,21]
# # result = tuple(filter(lambda i:i+2,list1))
# # print(result)
# #
# # #map
# # result1 = list(map(lambda x:x%2==0,list1))
# # print(result1)
# #
# # #reduce
# # from functools import reduce
# # list1 = [12,221,23,4,34,32,55,67,79]
# # result2 = reduce((lambda a,b:a+b),list1)
# # print(result2)
# # result3 = reduce((lambda a,b:a if a >b else b),list1)
# # print(result3)
# # sqr = []
# # for x in range(5,20):
# #     if x %2==0:
# #         sqr.append(x)
# # print(sqr)
# #
# # sqr1 = [x+2 for x in range(5,20) if x%2==0 ]   #list comprehension
# # print(sqr1)
# #
# # y = input("enter a day")
# # l = ['close' if y=='sunday' else 'open']
# # print(l)
# # z = input("enter month")
# # z1=z.upper()
# # l = ['winter' if z1=='DECEMBER' else 'moderate']
# # print(l)
# # for i in l:
# #     if "o" in i:
# #         print("contains")
# #     else:
# #         print("nothing")
#
# # result = [x for x in range(30) if x%2== 0 and x%5==0]
# # print(result)
#
#generator functions
# def wel():
#     print("round1")
#     yield
#     print("round2")
#     yield
#     print("round3")
#     yield
# messenger=wel()
#
# result1 = next((messenger))
# result2 = next(messenger)
# print(result2)
#
# #
# # #syntax of generator expression
# # #expression for item in iterable
# #
# # sqr = (x*x for x in range(10))
# # for x in sqr:
# #     print(x)
#
#
#
# def seq(x):
#     for i in range(x):
#         yield i
#
# gen1 = seq(10)
# gen2 = seq(10)
# print(next(gen1))
# print(next(gen2))
# print(seq(4))
#
# #named tuple
# from collections import namedtuple
# t = namedtuple('StudentDetails','fname,lname,Dob')
# x = t('peter','thomas','21 january')
# print(x)
#
# from collections import defaultdict
#
# def def_val():
#     return 'not exist'
#
# d = defaultdict(def_val)     #lambda functions
# d['x'] = 'monday'
# d['y'] = 'tuesday'
# d['z'] = 2
#
# print(d['x'])
# print(d['a'])

# from collections import Counter
# colors = ['red','green','blue','blue','red','red','green','blue','blue','black']
# c = Counter(colors)
# print(c)
#
# s = sorted(colors)
# print(s)
#
# courses = ['English', 'Math', 'Art','science','physics']
# grades = [96, 99, 88, 94]
# z = zip(courses, grades)
# print(tuple(z))
# print(type(z))
#
# def f1():
#     print("hello")
#     def f2():
#         var = 5
#         print("local var is",var)
#     f2()
#
# print(f1())
#
print(dir(__builtins__))