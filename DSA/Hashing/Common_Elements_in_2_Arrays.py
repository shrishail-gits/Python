arr1=list(map(int,input("Enter first array:").split()))
arr2=list(map(int,input("Enetr the 2nd array:").split()))
set1=set(arr1)
common=set()
for element in arr2:
    if element in set1:
        common.add(element)
print("common elements:",list(common))