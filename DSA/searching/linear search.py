arr=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target:"))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index:",i)
        found=True
        break
if not found:
    print("Element not found")