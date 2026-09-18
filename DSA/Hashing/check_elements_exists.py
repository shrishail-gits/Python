arr=list(map(int,input().split()))
target=int(input())
elements=set(arr)
if target in elements:
    print("Element exits")
else:
    print("Element does not exist")