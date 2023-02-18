# def add(x,y):
#     return x+y
# a=10
# b=20
# c=add(a,b)
# print(c)

# marks1=[45,67,89,34]
# marks2=[43,65,87,90]
# def percentage(marks):
#                 return (sum(marks)/400)*100
# percentage1=percentage(marks1)
# percentage2=percentage(marks2)
# print(percentage1,percentage2)


# def fun(name):
#     print("Good day" + " " + name)
# fun("vineet")

# def fun(name="Aman"):
#     print("Good day" + " " + name)
# fun("vineet")
# fun()

# num=int(input("Enter a number\n"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)


# def recursive(n):
#     if (n==1 or n==0):
#         return 1
#     return n*recursive(n-1) 
# factorial=recursive(num)
# print(factorial)

#1
# x=int(input("Enter a number"))
# y=int(input("Enter a number"))
# z=int(input("Enter a number"))
# def grt(a,b,c):
#     if(a>b and a>c):
#         print("a is greater")
#     elif(b>a and b>c):
#         print("b is greater")
#     else:
#         print("c is greater")
# grt(x,y,z)


#2
# temp=int(input("Enter a temp in celsius\n"))
# def temperature(t):
#     return t*1.8+32
# print(temperature(temp))

#3
# print("vineet",end=" ")
# print("jadhav")

#4
# num=int(input("Enter a number\n"))
# i=1
# sum=0
# def rec(n):
#     while(i<=n):
#         sum=sum+i
#         i=i+1
# return sum
# rec(num)

#5

#6
# lenght=float(input("Enter a lenght in inches\n"))
# def temperature(len):
#     return len * 2.54
# print(temperature(lenght))

#7
# list=["Harry","Soham","Sachin","Rahul"]
# def fun(l):
#     for item in l:
#         if (item.startswith("S")):
#             l.remove(item)
#     if(len(l)==4):
#         return l
# print(fun(list))

#8
# n=int(input("Enter a number\n"))
# def fun(num):
#     for i in range(1,11):
#         print(num*i)
# fun(n)