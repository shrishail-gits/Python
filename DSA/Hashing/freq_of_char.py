# s=input("Enter a string:")
# frequency={}
# for ch in s:
#     if ch in frequency:
#         frequency[ch]+=1
#     else:
#         frequency[ch]=1
# for ch,count in frequency.items():
#     print(ch,"->",count)
arr=list(map(int,input().split()))
frequency={}
for element in arr:
    frequency[element]=frequency.get(element,0)+1
print("Duplicate elements:")
for element,count in frequency.items():
    if count>1:
        print(element)