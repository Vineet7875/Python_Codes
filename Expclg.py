#1.1

# a=10
# b=10.32
# c="vineet"
# print(f"a={a} its datatype is {type(a)}")
# print(f"b={b} its datatype is {type(b)}")
# print(f"c={c} its datatype is {type(c)}")
# print(f"{type(2+3j)}")

#1.2

# n1=int(input("Enter a number"))
# n2=int(input("Enter a number"))
# print(n1+n2)
# print(n1-n2)
# print(n1*n2)
# print(n1/n2)
# print(n1//n2)

1.3

# a="vineet"
# b="jadhav"
# print(a+" "+b)

1.4

# quantity=int(input("Enter no of quantities sold"))
# value=int(input("Enter value of one quantity"))
# discount=float(input("Enter discount in percentage"))
# tax=float(input("Enter tax"))
# amount=quantity * value
# discount_amount=amount * (discount/100)
# discounted_amount=amount - discount_amount
# tax_amount=discounted_amount * (tax/100)
# bill_amount=discounted_amount + tax_amount
# print("Bill amount is",bill_amount)

2.1

# char=input("Enter a character")
# if(char>='a' and char<='z'):
#     print(char.upper())
# else:
#     print(char.lower())

2.2

# n1=int(input("Enter a 1st number"))
# n2=int(input("Enter a 2nd number"))
# n3=int(input("Enter a 3rd number"))
# max=n1 if n1>n2 else n2
# max=n3 if n3>max else max
# print(max)

2.3

# n=int(input("Enter a weekday number between 1-7\n"))
# if n==1:
#     print("Monday")
# elif n==2:
#     print("Tuesday")
# elif n==3:
#     print("Wednesday")
# elif n==4:
#     print("Thursday")
# elif n==5:
#     print("Friday")
# elif n==6:
#     print("Saturday")
# elif n==7:
#     print("Sunday")
# else:
#     print("Please Enter a weekday number between 1-7")

# 3.1

# l1=[]
# l2=[]
# while(1):
#     n=int(input("Enter a number\n"))
#     if(n==-1):
#         break
#     elif(n>0):
#         l1.append(n)
#     elif(n<0):
#         l2.append(n)
# print(f"+ve numbers avg={sum(l1)/len(l1)}")
# print(f"-ve numbers avg={sum(l2)/len(l2)}")

# 3.2

# investment=int(input("Enter investment amount\n"))
# rate=int(input("Enter rate of interest\n"))
# years=int(input("Enter no of years\n"))
# for i in range(years):
#     interest_amount=investment*(rate/100)
#     investment=investment+interest_amount
# print(f"final investment={investment}")

#4.1

# t=(10,20,30,40,50)
# print(type(t))
# print(t + (2,3))
# print(len(t))
# if(30 in t):
#     print("yes")
# else:
#     print("no")
# for i in range(len(t)):
#     print(t[i])

#4.2

# l=[]
# l.insert(0,10)
# print(l)
# l.remove(10)
# print(l)
# l.append(20)
# print(l)
# print(len(l))
# l.pop(0)
# print(l)
# l.insert(0,10)
# l.insert(1,20)
# print(l)
# l.clear()
# print(l)

#4.3

# d={
#     1:"laptop",
#     2:"mobile",
#     3:"ipad",
#     4:"airbuds"
# }
# print(d)
# print(len(d))
# print(d.keys())
# print(d.values())
# print(d.get(3))
# d[1]="powerbank"
# d[10]="bank"
# print(d[2])
# print(d)

#5.1

# def fun(string):
#     string=string.casefold()
#     print(list(string))
#     reverse=reversed(string)
#     print(list(reversed(string)))
#     if(list(string)==list(reverse)):
#         print("palindrome")
#     else:
#         print("Not a palindrome")
# s=input("Enter a string")
# fun(s)

#5.2

# def fun(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         fact=1
#         for i in range(1,n+1):
#             fact=fact*i
#         return fact
# num=int(input("Enter a number"))
# store=fun(num)
# print(f"factorial of {num} is {store}")

#5.3

# def fun(l1,l2):
#     if(l1 == l2):
#         return True
#     else:
#         return False
# list1=["vineet","jadhav","askhay"]
# list2=["vineet","jadhav","askhay"]
# store=fun(list1,list2)
# if(store == True):
#     print("Equal")
# else:
#     print("Not Equal")

#6.1




#6.2

# import datetime
# print(datetime.datetime.today())
# print(datetime.date.today())
# print(datetime.date.today().day)
# print(datetime.date.today().month)
# print(datetime.date.today().year)

#6.3

# import module
# print(module.ADD(3,2))
# print(module.SUB(3,2))

# from module import ADD,SUB 
# print(ADD(3,2))
# print(SUB(3,2))

#7.1

# d={
#     1:15000,
#     2:70000,
#     3:5000,
#     4:2000,
#     5:1200
# }
# device=""
# class store:
#     def Code(self,code):
#         self.code=code
#         if(self.code ==1):
#             self.device="Mobile"
#         elif(self.code==2):
#             self.device="Laptop"
#         elif(self.code==3):
#             self.device="Airbuds"
#         elif(self.code==4):
#             self.device="Powerbank"
#         elif(self.code==5):
#             self.device="Smart Watch"
#         else:
#             print("Enter a valid code")
#     def qua(self,quantity):
#         self.quantity=quantity
#     def value(self):
#         price=d.get(self.code)
#         return price
#     def display(self,prize):
#         print("Code\tName\tQuantity\tPrice\t\tAmount")
#         print(f"{self.code}\t{self.device}\t{self.quantity}\t\t{prize}\t\t{self.quantity*prize}")
# obj=store()
# n1=int(input("Enter a code"))
# n2=int(input("Enter a quantity"))
# obj.Code(n1)
# obj.qua(n2)
# a=obj.value()
# obj.display(a)

#7.2

# class person():
#     def get(self):
#         self.name=input("Enter name")
#         self.age=int(input("Enter age"))
#         self.gender=input("Enter gender")
#     def display(self):
#         print("Name is",self.name)
#         print("Age is",self.age)
#         print("Gender is",self.gender)
# class faculty(person):
#     def get(self):
#         super().get()
#         self.designation=input("Enter designation")
#         self.department=input("Enter Department")
#     def dispaly(self):
#         super().display()
#         print("Designation is",self.designation)
#         print("Department is",self.department)
# class publication(person):
#     def get(self):
#         super().get()
#         self.no_res_pub=int(input("Enter no of research paper published"))
#         self.no_book=int(input("Enter no of book published"))
#         self.no_articles=int(input("Enter no of articles published"))
#     def display(self):
#         super().display()
#         print("No of research paper published are",self.no_res_pub)
#         print("No of Book published are",self.no_book)
#         print("No of Articles published are",self.no_articles)
# obj1=person()
# obj2=faculty()
# obj3=publication()

# obj3.get()
# obj3.display()



#8.1

# class Complex:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def __add__(self,obj):
#          print(f"{self.num1+obj.num1} + {self.num2+obj.num2}j")
#        return f"{self.num1+obj.num1} + {self.num2+obj.num2}j"
# n1=int(input("Enter a number"))
# n2=int(input("Enter a number"))
# n3=int(input("Enter a number"))
# n4=int(input("Enter a number"))
# obj1=Complex(n1,n2)
# obj2=Complex(n3,n4)
# obj3=Complex()
# obj3=obj1+obj2
# print(obj3)

#9.1

# try:
#     n=int(input("Enter a number\n"))
#     if(n==0):
#         print(f"{n} is Zero")
#     elif(n>0):
#         print(f"{n} is +ve")
#     else:
#         raise ValueError
# except:
#     print("Exception raised valuerror Number is -ve ")

#9.2

# start=int(input("Enter a start number"))
# end=int(input("Enter a end number"))
# try:
#     for i in range(start,end+1):
#         if(i<start+10):
#             print(i)
#         else:
#             raise StopIteration
# except:
#     print("Stop interation exception raised")

#9.3

# import random
# class MyError(Exception):
#     def __init__(self,a):
#         self.a=a
#     def show(self):
#         print("My Exception",self.a)
# try:
#     while(1):
#         n=random.random()
#         print(n)
#         if(n<0.1):
#             raise MyError("Exception occured")
# except MyError as e:
#     print("number is below 0.1")

#10.1

# f=open("file1.txt","w")
# print(f.read())
# f.close()

# f=open("file1.txt","r")
# print(f.read())
# f.close()

# f=open("file1.txt","a")
# f.write("Kaise ho sab log")
# f.close()

# f=open("file1.txt","w+")
# f.write("Kaise ho sab log")
# f.seek(0)
# print(f.read())
# f.close()

# f=open("file1.txt","r+")
# f.write("To kaise hai aap log")
# f.seek(0)
# print(f.read())
# f.close()

# f=open("file1.txt","a+")
# f.write("Chaliye shuru karate hai")
# f.seek(0)
# print(f.read())
# f.close()

# import calendar
# print(dir(calendar))
# print(calendar.calendar(2023))
# print(calendar.month(2025,2))

# fun=lambda a,b:a+b
# print(fun(2,3))
# def sum(x):
#     print(x)
# sum(fun)

# str1="hello"
# print(str1.center(12,'*'))

# def fun(a,b=1):
#     print(a,b)
# fun(30,10)

# def fun(arg1,*argv):
#     print(arg1)
#     for arg in (argv):
#         print(arg)
# fun(30,10,78,67,44,89)

# def fun(vineet,*akshay):
#     print(vineet)
#     for aman in (akshay):
#         print(aman)
# fun(30,10,78,67,44,89)

# import datetime
# print(datetime.date.today())
# print(datetime.date.today().day)
# print(datetime.date.today().month)
# print(datetime.date.today().year)
# print(datetime.datetime.now().weekday())
# print(datetime.datetime.now().strftime("%A"))

# print(dir(__doc__)) #objects attributes
# print(__name__)


# str1="vineet"
# str2="vineet"
# list1=[1,2,3]
# list2=[1,2,3]
# t1=(2,3,4)
# t2=(2,3,4)
# print(id(list1)==id(list2))
# print(id(str1)==id(str2))
# print(id(t1)==id(t2))

# print(complex(3,4))

# list=[10,20,30,40,50]
# print(list[-3:-1])
# print(list[-3:4])
# print(list[1:5])

# def fun(*argc):
#     for i in range(len(argc)):
#         print(argc[i])
# fun(10,22,33,44,55)

# def fun(b=2):
#     print(b)
# fun(5)