class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ( '+self.meaning+' )'
flash = []
print("Welcome to flashcard application!")

while(True):
    word = input("enter the word you want to add to the flashcards: ")
    meaning = input("enter the meaning to the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 if you want another flashcard else enter 1: "))
    if(option):
        break
print("\nYour Flashcards")
for i in flash:
    print('>', i)