T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    slow=0
    for fast in range(1,N):
        if A[fast]!=A[slow]:
            slow+=1
            A[slow]=A[fast]
    print(slow + 1)
    print(*A[:slow + 1])

