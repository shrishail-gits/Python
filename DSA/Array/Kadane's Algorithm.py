n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input("Enter the number:"))
    arr.append(num)
current_sum=0
max_sum=0
for i in range(1,n):
    current_sum=current_sum+arr[i]
    if current_sum<arr[i]:
        current_sum=arr[i]
    if current_sum>max_sum:
        max_sum=current_sum
print("Maximum subarray sum:",max_sum)