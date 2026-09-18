s = input("Enter the string: ")

visited = []

for i in range(len(s)):

    if s[i] in visited:
        continue

    count = 0

    for j in range(len(s)):

        if s[i] == s[j]:
            count += 1

    print(s[i], "->", count)

    visited.append(s[i])