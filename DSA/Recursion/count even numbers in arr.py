def count_even(arr,i):
    if i==len(arr):
        return 0
    if arr[i]%2==0:
        return 1+count_even(arr,i+1)
    return count_even(arr,i+1)
arr=list(map(int,input("Enter elements:").split()))
print("Even numbers:",count_even(arr,0))