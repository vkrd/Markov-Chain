from Vertex import Vertex
import random

class Graph:

    def __init__(self):
        self.nodes = {}

    def generate_graph(self, text):
        raw_text = text.split(" ")
        for i in range(len(raw_text)-1):
            char = raw_text[i]
            if not (char in self.nodes.keys()):
                self.nodes[char] = Vertex(char)
            self.nodes[char].add_node(raw_text[i + 1])

    def generate_graph_from_file(self, filename):
        f = open(filename, "r", encoding="utf8")
        text = f.read().replace("\n"," ").replace("\r"," ").replace("."," .").replace("!"," !")
        f.close()
        self.generate_graph(text)

    def generate_sentence(self):
        next_word = self.generate_random_word()
        sentence = ""
        while next_word != ".":
            sentence += " " + next_word
            next_word = self.nodes[next_word].generate_next_word()

        return sentence + "."


    def generate_random_word(self):
        rand = random.randint(1,len(self.nodes))
        for key in self.nodes.keys():
            rand -= 1
            if rand <= 0:
                return key

pot = Graph()
pot.generate_graph_from_file("data.txt")
print(pot.generate_sentence())
