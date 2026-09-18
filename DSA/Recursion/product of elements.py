def product(arr,i):
    if i==len(arr):
        return 1
    return arr[i]*product(arr,i+1)
arr=list(map(int,input().split()))
print(product(arr,0))