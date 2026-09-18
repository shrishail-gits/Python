def count_odd(arr,i):
    if i==len(arr):
        return 0
    if arr[i]%2!=0:
        return 1+count_odd(arr,i+1)
    return count_odd(arr,i+1)
arr=list(map(int,input("Enter elements:").split()))
print("odd numbers:",count_odd(arr,0))