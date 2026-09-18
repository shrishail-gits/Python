T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    seen = {0: -1}
    prefix = 0
    max_length = 0

    for i in range(N):
        prefix += A[i]
        needed = prefix - K

        if needed in seen:
            length = i - seen[needed]

            if length > max_length:
                max_length = length

        if prefix not in seen:
            seen[prefix] = i

    print(max_length)