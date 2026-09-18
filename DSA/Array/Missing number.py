n = int(input("Enter n: "))

arr = []

for i in range(n - 1):
    num = int(input("Enter number: "))
    arr.append(num)

expected = n * (n + 1) // 2

actual = 0

for num in arr:
    actual += num

missing = expected - actual

print("Missing number =", missing)