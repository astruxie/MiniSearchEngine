# Program that asks the user for a word to search for and the amount of flaws
# allowed. The file is searched for the words that match the input with x amount
# of flaws
from queue import Queue

# Get the parameters
input = input("Please enter your word to search for: ")

#variables
inputQ = Queue(maxsize = len(input))

# Size check
if (len(input) > 8):
    print("This word is too big!")

# Put input into stack
for letter in reversed(input):
    inputQ.put(letter)


# Open file to start the search
f = open("examplefile.txt", "r").read().splitlines()

for word in f: # Each word in file
    #only words that are the correct size are worth checking
    if word < (len(input) + flaws) or word > (len(input) - flaws):
        #comapre each digit
        for i, letter in enumerate(word):

    
