T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    K=int(input())
    left=0
    right=N-1
    found=False
    while left<right:
        total=A[left]+A[right]
        if total==K:
            found=True
            break
        elif total<K:
            left+=1
        else:
            right-=1
    if found:
        print("YES")
    else:
        print("NO")

