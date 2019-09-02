from Vertex import Vertex
import random
import pickle

class Graph:

    def __init__(self):
        self.nodes = {}

    def generate_graph(self, text):
        # split up the text by spaces to easily loop thru
        raw_text = text.split(" ")

        # loop through words and create Vertices and connections
        for i in range(len(raw_text)-1):
            char = raw_text[i]
            
            # check to see if Vertex already exists
            if not (char in self.nodes.keys()):
                # create new Vertex with word
                self.nodes[char] = Vertex(char)

            # increase the frequency count of the directed line from char to raw_text[i+1] by one
            self.nodes[char].add_node(raw_text[i + 1])

    def generate_graph_from_file(self, filename):
        f = open(filename, "r", encoding="utf8")

        # make substitutions to make sentences cleaner
        text = f.read().replace("\n"," ").replace("\r"," ").replace("."," .").replace("!"," !")

        f.close()
        self.generate_graph(text)

    def generate_sentence(self):
        # find first word by looking for words after periods
        next_word = "."
        sentence = ""
        first_run = True

        # build sentence until you run into a period
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
