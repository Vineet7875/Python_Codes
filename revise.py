# '''print("Hello world")
# import imp
# import os
# import flask'''
# print("twinkle twinkle")
# print("little star")
# import os
# print(os.listdir())

# name="vineet"
# age=20
# per=34.67
# print(type(name))
# print(type(age))
# print(type(per))

# a=4
# a+=3
# print(a)
# # a=a+3

# a="1"
# b=2
# print(int(a)+b)

# a=int(input("Enter a value"))
# print(a)
# print(type(a))

# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(a+b)

# a=int(input("Enter a number"))
# print(a%2)

# a=input("Enter a name")
# print(type(a))

# a=34
# b=80
# if(a>b):
#     print("a is greater than b")
# else:
#      print("b is greater than a")

# a=int(input("Enter a number\n"))
# b=int(input("Enter a number\n"))
# print((a+b)/2)

# a=int(input("Enter a number"))
# print(a*a)

# a="Harry"
# # print(len(a))
# print(a[2])
# print(a[1:4])
# print(a[3:5])
# print(a[:4])
# print(a[2:])
# print(a[-1])
# b="vineet jadhav is very very bad boy bad"
# # print(b[0::2])
# # print(b[0::3])
# print(b.endswith("zv"))
# print(b.count("z"))
# print(b.capitalize())
# print(b.find("bad"))
# print(b.replace("bad","good"))

# a=input("Enter a name")
# print(f"Good morning, {a}")

# name=input("Enter a name\n")
# date=input("Enter a date\n")
# print(f"'''Dear <|{name}|>,\n\t\tyou are selected!\n\t\t<|{date}|>'''")

# a="vineet  jadhav  "
# print(a.find("  "))
# print(a.replace("  "," "))

# print("Dear Harry,\n\t This Python course is nice.\n\tThanks!")

# l1=[2,5,7.8,"vineet",89,"harry"]
# l=[3,56,1,45,90,23,45]
# l.sort()
# print(l)
# l.append(999)
# print(l)
# print(l.count(45))
# l.reverse()
# print(l)
# l.insert(1,998)
# print(l)
# l.pop(3)
# print(l)
# l.remove(45)
# print(l)

# a=(1,2,3)
# print(a)
# print(type(a))
# b=()
# print(b)
# print(type(b))
# c=(1,)
# print(c)
# print(type(c))

# a=(1,7,2,1)
# print(a.count(1))
# print(a.index(7))

# l=[]
# for i in range(7):
#     a=input("Enter fruit name")
#     l.append(a)
# print(l)

# l=[]
# for i in range(6):
#     a=input("Enter marks")
#     l.append(a)
# print(l)

# a=(1,3,6)
# a[1]=999
# print(a)

# l=[1,2,3,4,5]
# print(sum(l))

# t=(7,0,8,0,0,9)
# print(t.count(0))

# a={"name":"vineet",
#     "marks":34,
#      2:1,
#     "list":[1,5,7],
#     "tuple":(4,8,0),
#     "dict":{"age":20,
#             "role":"SDE"
#            }
#   }

# # print(a.items()) 
# # print(a.keys())
# print(a.update({"marks":90}))
# print(a)
# print(a.get("tuple"))
# print(a)
# print(a["tuple"])
# a["marks"]=60
# a["salary"]=50000
# print(a["dict"]["role"])
# print(a)
# print(a)
# print(type(a))

# s={1,5,7,7,1}
# print(s)
# print(len(s))
# print(s.remove(5))
# print(s)
# s.pop()
# print(s)
# s.add(5)
# s.add(9)
# print(s)
# s.clear()
# print(s)
# s={1,5,7,8}
# print(s.union({1,9,7,8}))
# print(s.intersection({1,90,87}))
# s=set()
# s.add(1)
# s.add(5)
# s.add(9)
# print(s)

# dict={
#         "panka":"fan",
#         "kapade":"cloths",
#         "vahi":"notebook",
#         "roomal":"handkerchief"
#      }
# print(dict)
# print(dict.items())

# s=set()
# for i in range(8):
#     a=int(input("Enter a number"))
#     s.add(a)
# print(s)

# s={18,"18"}
# print(s)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))

# s={}
# print(type(s))

# s={}
# for i in range(2):
#     a=input("Enter your name\n")
#     b=input("Enter your fav language\n")
#     s.update({f"{a}":f"{b}"})
# print(s)
# print(type(s))

# a=20
# if(a<5):
#     print("a is greater than 5")
# elif(a<10):
#     print("a is greater than 10")
# else:
#     print("a is greater than 5 and 10")

# age=int(input("Enter your age\n"))
# if(age>=18):
#     print("yes")
# else:
#     print("No")

# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# d=int(input("Enter a number"))
# if(a>b and a>c and a>c):
#     print("a is greater")
# elif(b>a and b>c and b>d):
#     print("b is greater")
# elif(c>a and c>b and c>d):
#     print("c is greater")
# else:
#     print("d is greater")

# a=int(input("Enter a marks\n"))
# b=int(input("Enter a marks\n"))
# c=int(input("Enter a marks\n"))
# tper=((a+b+c)/300)*100
# s1per=(a/100)*100
# s2per=(b/100)*100
# s3per=(c/100)*100
# if(tper>40 and s1per>33 and s2per>33 and s3per>33):
#     print("pass")
# else:
#     print("fail")

# a=input("Enter a comment\n")
# if("make a lot of money" in a or "buy now" in a or "click this" in a):
#     print("spam")
# else:
#     print("not spam")

# a=input("Enter a username\n")
# if(len(a)<10):
#     print("yes")
# else:
#     print("No")

# l=["vineet","harry","aman","naman","akshay"]
# for item in l:
#     if(item=="harry"):
#         print("yes")

# marks=int(input("Enter marks\n"))
# if(marks>60 and marks<100):
#     print("A")
# elif(marks>30 and marks<60):
#     print("C")
# else:
#     print("F")

# post="vineet is a bad boy"
# if("harry" in post):
#     print("yes")
# else:
#     print("no")  

# i=1
# while(i<=50):
#     print(i)
#     i=i+1

# l=[4,8,90,"vineet",45]
# i=0
# while(i<=len(l)-1):
#     print(l[i])
#     i+=1

# for i in range(1,5,2):
#     print("hi")

# l=[1,7,8]
# for item in l:
#     print(item)
# else:
#     print("loop khatam")

# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)

# a=3
# if(a==3):
#     pass

# a=int(input("Enter a number\n"))
# for i in range(2,3):
#     for j in range(1,11):
#         print(i*j)

# l1=["Harry","Soham","Sachin","Rahul"]
# for item in l1:
#     if(item.startswith("S")):
#         print(f"Hello {item}")

# a=int(input("Enter a number\n"))
# i=1
# while(i<=10):
#     print(a*i)
#     i=i+1

# num=int(input("Enter a number\n"))
# n=num/2
# a=0
# for i in range(2,int(n)):
#     if(num%i==0):
#         a=1
#         break
# if(a==1):
#     print("not prime")
# else:
#     print("prime")

# n=int(input("Enter a number"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(sum)

# n=int(input("Enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# for i in range(1,4):
#     for j in range(i):
#         print("* ",end="")
#     print()

# n=int(input("Enter a number\n"))
# for i in range(10,0,-1):
#     print(n*i)

# def fun():
#     print("function")
# fun()

# name=input("Enter your name")
# def fun(n="vineet"):
#     return f"Good Day,{n}"
# print(fun(name))

# num=int(input("Enter a number\n"))
# def fun(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fun(n-1)
# print(fun(num))

# x=int(input("Enter a number\n"))
# y=int(input("Enter a number\n"))
# z=int(input("Enter a number\n"))
# def grt(a,b,c):
#     if(a>b and a>c):
#         print("a is greater")
#     elif(b>a and b>c):
#         print("b is greater")
#     elif(c>a and c>b):
#         print("c is greater")
# grt(x,y,z)

# c=int(input("Enter temp in celsius"))
# def temperature(cel):
#     f=cel*9.5+1.8
#     return f
# print(temperature(c))

# print("vineet",end="")
# print("jadhav")

# for i in range(1,4):
#    for j in range(4-i):
#     print("* ",end="")
#    print()

# l=["vineet","jadhav","harry","aman"]
# def fun(word):
#     for item in l:
#         if(item==word):
#             l.remove(item)
# fun("harry")
# print(l)

# n=int(input("Enter a number\n"))
# def fun(num):
#     for i in range(1,11):
#         print(num*i)
# fun(n)

# f=open("sample.txt",'r')
# data=f.read(2)
# print(data)
# f.close()

# f=open("sample.txt",'w')
# f.write(" This content will append")
# f.close()

# with open("sample.txt",'r') as f:
#     data=f.read()
#     print(data)

# with open("poems.txt") as f:
#     data=f.read()
# print(data)
# if("twinkle" in data):
#     print("yes")
# else:
#     print("No")

# def game():
#     return 290
# score=game()
# with open("hisscore.txt") as f:
#     hiscore=f.read()
# if(hiscore==""):
#     with open("hisscore.txt",'w') as f:
#         f.write(str(score))  
# elif(score > int(hiscore)):
#     with open("hisscore.txt",'w') as f:
#         f.write(str(score))


# for i in range(2,21):
#     with open(f"multiplication table of {i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}*{j}={i*j}")
#             f.write("\n")

# l=["Donkey","kaddu","motu"]
# f=open("rough.txt",'r')
# data=f.read() 
# for item in l:
#     if(item in data):
#         data=data.replace(item,"#####")
# f=open("rough.txt",'w')
# f.write(data)

# with open("sample.txt") as f:
#     data=f.read()
# if("python" in data):
#     print("yes")
# else:
#     print("no")

# with open("sample.txt") as f:
#     for i in range(1,100):
#         data=f.readline()
#         if("python" in data):
#             print("yes")
#             print(f"{i}")

# with open("sample.txt") as f:
#     data1=f.read()
# with open("this.txt",'r') as f:
#     data2=f.read()
# if(data1==data2):
#     print("same")
# else:
#     print("different")

# with open("this.txt",'w') as f:
#     f.write("")

# class Employee:
# #     salary=60000
# #     comapny="microsoft"  
#     def __init__(vineet,x,y):
#         vineet.x=x
#         vineet.y=y
#     def get(vineet):
#         print(vineet.x)
#         print(vineet.y)       
# obj=Employee(1,2)
# obj1=Employee()
# Employee.salary=50000
# print(obj1.salary)
# obj.salary=200
# obj.get()
# Employee.display(obj)
# print(obj.salary)

# class programmer:
#     company="google"
#     salary=50000
# obj=programmer()
# print(obj.company)
# print(obj.salary)

# from cmath import sqrt


# class calculator:
#     n=4
#     def square(self):
#         return self.n*self.n
#     def cube(self):
#         return self.n*self.n*self.n
#     # def sqroot(self):
#     #     return sqrt(self.n) 
#     @staticmethod
#     def display(name):
#         print(f"Hello,{name}")
# obj=calculator()
# obj.display("vineet")
# # print(obj.square())
# # print(obj.cube())
# # print(obj.sqroot())

# class A:
#     a=1
# obj=A()
# obj.a=0
# print(A.a)

# from logging import RootLogger


# class Employee:
#     company="microsoft"
#     salary=60000
#     def fun(self):
#         print("Employee")
# class programmer(Employee):
#     role="Developer"
#     def fun(self):
#         print("programmer")
#         super().fun()
#     @classmethod
#     def fun(cls):
#         cls.name="vineet"

# obj2=programmer()
# # Employee.name="vineet"
# obj2.fun()
# print(obj2.name)
# # obj2.fun()

# class Employee:
#     salary=5000
#     bonus=200
#     @property
#     def totalsalary(self):
#         totalsalary=self.salary+self.bonus
#         return totalsalary
#     @totalsalary.setter
#     def totalsalary(self,val):
#         self.bonus=val -self.salary
# obj=Employee()
# print(obj.totalsalary)
# obj.totalsalary=6000
# print(obj.bonus)

# class A:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,obj):
#         return self.x + obj.x
#     def __sub__(self,obj):
#         return self.x - obj.x
#     def __mul__(self,obj):
#         return self.x * obj.x
#     def __truediv__(self,obj):
#         return self.x / obj.x
#     def __floordiv__(self,obj):
#         return self.x // obj.x
# obj1=A(4)
# obj2=A(2)
# print(obj1+obj2)
# print(obj1-obj2)
# print(obj1*obj2)
# print(obj1/obj2)
# print(obj1//obj2)

# class Animals:
#     pass
# class pets(Animals):
#     pass
# class dog(pets):
#     def bark(self):
#         pass

# from ast import increment_lineno
# class Employee:
#     salary=5000
#     increment=1.5
#     @property
#     def salaryafterincrement(self):
#         salaryafterincrement=self.salary*self.increment
#         return salaryafterincrement
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,val):
#         self.increment=val/self.salary
# obj=Employee()
# print(obj.salaryafterincrement)
# obj.salaryafterincrement=7000
# print(obj.increment)
 
# class complex:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,obj):
#         return f"{self.x+obj.x}+{self.y+obj.y}i"
# obj1=complex(2,3)
# obj2=complex(4,6)
# print(obj1+obj2)

# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self,obj):
#         return f"{self.x+obj.x}i+{self.y+obj.y}j+{self.z+obj.z}k"
# obj1=vector(2,3,2)
# obj2=vector(4,6,1)
# print(obj1+obj2)

# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __str__(self):
#         return f"{self.x}i+{self.y}j+{self.z}k"
# obj1=vector(2,3,2)
# print(obj1)

# from decimal import DivisionByZero
# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print("No errors")
# finally:
#     print("definatly excute")
# print("last line")

# print(__name__)
# def fun(name):
#     print(f"Good Day,{name}")
# if(__name__=="__main__"):
#     a=input("Enter your name\n")
#     fun(a)

# l=["vineet",67,34,"aman"]
# for index,item in enumerate(l):
#     print(index,item)

# l1=[1,2,3,4,5,6,7,8,9]
# l2=[item for item in l1 if item%2==0]
# print(l2)

# from logging import exception
# def fun(name):
#     try:
#         f=open(name,'r')
#     except FileNotFoundError:
#         print(f"{name} not found")
#     else:
#         print(f"{name} present")
# fun("1.txt")
# fun("2.txt")
# fun("3.txt")

# l=[1,4,7,"vineet","harry",9.7,56,21]
# for index,item in enumerate(l):
#     if(index%2==0 and index!=0):
#         print(item)

# n=int(input("Enter a number"))
# l=[n*i for i in range(1,11)]
# print(l)

# from decimal import DivisionByZero
# try:
#     a=int(input("Enter a number"))
#     b=int(input("Enter a number"))
#     c=a/b
#     print(c)
# except DivisionByZero:
#     print("ZeroDivisionError")
# print("last line")

# n=int(input("Enter a number"))
# l=[n*i for i in range(1,11)]

# with open("table1.txt",'w') as f:
#     f.write(str(l))

# def add(a,b):
#     return a+b
# print(add(1,2))

# add=lambda a,b:a+b
# print(add(1,2))

# l=["apple","mango","banana"]
# sentence=" and ".join(l)
# print(sentence)

# def fun(name,role):
#     print("name={1} and role={0}".format(role,name))
# fun("vineet","developer")

# l=[1,2,3,4,5]
# def fun(item):
#     return item*item
# print(list(map(fun,l)))

# from functools import reduce
# l=[1,2,3,4,5]
# fun=lambda a,b:max(a,b)
# print(reduce(fun,l))

# name=input("Enter name\n")
# marks=int(input("Enter marks\n"))
# number=int(input("Enter phone number\n"))
# def fun(n,m,num):
#     print("The name of the student is {} , his marks are {} and phone number is {}".format(n,m,num))
# fun(name,marks,number)

# l=[str(7*i) for i in range(1,11)]
# print(l)
# sentence="\n".join(l)
# print(sentence)

# l=[1,5,90,67,34,10,20]
# fun=lambda a:a%5==0
# print(list(filter(fun,l)))

# from functools import reduce
# l=[1,5,134,67,34,10,20]
# fun=lambda a,b:max(a,b)
# print(reduce(fun,l))



