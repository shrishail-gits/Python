n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

left = 0
right = n - 1

while left < right:

    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print("Reversed array =", arr)