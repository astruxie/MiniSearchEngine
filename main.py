# Program that searches a file for a user-specified word
# returning all the words with maximum 2 total
# insertions and deletions (in no particular order)
from timeit import default_timer as timer

def longest_common_subsequence(str1, str2, m, n):
 
    L = [[0 for i in range(n + 1)]
         for i in range(m + 1)]
 
    # Following steps build L[m+1][n+1]
    # in bottom up fashion. Note that
    # L[i][j] contains length of LCS
    # of str1[0..i-1] and str2[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif(str1[i - 1] == str2[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    # Return length of LCS
    return L[m][n]

def isWordWithinRange(str1, str2):
    leng = longest_common_subsequence(str1, str2, len(str1), len(str2))
    deletions = len(str1) - leng
    insertions = len(str2) - leng
    total = insertions + deletions
    if total > 2:
        return False
    else:
        return True

# Variables
similarWords = []
# Get the parameters
input = input("Please enter your word to search for: ")

# Open file to start the search
f = open("english_words.txt", "r").read().splitlines()

# Timing the search
start = timer()

# Check each word in the file & add it to the list if 
# it has 2 or less total insertions and deletions
for word in f: 
    # Ignore words that are too large or small - hopefully saving time
    if len(word) <= (len(input) + 2) and len(word) >= (len(input) - 2):
        if isWordWithinRange(word, input):
            similarWords.append(word)

# Timing the search
end = timer()

# Print results in no particular order with duplicates
print("{0} results found in {1} seconds!".format(len(similarWords), (end - start)))
for x in similarWords:
    print(x)
