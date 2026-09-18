s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("Not Anagram")

else:

    visited = []
    anagram = True

    for i in range(len(s1)):

        if s1[i] in visited:
            continue

        count1 = 0
        count2 = 0

        for j in range(len(s1)):
            if s1[i] == s1[j]:
                count1 += 1

        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count2 += 1

        if count1 != count2:
            anagram = False
            break

        visited.append(s1[i])

    if anagram:
        print("Anagram")
    else:
        print("Not Anagram")