def count_positive(arr,i):
    if i==len(arr):
        return 0
    if arr[i]>0:
        return 1+count_positive(arr,i+1)
    return count_positive(arr,i+1)
arr=list(map(int,input("Enter elements").split()))
print("positive number:",count_positive(arr,0))