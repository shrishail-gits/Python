n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter the number:"))
    arr.append(num)
freq={}
for num in arr:
    if num in freq:
        print("Duplicate Found:",num)
        freq[num] += 1
    else:
        freq[num]=1
        print("First time:",num)
# T=int(input())
# for _ in range(T):
#    N=int(input())
#    A=list(map(int,input().split()))
#    seen=set()
#    duplicate=False
#    for x in A:
#        if x in seen:
#            duplicate=True
#            break
#        seen.add(x)
#    if duplicate:
#        print("Duplicate")
#    else:
#        print("No Duplicate")

