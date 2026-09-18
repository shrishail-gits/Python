def reverse(arr, i, result):
    if i < 0:
        return result

    result.append(arr[i])
    return reverse(arr, i - 1, result)


arr = list(map(int, input("Enter elements: ").split()))

result = reverse(arr, len(arr) - 1, [])
print(result)