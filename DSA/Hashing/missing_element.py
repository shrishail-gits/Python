arr=list(map(int,input().split()))
n=int(input())
numbers=set(arr)
for i in range(1,n+1):
    if i not in numbers:
        print("Missing element:",i)
        break