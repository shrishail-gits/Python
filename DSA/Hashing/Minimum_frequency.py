arr=list(map(int,input("Enter elements:").split()))
frequency={}
for element in arr:
    frequency[element]=frequency.get(element,0)+1
min_element=arr[0]
min_count=frequency[arr[0]]
for element in frequency:
    if frequency[element]<min_count:
        min_count=frequency[element]
        min_element=element
print("Element with minimum frequency:",min_element)
print("Frequency:",min_count)
