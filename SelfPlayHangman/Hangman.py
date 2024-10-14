from wordLoader import loadIntoBuffer
from wordLoader import loadedWords
import wordLoader

def getKnowLetterIndex(word_pattern: str) -> list[int]:
    return [i for i, char in enumerate(word_pattern) if char != '*']

wordChosen: wordLoader.WordHint
totalHint = 0

def getHint(letter):
    global totalHint
    totalHint += 1
    return [i for i, char in enumerate(wordChosen.mWord) if char == letter]

def resolveHangman(hint):
    askCounter = 0
    lastLetterQ = ''
    possibleWords = [x.mWord for x in loadedWords if len(x.mHint) == len(hint)]
    knowLetters = getKnowLetterIndex(hint)
    possibleWords = [word for word in possibleWords if all(word[index] == hint[index] for index in knowLetters)]
    while True:
        if len(possibleWords) == 1:
            askCounter += 1
            global totalHint
            totalHint += 1
            print("Your word is:" + str(possibleWords))
            print("The word was found in: " + str(askCounter) + "trys")
            break
        else:
            lastLetterQ = possibleWords[0][askCounter]
            lettersFound = getHint(lastLetterQ)
            possibleWords = [word for word in possibleWords if all(word[index] == lastLetterQ for index in lettersFound)]
            askCounter += 1

if __name__ == "__main__":
    print("Welcome to self play hangman!")
    print("The game where YOU chose the word and the computer try to find it")
    print("First, let's import the words!")
    
    loadIntoBuffer()
    print("Number of words: " + str(len(loadedWords)))
            
    print("Let's begin!")
    for word in loadedWords:
        wordChosen = word
        resolveHangman(wordChosen.mHint)
    print("The list was terminated in: " + str(totalHint) + " hints")
