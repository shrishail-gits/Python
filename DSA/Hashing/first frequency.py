n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter the number:"))
    arr.append(num)
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
found=False
for num in arr:
    if freq[num]>1:
        print("First repeating element=",num)
        found=True
        break
if found==False:
    print("No repeating element")

