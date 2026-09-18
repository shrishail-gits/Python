T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    slow=0
    for fast in range(N):
        if A[fast]!=0:
            A[slow],A[fast]=A[fast],A[slow]
            slow+=1

    print(*A)