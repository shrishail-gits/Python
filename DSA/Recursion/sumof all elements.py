def sum(arr,i):
    if i==len(arr):
        return 0
    return arr[i]+sum(arr,i+1)
arr=list(map(int,input().split()))
print(sum(arr,0))