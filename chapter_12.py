# while(1):
#     a=input("Enter a number")
#     print("Enter q to quite")
#     if(a=="q"):
#             break
#     try:
#         if(int(a)>6):
#             print("Number is greater than 6")
#     except Exception as e:
#         print(e)

# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print(e)

# print("Thanks for using our code")


# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except ValueError as e:
#     print("valueError")
#     print(e)
# except ZeroDivisionError as e:
#     print("ZeroDivisionError")
#     print(e)
# print("Thanks for using our code")


# def increment(num):
#     try:
#         return num + 1
#     except:
#         raise ValueError("Enter int value")
# z=increment('h')
# print(z)
# print("Thanks for using  our code")


# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print("Error Occurs")
#     print(e)
# else:
#     print("No any Error")

# print("Thanks for using our code")


# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print("Error Occurs")
#     print(e)
#     exit()
# else:
#     print("No any Error")

# print("Thanks for using our code")


# try:
#     a=int(input("Enter a number"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print("Error Occurs")
#     print(e)
#     exit()
# else:
#     print("No any Error")
# finally:
#     print("We are done")
    
# print("Thanks for using our code")



def fun(name):
    print(f"Good morning, {name}")
print(__name__)
if(__name__=="__main__"):
    a=input("Enter a name")
    fun(a)

# a=54 
# def fun():
#     print(a)
# fun()
# print(a)

# a=54
# def fun():
#     global a
#     print(a)
#     a=8
#     print(a)
# fun()
# print(a)


# list=[3,6,"vineet",9.78,"harry",1,]
# for item in list:
#     print(item)

# list=[3,6,"vineet",9.78,"harry",1,]
# for index,item in enumerate(list):
#     print(index,item)


# list1=[3,4,5,8,90,1,245,89]
# list2=[]
# for item in list1:
#     if(item%2==0):
#         list2.append(item)
# print(list2)

# list1=[3,4,5,8,90,1,245,89]
# list2=[item for item in list1 if item%2==0 ]
# print(list2)

# list=[1,5,7,4,8]
# set={item for item in list if item%2!=0}
# print(set)


#1
# try:
#     f=open("1.txt",'r')
#     f=open("2.txt",'r')
#     f=open("3.txt",'r')
# except Exception as e:
#     print(e)
#     print("file not present")

# def fun(filename):
#     try:
#         f=open(filename,'r')
#         f.close()
#     except FileNotFoundError:
#         print(f"{filename} not present")
#     else:
#         print(f"{filename} present")

# fun("1.txt")
# fun("2.txt")
# fun("3.txt")

#2
# list=[1,5,78,"harry","vineet",7.5,32]
# for index,item in enumerate(list):
#     if(index%2==0 and index!=0):
#         print(item)

#3
# n=int(input("Enter a number"))
# list=[n*i for i in range(1,11)]
# print(list)

#4
  
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# try:
#     c=a/b
#     print(c)
# except:
#     raise ZeroDivisionError("Infinite")

#5
# n=int(input("Enter a number"))
# list=[n*i for i in range(1,11)]
# # print(list)
# f=open("tables.txt",'a')
# f.write(str(list))
# f.write("\n")




