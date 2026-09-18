N=int(input())
A=list(map(int,input().split()))
K=int(input())
window_sum=sum(A[:K])
max_sum=window_sum
for i in range(K,N):
    window_sum=window_sum-A[i-K]+A[i]
    if window_sum > max_sum:
        max_sum=window_sum
print(max_sum)