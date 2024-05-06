class Dictionary:

    def __init__(self):
        self.words = set()

    def check(self, word):
        if word.lower() in self.words:
            return True
        else:
            return False

    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True

    def size(self):
        return len(self.words)

    def unload(self):
        return True
        
# Thanks for looking
