arr=list(map(int,input().split()))
frequency={}
for element in arr:
    frequency[element]=frequency.get(element,0)+1
max_element=arr[0]
max_count=frequency[arr[0]]
for element in frequency:
    if frequency[element]>max_count:
        max_count=frequency[element]
        max_element=element
print("Element with maximum frequency:",max_element)
print("Frequency:",max_count)
