s1=input()
s2=input()
frequency1={}
frequency2={}
for ch in s1:
    frequency1[ch]=frequency1.get(ch,0)+1
for ch in s2:
    frequency2[ch]=frequency2.get(ch,0)+1
if frequency1==frequency2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")