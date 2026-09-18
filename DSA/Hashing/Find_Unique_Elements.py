arr=list(map(int,input("Enter elements:").split()))
frequency={}
for element in arr:
    frequency[element]=frequency.get(element,0)+1
print("Unique element:")
for element,count in frequency.items():
    if count==1:
        print(element)