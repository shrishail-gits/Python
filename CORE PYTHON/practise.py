# # a1="apple"
# # print(a1.upper())
# a1="BANANA"
# print(a1.lower())
# a1="GrAps"
# print(a1.swapcase())
# s="manjnu"
# print(s.capitalize())
# s="laila is dancing"
# print(s.replace("is","was"))
# s="Rose"
# print(s.islower())
# s="YASH"
# print(s.isupper())
# R="FUN"
# A=""
# for i in R:
#     A=i+A
# print(A)
# R="hello boss"
# A=""
# for i in R:
#     A=i+A
# print(A)
# R=input()
# A=""
# for i in R:
#     A=i+A
# if R==A:
#      print("Palindrome")
# else:
#      print("Not Palindrome")
# print(A)
# reverse the word not string
# a="hello boss"
# b=""
# c=""
# for i in a:
#     if i != " ":
#         c=c+i
#     else:
#         b=c+" "+b
#         c=" "
# b=c+" "+b
# print(b)
# r=" R A M "
# r1=""
# for i in r:
#     if i == " ":
#         continue
#     else:
#         r1=r1+i
# print(r1)
# r=" R A M "
# r=r.replace(" ","")
# print(r)
# t="tata"
# t1,t2,t3,t4=t
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# s="if you think you can or you cant"
# print(s.find("u"))
# print(s.count("you"))
# print(s.index("h"))
# print(s.rfind("i"))
# print(s.rindex("o"))
# print(s.find("python"))
# print(s.count("l"))
# s=input()
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())
# ptr="Raya is bad dad"
# res=ptr.split()
# r=""
# for i in res:
#     r=i+" "+r
# print(r.rstrip())
# name=input()
# place=input()
# print(f"I am {name},my native is {place}")
# A=int(input())
# B=int(input())
# print(f"sum={A+B}")
# r = input()
# s=""
# for ch in r:
#     if ch not in s:
#         s+=ch
# print(s)
# word=input()
# count={}
# for ch in word:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
# A=22
# def outer():
#     global A
#     A=33
#     B=44
#     print(A)
#     print(B)
#     def inner():
#         global A
#         A=11
#         B=55
#         print(B)
#         print(A)
#         print(A)
#     print(A)
#     inner()
#     print(A)
# print(A)
# outer()
# print(A)
# def outer():
#     print(R)
#     def inner():
#         R=420
#     inner()
# outer()
def outer():
    R=420 
    def inner():
        print(R)
    inner()
outer()