# n=int(input("Enter the number of elements:"))
# arr=[]
# for i in range(n):
#     num=int(input("Enter the number:"))
#     arr.append(num)
# freq={}
# for num in arr:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
# for num in freq:
#     print(num,"->",freq[num])
arr=list(map(int,input("Enter elements:").split()))
frequency={}
for element in arr:
    if element in frequency:
        frequency[element]+=1
    else:
        frequency[element]=1
for element,count in frequency.items():
    print(element,"->",count)
