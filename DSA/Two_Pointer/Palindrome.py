T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    left=0
    right=N-1
    found=True
    while left<right:
        if A[left]!=A[right]:
            found=False
            break
        left+=1
        right+=1
    if found:
        print("yes")
    else:
        print("no")
