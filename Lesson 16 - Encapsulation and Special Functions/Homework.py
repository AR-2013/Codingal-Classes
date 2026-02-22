class String:
    def __init__(self):
        self.str = ""
    def GetString(self):
        self.str = input("Enter a sentence: ")
    def ReverseString(self):
        words = self.str.split()
        words.reverse()
        self.str = " ".join(words)
        print(self.str)
obj = String()
obj.GetString()
obj.ReverseString()