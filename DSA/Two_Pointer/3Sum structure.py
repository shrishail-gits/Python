T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    A.sort()
    count = 0

    for i in range(N - 2):

        # Skip duplicate fixed elements
        if i > 0 and A[i] == A[i - 1]:
            continue

        left = i + 1
        right = N - 1

        while left < right:
            total = A[i] + A[left] + A[right]

            if total == K:
                count += 1

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and A[left] == A[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and A[right] == A[right + 1]:
                    right -= 1

            elif total < K:
                left += 1

            else:
                right -= 1

    print(count)