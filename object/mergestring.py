# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.

def mergeAlternately(word1, word2):
    merge = taille = ""
    j = 0
    if word1 == word2:
        taille = "same"
    for i in range(len(word1)):
        merge += word1[i]
        while (j != len(word2)):
            merge += word2[j]
            j += 1
            break
    if taille == "same":
        return merge
    while (j != len(word2)):
        merge += word2[j]
        j += 1
    return merge


print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))
