def pal(n,result=0):
    if n==0:
        return result
    result=(result*10)+(n%10)
    return pal(n//10,result)
n=int(input("Enter the number:"))
if n==pal(n):
    print("Palindrome")
else:
    print("Not Palindrome")