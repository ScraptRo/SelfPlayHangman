
class WordHint:
    def __init__(self, index: int, hint: str, word: str):
        self.mIndex: int = index 
        self.mWord = word
        self.mHint= hint
    def __str__(self):
        return f"Index: {self.mIndex}, Hint: {self.mHint}, Word: {self.mWord}\n"
    def __repr__(self):
        return f"Index: {self.mIndex}, Hint: {self.mHint}, Word: {self.mWord}\n"

#All words loaded from the file
loadedWords = [] 

def loadIntoBuffer():
    file = open("cuvinte_de_verificat.txt", "r", encoding='utf-8')
    for line in file:
        elements = line.split(';')
        loadedWords.append(WordHint(elements[0], elements[1], elements[2].rstrip()))
    file.close()
    
