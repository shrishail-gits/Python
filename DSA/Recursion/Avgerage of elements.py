def total(arr,i):
    if i==len(arr):
        return 0
    return arr[i]+total(arr,i+1)
arr=list(map(int,input("Enter elements:").split()))
s=total(arr,0)
average=s/len(arr)
print("average=",average)