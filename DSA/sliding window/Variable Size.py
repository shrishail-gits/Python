N=int(input())
A=list(map(int,input().split()))
K=int(input())
left=0
window_sum=0
max_length=0
for right in range(N):
    window_sum+=A[right]
    while window_sum>K:
        window_sum -=A[left]
        left+=1
    length=right-left+1
    if length>max_length:
        max_length=length
print(max_length)