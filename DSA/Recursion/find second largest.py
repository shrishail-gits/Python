def maximum(arr,i):
    if i==len(arr)-1:
        return arr[i]
    return max(arr[i],maximum(arr,i+1))
def second_largest(arr,i,larget):
    if i==len(arr):
        return -float("inf")
    if arr[i]<largest:
        return max(arr[i],second_largest(arr,i+1,largest))
    return second_largest(arr,i+1,largest)
arr=list(map(int,input("Enter elements:").split()))
largest=maximum(arr,0)
second=second_largest(arr,0,largest)
print("Second largest:",second)
