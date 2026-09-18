def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
n=int(input("Enter the number:"))
print(sum(n))
#For Even number Sum
# def sum_even(n):
#     if n==0:
#         return 0
#     if n%2==0:
#         return n+sum_even(n-1)
#     else:
#         return sum_even(n-1)
# n=int(input("Enter the number:"))
# print(sum_even(n))