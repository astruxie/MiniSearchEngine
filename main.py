# Program that asks the user for a word to search for and the amount of flaws
# allowed. The file is searched for the words that match the input with x amount
# of flaws

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

# Variables
similarWords = []
# Get the parameters
input = input("Please enter your word to search for: ")

# Open file to start the search
f = open("examplefile.txt", "r").read().splitlines()

# Check each word in the file & add it to the list if 
# it has 2 or less total insertions and deletions
for word in f: 
    # Ignore words that are too large or small - hopefully saving time
    if len(word) <= (len(input) + 2) and len(word) >= (len(input) - 2):
        if isWordWithinRange(word, input):
            similarWords.append(word)
