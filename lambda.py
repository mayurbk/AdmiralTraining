def myfunc(n):
    print(n**2)

myfunc(4)
#
x = lambda n:n**2
print(x(4))
# print(x(4))
#
mystr = "python"
mylambda = lambda string:string.upper()
print(mylambda(mystr))
#
mylist = [12,23,43,21,28,65,49,97]
e_list = list(filter(lambda x:(x%2==0),mylist))
print(e_list)

#e_list = list(filter())

#print all ages by creating a list greater than 15

m_list = list(map(lambda x:x+2,mylist))
print(m_list)
#
# from functools import reduce
# mylist = [12,23,43,21,28,65,49,97]
# my_reduce = reduce((lambda x,y:x+y),mylist)
# print(my_reduce)
# max_reduce = reduce((lambda x,y:x if x>y else y),mylist)
# print('thye maximum element is :',max_reduce)
#
# newlist=[]
# for x in mylist:
#     if x>30:
#         newlist.append(x)
#
# print(newlist)
#
# newlist1 = [x for x in mylist if x>30]
# print(newlist1)
#
# x = input("enter a day")
# day = "sunday"
# result = ["office close" if x==day else "office open"]
# print(result)
