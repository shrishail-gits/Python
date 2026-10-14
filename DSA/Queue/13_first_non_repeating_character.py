s=input("Enter the string:")
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1

queue=[]
for ch in s:
    queue.append(ch)
found=False
while len(queue)>0:
    ch=queue.pop(0)
    if count[ch]==1:
        print("First non-repeating character:",ch)
        found=True
        break
if not found:
    print("No non-repeating character")