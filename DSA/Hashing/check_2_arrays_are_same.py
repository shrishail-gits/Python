arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
freq1={}
freq2={}
for element in arr1:
    freq1[element]=freq1.get(element,0)+1
for element in arr2:
    freq2[element]=freq2.get(element,0)+1
if freq1==freq2:
    print("Arrays are the same")
else:
    print("Arrays are not the same")