N=int(input())
A=list(map(int,input().split()))
K=int(input())
X=int(input())
window_sum=sum(A[:K])
count=0
if window_sum>X:
    count+=1
for i in range(K,N):
    window_sum=window_sum-A[i-K]+A[i]
    if window_sum>X:
        count+=1
print(count)
