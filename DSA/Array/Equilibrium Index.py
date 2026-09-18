n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

found = False

for i in range(n):

    left_sum = 0
    right_sum = 0

    for j in range(i):
        left_sum = left_sum + arr[j]

    for j in range(i + 1, n):
        right_sum = right_sum + arr[j]

    if left_sum == right_sum:
        print("Equilibrium index:", i)
        found = True

if found == False:
    print("No equilibrium index")