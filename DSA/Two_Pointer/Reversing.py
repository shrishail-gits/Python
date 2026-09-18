T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    left=0
    right=N-1
    while left<right:
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1
    print(*A)
#                  FOR STRING
# s = input()
#
# A = list(s)
#
# left = 0
# right = len(A) - 1
#
# while left < right:
#     A[left], A[right] = A[right], A[left]
#     left += 1
#     right -= 1
#
# print("".join(A))
