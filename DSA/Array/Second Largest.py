n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

largest = float('-inf')
second = float('-inf')

for num in arr:

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Largest =", largest)
print("Second Largest =", second)