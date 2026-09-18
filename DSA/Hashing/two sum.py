# n = int(input("Enter the number of elements: "))
# arr = []
# for i in range(n):
#     num = int(input("Enter the number: "))
#     arr.append(num)
# target = int(input("Enter the target: "))
# seen = {}
# index = 0
# found = False
# for num in arr:
#     needed = target - num
#     if needed in seen:
#         print("Pair found")
#         print("Indices:", seen[needed], index)
#         found = True
#         break
#     else:
#         seen[num] = index
#     index += 1
# if found == False:
#     print("Pair not found")
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    target=int(input())
    seen={}
    for i in range(N):
        x=A[i]
        complement=target-x
        if complement in seen:
            print(seen[complement],i)
            break
        seen[x]=i