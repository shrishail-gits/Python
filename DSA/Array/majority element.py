n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

found = False

for i in range(n):

    count = 0

    for j in range(n):

        if arr[i] == arr[j]:
            count += 1

    if count > n // 2:
        print("Majority element:", arr[i])
        found = True
        break

if found == False:
    print("No majority element")