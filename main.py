# Program that asks the user for a word to search for and the amount of flaws
# allowed. The file is searched for the words that match the input with x amount
# of flaws

def longest_common_substring(str1, str2, m, n):
 
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
 
    # L[m][n] contains length of LCS
    # for X[0..n-1] and Y[0..m-1]
    return L[m][n]

def isInRange(fileWord, word):
    leng = longest_common_substring(str1, str2, m, n)



# Get the parameters
input = input("Please enter your word to search for: ")


# Open file to start the search
f = open("examplefile.txt", "r").read().splitlines()

for word in f: # Each word in file
    pass