def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter the number:"))
print(fact(n))
# def sum(n):
#     if n==0:
#         return 0
#     return (n%10)+sum(n//10)
# n=int(input("Enter the number:"))
# print(sum(n))
