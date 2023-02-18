# def fun(a):
#     return a+5
# print(fun(10))

# fun=lambda a:a+5
# square=lambda b:b*b
# addd=lambda x,y,z:x+y+z
# print(fun(10))
# print(square(2))
# print(addd(1,2,3))


# list=["Mobile","Laptop","Headphone","Earbud","Power bank"]
# a=" and ".join(list)
# print(a)
# print(type(a))
# tuple=("Mobile","Laptop","Headphone","Earbud","Power bank")
# a=" + ".join(list)
# print(a)

# n="vineet"
# a=20
# a=f"name={n} and age={a}"
# print(a)
# print(type(a))

# n="vineet"
# a=20
# a="name={} and age={}".format(n,a)
# print(a)
# print(type(a))

# n="vineet"
# a=20
# r="Developer"
# a="name={2} and age={0} and role={1}".format(a,r,n)
# print(a)
# print(type(a))


# l1=[1,2,4]
# l2=[]
# def fun(num):
#     return num*num
# for item in l1:
#     l2.append(fun(item))
# print(l2)


# l1=[1,2,4]
# def fun(num):
#     return num*num
# print(list(map(fun,l1)))

# l1=[1,2,3,4,5,6,7,8,9]
# def fun(num):
#     if(num%2!=0):
#         return True
#     else:
#         return False
# print(list(filter(fun,l1)))

# l1=[1,2,3,4,5,6,7,8,9]
# fun=lambda num:num%2==0
# print(list(filter(fun,l1)))

# from functools import reduce
# l1=[1,2,3,4]
# fun=lambda a,b:a+b 
# val=reduce(fun,l1)
# print(val)
# fun=lambda a,b:a*b 
# print(reduce(fun,l1))

#1
#2
# name="Harry"
# marks=34
# phone_number=8308544723
# print("The name of student is {},his marks are {} and phone number is {}".format(name,marks,phone_number))

#3
# l=[str(7*i) for i in range(1,11)]
# print(l)
# table="\n".join(l)
# print(table)

#4
# l=[10,6,8,15,78,5,20,98,70]
# def fun(num):
#     if(num%5==0):
#         return True
#     else:
#          return False
# print(list(filter(fun,l)))

#5
# from functools import reduce
# l=[45,67,3,1,90,57,78,999]
# fun=lambda a,b:max(a,b)
# print(reduce(fun,l))

#6
#7
