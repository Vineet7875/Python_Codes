# class Employee:
#     x=10
#     y=20
#     def fun(self):
#         print("oops")

# obj=Employee()
# print(obj.x,obj.y)
# obj.fun()

# class Employee:
#     def fun(self):
#        return self.x+self.y
# obj=Employee()
# obj.x=20
# obj.y=80
# z=obj.fun()
# print(z)

# class Employee:
#     company="Google"
#     def fun(self):
#         pass
# obj1=Employee()
# obj2=Employee()
# obj1.company="Youtube"
# obj2.company="Facebook"
# print(Employee.company)
# print(obj1.company)
# print(obj2.company)


# class Employee:
#     company="Google",
#     salary=40000
#     def fun(self):
#         pass
# obj1=Employee()
# obj2=Employee()
# Employee.company="Youtube"
# obj1.salary=50000
# obj2.salary=80000
# Employee.salary=100
# print(Employee.company)
# print(obj1.company)
# print(obj2.company)
# print(obj1.salary)
# print(obj2.salary)

# class Employee:
#     a=21
#     b=22
#     def fun(self):
#         print(self.a,self.b)
# obj=Employee()
# # Employee.fun(obj)
# obj.fun() 

# class Employee:
#     a=21
#     b=22
#     def fun(o):
#         print(o.a,o.b)
# obj=Employee()
# # Employee.fun(obj)
# obj.fun() 

# class Employee:
#     @staticmethod
#     def fun():
#         print("puthon tutorials")
# obj=Employee()
# obj.fun() 

# class Employee:
#     def __init__(self):
#        print("Default constructor called")
# obj1=Employee() 


# class Employee:
#     def __init__(self,name,age):
#         self.x=1
#         self.y=2
#         self.name=name
#         self.age=age
#         print("parameterised constructor")
#     def display(self):
#          print(self.name,self.age)  
# obj2=Employee("vineet",20)
# obj2.display()

# class Employee:
#     @staticmethod
#     def __init__():
#         print("constructor is called")
#     @staticmethod
#     def fun():
#         print("puthon tutorials")
# obj=Employee()
# obj.fun() 

#1
# class programmer:
#     def __init__(self,name,salary,role):
#         self.name=name
#         self.salary=salary
#         self.role=role 
#     def display(self):
#         print("name =",self.name)
#         print("salary =",self.salary)
#         print("role =",self.role)  
# obj=programmer("vineet",60000,"SDE-1")
# obj.display()

#2
# from cmath import sqrt


# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def sqr(self):
#         return self.n*self.n
#     def cube(self):
#         return self.n*self.n*self.n
#     def sqr_root(self):
#         return sqrt(self.n)
# obj=calculator(4)
# print(obj.sqr())
# print(obj.cube())
# print(obj.sqr_root())

#3
#NO
# class A:
#     a=2
# obj=A()
# obj.a=0
# print(obj.a)
# print(A.a)

#4
# class A:
#     @staticmethod
#     def greet(name):
#         print("Hello"+" "+name)
# obj=A()
# obj.greet("vineet")

#5
# class Train:
#     def book_ticket(self,seat):
#         self.seat = seat
#         print(self.seat,"seats booked")
#         self.seats =self.seats - self.seat
#     def seats(self):
#         self.seats=100
#         return self.seats
# obj=Train()
# print("reamaining seats ",obj.seats())
# obj.book_ticket(20)

#6
# class Employee:
#     def fun(vineet):
#        return vineet.x+vineet.y
# obj=Employee()
# obj.x=20
# obj.y=80
# z=obj.fun()
# print(z)

# class A:
#     name="vineet"
#     def fun1(self):
#         self.a=10
#         print(self.a)
# class B:
#     name="rahul"
#     # def fun1(self):
#     #     self.name="sachin"
#     #     print("function overriding")
#     salary=1000
#     def fun2(self):
#         pass
# class C(B,A):
#     def fun3():
#         pass
# b=B()
# a=A()
# c=C()
# # b.fun1()
# print(c.name)
# print(c.salary)


# class A:
#     def fun(self):
#         print("class A")
# class B(A):
#     def __init__(self):
#         print("class B constructor")
#     def fun(self):
#          super().fun()
#          print("class B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("class C constructor")
#     def fun(self):
#         super().fun()
#         print("class C")
# obj=C()
# # obj.fun()

# class A:
#     salary=60000
#     name="vineet"
#     @classmethod
#     def fun(cls):
#         cls.salary=100
#         cls.name="aman"
#         print(cls.salary,cls.name)

# obj=A()
# obj.salary=45000
# print(obj.salary)
# obj.fun()

# class Employee:
#     company="youtube"
#     salary=50000
#     salarybonus=2000
#     @property
#     def totalsalary(self):
#         return self.salary + self.salarybonus
#     @totalsalary.setter
#     def totalsalary(self,val):
#             self.salarybonus=val - self.salary
# obj=Employee()
# obj.totalsalary=60000
# print(obj.totalsalary)
# print(obj.salarybonus)
# print(obj.salary)

class Number:
    def __init__(self,num):
        self.num=num
    # def __add__(self,obj):
    #     print(self.num+obj.num)
    # def __sub__(self,obj):
    #     print(self.num-obj.num)
    # def __mul__(self,obj):
    #     print(self.num*obj.num)
    # def __truediv__(self,obj):
    #     print(self.num/obj.num)
    # def __floordiv__(self,obj):
    #     print(self.num//obj.num)
    # def __str__(self):
    #     return f"{self.num}"
    # def __len__(self):
    #     return (len(self.num))
n1=Number(22)
print(n1)
# n2=Number(5)
# print(len(n2))
# n1+n2
# n1-n2
# n1*n2
# n1/n2
# n1//n2

#1
# class A:
#     company="micosoft"
#     salary=150
# class B(A):
#     def set(self):
#         self.salary=200
#         self.company="google"
#     def display(self):
#         print(self.company,self.salary)
# b=B()
# b.set()
# b.display()

#2
#multilevel inheritance

#3
# class Employee:
#     salary=1000
#     increment=1.5
#     @property
#     def salaryafterincrement(self):
#         self.saryafterincrement=self.salary*self.increment
#         return self.saryafterincrement
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,val):
#         self.increment=val/self.salary
# obj=Employee()
# # print(obj.salaryafterincrement)    
# obj.salaryafterincrement=2000
# print(obj.salaryafterincrement)
# print(obj.salary)
# print(obj.increment)

#4
# class Complex:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,obj):
#         print((self.a+obj.a),(self.b+obj.b))
#     def __mul__(self,obj):
#         print((self.a*obj.a),(self.b*obj.b))
# obj1=Complex(2,3)
# obj2=Complex(1,4)
# obj1+obj2
# obj1*obj2

#5
# class vector:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def __add__(self,obj):
#         print((self.a+obj.a),"i","+",(self.b+obj.b),"j","+",(self.c+obj.c),"k")
#     def __mul__(self,obj):
#         print((self.a*obj.a),(self.b*obj.b),(self.c*obj.c))
# obj1=vector(1,3,5)
# obj2=vector(2,4,4)
# obj1+obj2
# obj1*obj2

#6
# class vector:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def __str__(self):
#         return f"{self.a}i+{self.b}j+{self.c}k"
#     def __len__(self):
#         return self.a
# obj=vector(7,8,10)
# # print(obj)
# print(len(obj))

#7
# class vector:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def __add__(self,obj):
#         print((self.a+obj.a),"i","+",(self.b+obj.b),"j","+",(self.c+obj.c),"k")
#     def __mul__(self,obj):
#         print((self.a*obj.a),(self.b*obj.b),(self.c*obj.c))
# obj1=vector(1,3,5)
# obj2=vector(2,4,4)
# obj1+obj2
# obj1*obj2

class person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def fun1(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Gender is",self.gender)
class faculty(person):
    def __init__(self,designation,department):
        self.designation=designation
        self.department=department
    def fun2(self):
        print("Designation is",self.designation)
        print("Department is",self.department)
class publication(person):
    def __init__(self,no_res_pub,no_book,no_articles):
        self.no_res_pub=no_res_pub
        self.no_book=no_book
        self.no_articles=no_articles
    def fun3(self):
        print("No of research paper published are",self.no_res_pub)
        print("No of Book published are",self.no_book)
        print("No of Articles published are",self.no_articles)
n=input("Enter name")
a=int(input("Enter age"))
g=input("Enter gender")
dg=input("Enter designation")
dp=input("Enter Department")
nrp=int(input("Enter no of research paper published"))
nb=int(input("Enter no of book published"))
na=int(input("Enter no of articles published"))
obj1=person(n,a,g)
obj2=faculty(dg,dp)
obj3=publication(nrp,nb,na)

obj1.fun1()
obj2.fun2()
obj2.fun1()
obj3.fun3()
obj3.fun1()


'''class Complex1:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __add__(self,obj):
        print(f"Addition is {self.num1+obj.num1}+{self.num2+obj.num2}i")

n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
m1=int(input("Enter a number"))
m2=int(input("Enter a number"))
obj1=Complex1(n1,n2)
obj2=Complex1(m1,m2)
obj1+obj2'''


'''try:
    start=int(input("Enter start number"))
    end=int(input("Enter end number"))
    if(start>=1 and end>=1):
        for i in range(start+1,end+1):
            if(i<=start+10):
                print(i)
            else:
                raise StopIteration
    else:
        raise ValueError
except StopIteration:
    print("10 numbers printed =>StopIterration Exception raised")
except ValueError:
    print("Enter natural number =>Exception raised")'''


# class store:
#     d={1:15000,2:7000,3:5000,4:3000,5:2000}
#     Device=""
#     def code(self,a):
#         self.a=a
#         c=self.d.get(self.a)
#         if(self.a==1):
#             self.Device="LAPTOP"
#         elif(self.a==2):
#             self.Device="MOBILE"
#         elif(self.a==3):
#             self.Device="AIRBUDS"
#         elif(self.a==4):
#             self.Device="POWERBANK"
#         elif(self.a==5):
#             self.Device="CHARGER"
#         return c
#     def qua(self,b):
#         self.b=b
#         # self.d.get()
#     def display(self,c):
#         print("product code\tproduct name\tproduct price\tNoofproducts\tprice")
#         print(f"{self.a}\t\t{self.Device}\t\t{c}\t\t{self.b}\t\t{c*self.b}")
# obj=store()
# n1=int(input("Enter product code"))
# value=obj.code(n1)
# n2=int(input("Enter quanty"))
# obj.qua(n2)
# obj.display(value)

'''import random
class MyError(Exception):
    pass
try:
    num=random.random()
    print(num)
    if(num<0.1):
        raise MyError("Raise an Exception ")
except Exception as e:
    print("Number is below 0.1")'''


