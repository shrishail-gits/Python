arr=list(map(int,input().split()))
numbers=set(arr)
longest=0
for num in numbers:
    if num -1 not in numbers:
        current=num
        length=1
        while current+1 in numbers:
            current+=1
            length+=1
        longest=max(longest,length)
print("longest consecutive sequence length:",longest)
