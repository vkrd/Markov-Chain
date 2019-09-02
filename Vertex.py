import random

class Vertex:
    def __init__(self, word):
        self.word = word
        self.total = 0
        self.word_counts = {}

    def add_node(self, consec_word):
        
        if consec_word in self.word_counts:
            # if word is already connected, increase frequency
            self.word_counts[consec_word] = self.word_counts[consec_word] + 1
        else:
            # if word is not connected, add it to connected Vertices
            self.word_counts[consec_word] = 1

        # update total to make probability calculation easier
        self.total += 1

    def generate_next_word(self):
        # choose random Vertex from connected Vertices
        rand = random.randint(1,self.total)
        
        for key, value in self.word_counts.items():
            rand -= value
            if rand <= 0:
                return key

        # if word has no outgoing edges, return a period
        return "."

    def getWords(self):
        return self.word_counts
