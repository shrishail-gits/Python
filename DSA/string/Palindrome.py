s = input("Enter the string:")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]

if reverse == s:
    print("Palindrome")
else:
    print("Not palindrome")