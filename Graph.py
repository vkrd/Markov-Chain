from Vertex import Vertex
import random
import pickle

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
        next_word = "." #self.generate_random_word()
        sentence = ""
        first_run = True
        while next_word != "." or first_run == True:
            first_run = False
            sentence += " " + next_word
            next_word = self.nodes[next_word].generate_next_word()
        return (sentence + " .").replace(" .",".")[2:]


    def generate_random_word(self):
        rand = random.randint(1,len(self.nodes))
        for key in self.nodes.keys():
            rand -= 1
            if rand <= 0:
                return key

    def save(self, filename):
        with open(filename,'wb') as outfile:
            pickle.dump(self.nodes,outfile)
            outfile.close()

    def load(self, filename):
        with open(filename,'rb') as infile:
            self.nodes = pickle.load(infile)
            infile.close()
