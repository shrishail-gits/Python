# n = int(input("Enter the number of elements: "))
# arr = []
# for i in range(n):
#     num = int(input("Enter the number: "))
#     arr.append(num)
# target = int(input("Enter the target: "))
# seen = {}
# count = 0
# for num in arr:
#     needed = target - num
#     if needed in seen:
#         count += seen[needed]
#     if num in seen:
#         seen[num] += 1
#     else:
#         seen[num] = 1
# print("Number of pairs =", count)
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    K=int(input())
    freq={}
    count=0
    for x in A:
        complement=K-x
        if complement in freq:
            count+=freq[complement]
        freq[x]=freq.get(x,0)+1
    print(count)