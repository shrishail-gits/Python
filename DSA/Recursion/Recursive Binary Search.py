def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    return binary_search(arr, target, mid + 1, high)


arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter target: "))

result = binary_search(arr, target, 0, len(arr) - 1)

if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)