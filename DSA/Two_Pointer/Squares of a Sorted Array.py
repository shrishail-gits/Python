N=int(input())
A=list(map(int,input().split()))
left=0
right=N-1
result=[0]*N
position=N-1
while left<=right:
    if abs(A[left])>abs(A[right]):
        result[position]=A[left]*A[left]
        left+=1
    else:
        result[position]=A[right]*A[right]
        right-=1
    position -=1
print(*result)
