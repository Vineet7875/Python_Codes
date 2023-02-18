# f=open("sample.txt",'r')
# data=f.read()
# print(data)
# f.close()

# f=open("sample.txt",'rt')
# data=f.read()
# print(data)
# f.close()

# f=open("sample.txt")
# data=f.read()
# print(data)
# f.close()

# f=open("sample.txt",'r')
# data=f.read(5)
# print(data)
# f.close()

# f=open("sample.txt",'r')
# data=f.readline()
# print(data)
# f.close()

# f=open("sample.txt",'r')
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()

# f=open("another.txt",'w')
# f.write("Please write these to the file")
# f.close()

# f=open("another.txt",'w')
# f.write("ok ji")
# f.close()

# f=open("another.txt",'w')
# f.write("tata bye bye")
# f.write("tata bye bye")
# f.write("tata bye bye")
# f.write("tata bye bye")
# f.close()

# f=open("another.txt",'a')
# f.write(" this content will append in the file")
# f.close()

# f=open("another.txt",'a+')
# f.write("   this content will append in the file")
# f.close()

# with open("sample.txt",'r') as f:
#     data=f.read()
#     print(data)

# with open("sample.txt",'w') as f:
#     f.write("hello ji")
#     f.write("namaste python")

# 1
# f=open("poems.txt",'r')
# str=f.read()
# if "twinkle" in str:
#     print("prsent")
# else:
#     print("not present")

#2
# a=input("Enter a score")
# f=open("hisscore.txt",'w')
# f.write(a)
# b=input("Enter a score")
# a=int(a)
# b=int(b)
# if(b>a):
#     f=open("hisscore.txt",'w')
#     b=str(b)
#     f.write(b)
# c=input("Enter a score")
# a=int(a)
# b=int(b)
# c=int(c)
# if(c>a and c>b):
#     f=open("hisscore.txt",'w')
#     c=str(c)
#     f.write(c)

# def game():
#     return 100
# score=game()
# with open("hisscore.txt",'r') as f:
#     hiscore=f.read()
# if (hiscore ==""):
#     with open("hisscore.txt",'w') as f:
#         f.write(str(score))
# elif (int(hiscore)<score):
#     with open("hisscore.txt",'w') as f:
#         f.write(str(score))

#3
# for i in range(2,21):
#     with open (f"mutliplication table of {i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}*{j}={i*j}")
#             f.write("\n")

#4
# f=open("rough.txt",'r')
# data=f.read()
# print(data)
# f.close()
# data1=data.replace("Donkey","########")
# print(data1)
# f=open("rough.txt",'w')
# f.write(data1)

#5
# f=open("rough.txt",'r')
# data=f.read()
# print(data)
# f.close()
# data=data.replace("Donkey","########")
# data=data.replace("kaddu","########")
# data=data.replace("motu","########")
# print(data)
# f=open("rough.txt",'w')
# f.write(data)

# words=["Donkey","kaddu","motu"]
# f=open("rough.txt",'r')
# data=f.read()
# print(data)
# f.close()
# for word in words:
#     data=data.replace(words,"########")
# print(data)
# f=open("rough.txt",'w')
# f.write(data)

#6
# f=open("log.txt",'r')
# str=f.read()
# # print(str)
# if("python" in str):
#     print("present")
# else:
#     print("not present")

#7
# f=open("log.txt",'r')
# for i in range(1,10):
#     data=f.readline()
#     if("python" in data):
#         print(i)
    
#8
# f=open("log.txt",'r')
# data=f.read()
# print(data)
# f.close
# f=open("copy.txt",'w')
# f.write(data)
# f.close()

#9
# f=open("log.txt",'r')
# data1=f.read()
# f.close()
# f=open("copy.txt",'r')
# data2=f.read()
# # print(data2)
# f.close()
# if(data1==data2):
#     print("same")
# else:
#     print("different")

#10
# f=open("sample.txt",'w')
# f.write("")
# f.close()

#11
# import os
# f=open("sample.txt",'r')
# data=f.read()
# f.close()
# f=open("dimple.txt",'w')
# f.write(data)
# f.close()
# os.remove("sample.txt")
