n1 = int(input("Enter number of elements in first array: "))

arr1 = []

for i in range(n1):
    num = int(input("Enter number: "))
    arr1.append(num)

n2 = int(input("Enter number of elements in second array: "))

arr2 = []

for i in range(n2):
    num = int(input("Enter number: "))
    arr2.append(num)

union = []

for num in arr1:

    if num not in union:
        union.append(num)

for num in arr2:

    if num not in union:
        union.append(num)

print("Union:", union)