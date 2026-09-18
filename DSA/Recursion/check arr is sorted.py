def is_sorted(arr, i):
    if i == len(arr) - 1:
        return True

    if arr[i] > arr[i + 1]:
        return False

    return is_sorted(arr, i + 1)


arr = list(map(int, input("Enter elements: ").split()))

if is_sorted(arr, 0):
    print("Sorted")
else:
    print("Not Sorted")