# def reverse(n,rev=0):
#     if n==0:
#         return rev
#     return reverse(n//10,rev*10+n%10)
# n=int(input("Enter the number:"))
# print(reverse(n))
def rev(n,result=0):
    if n==0:
        return result
    result=result*10+(n%10)
    return rev(n//10,result)
n=int(input("Enter the number:"))
print(rev(n))