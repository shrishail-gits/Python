def count_occurrences(arr,target,i):
    if i==len(arr):
        return 0
    if arr[i]==target:
        return 1+count_occurrences(arr,target,i+1)
    return count_occurrences(arr,target,i+1)
arr=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target:"))
print(count_occurrences(arr,target,0))