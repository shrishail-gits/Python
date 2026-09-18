def decimal_to_binary(n):
    if n == 0:
        return

    decimal_to_binary(n // 2)
    print(n % 2, end="")


n = int(input("Enter decimal number: "))

if n == 0:
    print(0)
else:
    decimal_to_binary(n)