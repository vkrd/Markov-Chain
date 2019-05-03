from Vertex import Vertex
import numpy as np
from Graph import Graph
from keras.datasets import mnist
import matplotlib.pyplot as plt
import random
import pickle

(x_train, y_train), (x_test, y_test) = mnist.load_data()


print("data loaded")

training_digit = 9

class ImageConverter:
    def __init__(self):
        self.nodes = {}

    def generate_graph(self, i):
        if (y_train[i] == training_digit):
            for r in range(28):
                for c in range(28):
                    index = str(r) + "-" + str(c)
                    if not (index in self.nodes.keys()):
                        self.nodes[index] = Vertex(index)
                    self.nodes[index].add_node(x_train[i][r,c])

    def save(self, filename):
        with open("data\\" + filename,'wb') as outfile:
            pickle.dump(self.nodes,outfile)
            outfile.close()

    def load(self, filename):
        with open("data\\" + filename,'rb') as infile:
            self.nodes = pickle.load(infile)
            infile.close()

    def generate_image(self):
        ret_image = np.zeros((28,28))
        for r in range(28):
            for c in range(28):
                ret_image[r,c] = self.nodes[str(r) + "-" + str(c)].generate_next_word()
        return ret_image


graph = Graph()
im = ImageConverter()
for i in range(60000):
    im.generate_graph(i)
#im.load("digit0.dat")

im.save("digit" + str(training_digit) + ".dat")

plt.imshow(im.generate_image(), cmap='Greys')
plt.show()
