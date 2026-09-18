T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    left=0
    right=N-1
    max_area=0
    while left<right:
        area=(right-left)*min(A[left],A[right])
        if area>max_area:
            max_area=area
        if A[left]<A[right]:
            left+=1
        else:
            right-=1
    print(max_area)