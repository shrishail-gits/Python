def count_digit(n, target):
    if n == 0:
        return 0

    digit = n % 10

    if digit == target:
        return 1 + count_digit(n // 10, target)

    return count_digit(n // 10, target)


n = int(input("Enter number: "))
target = int(input("Enter digit: "))

print("Count:", count_digit(n, target))