s=input("Enter the string:")
unique=""
for ch in s:
    if ch not in unique:
        unique=unique+ch
print(unique)