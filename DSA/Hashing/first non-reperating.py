# n=int(input("Enter the number of element:"))
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
# found=False
# for num in arr:
#     if freq[num]==1:
#         print("First non repeating number=",num)
#         found=True
#         break
# else:
#      print("There is no non-repating element")
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    freq={}
    found=False
    for x in A:
        freq[x]=freq.get(x,0)+1
    for x in A:
        if freq[x]==1:
            print(x)
            found=True
            break
    if not found:
       print(-1)
