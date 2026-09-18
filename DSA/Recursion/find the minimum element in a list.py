def minimum(arr,i):
    if i==len(arr)-1:
        return arr[i]
    return min(arr[i],minimum(arr,i+1))
arr=list(map(int,input().split()))
print(minimum(arr,0))

