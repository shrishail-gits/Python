arr=list(map(int,input().split()))
target=int(input())
prefix_sum=0
seen={0}
found=False
for element in arr:
    prefix_sum+=element
    if prefix_sum-target in seen:
        found=True
        break
    seen.add(prefix_sum)
if found:
    print("Subarray with given sum exists")
else:
    print("Subarray with given sum does not exist")