# -----------------------------------------------------------
# Program that searches a file for a user-specified word &
# returns all the words with maximum 2 total
# insertions and deletions (in no particular order)
#
# Samantha Noggle
# -----------------------------------------------------------
from timeit import default_timer as timer

def longest_common_subsequence(str1, str2, x, y):
 
    L = [[0 for i in range(y + 1)]
         for i in range(x + 1)]
 
    # Build the grid to compare each letter in the two words
    # L[i][j] contains length of LCS of string1[0...i-1] and string[0...j-1]
    # L[x][y] contains the length of the longest common subsequnece
    for i in range(x + 1):
        for j in range(y + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif(str1[i - 1] == str2[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    # Return length of longest common subsequence
    return L[x][y]

def isWordWithinRange(str1, str2):
    leng = longest_common_subsequence(str1, str2, len(str1), len(str2))
    deletions = len(str1) - leng
    insertions = len(str2) - leng

    if (insertions + deletions) > 2:
        return False
    else:
        return True

# Driver code

similarWords = []

input = input("Please enter your word to search for: ")

f = open("english_words.txt", "r").read().splitlines()

start = timer()

# Check each word in the file & add it to the list if 
# it has 2 or less total insertions and deletions
for word in f: 
    # Ignore words that are too large or small - hopefully saving time
    if len(word) <= (len(input) + 2) and len(word) >= (len(input) - 2):
        if isWordWithinRange(word, input):
            similarWords.append(word)

end = timer()

# Print in no particular order with duplicates allowed
print("{0} results found in {1} seconds!".format(len(similarWords), (end - start)))
for x in similarWords:
    print(x)
