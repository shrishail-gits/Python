
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    value = int(input("Enter value: "))
    arr.append(value)

k = int(input("Enter window size: "))

if k <= 0 or k > n:
    print("Invalid window size")
else:
    result = []

    for i in range(n - k + 1):
        maximum = arr[i]

        for j in range(i, i + k):
            if arr[j] > maximum:
                maximum = arr[j]

        result.append(maximum)

    print("Sliding window maximum:", result)
