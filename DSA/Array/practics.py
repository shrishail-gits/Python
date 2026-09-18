n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

largest = arr[0]
smallest=arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
        largest=num

    if arr[i]<smallest:
        smallest=arr[i]
        smallest=num
print("Smallest=",smallest)
print("Largest =", largest)