def rev(n):
    if n==0:
        return 0
    print(n)
    rev(n-1)
n=int(input("Enter the number:"))
rev(n)

# def rev(n):
#     if n==0:
#         return 0
#     rev(n-1)
#     print(n)
# n=int(input("Enter the number:"))
# rev(n)