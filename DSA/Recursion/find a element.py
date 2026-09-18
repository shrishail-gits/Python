def search(arr,target,i):
    if i==len(arr):
        return -1
    if arr[i]==target:
        return i
    return search(arr,target,i+1)
arr=list(map(int,input().split()))
target=int(input())
result=search(arr,target,0)
if result==-1:
    print("Element not found")
else:
    print("Element found at index",result)
