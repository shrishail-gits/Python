words=input("Enter words:").split()
groups={}
for word in words:
    key="".join(sorted(word))
    if key not in groups:
        groups[key]=[]
    groups[key].append(word)
print("Anagram groups:")
for group in groups.values():
    print(group)