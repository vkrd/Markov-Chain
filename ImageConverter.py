from PIL import Image
import numpy as np
from Graph import Graph
import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print("data loaded")

class ImageConverter:
    def convert(self, filename):
        img = Image.open(filename)
        img.load()
        #Black and white imort
        data = np.asarray(img,dtype="int32")
        return ' '.join(data[:25,:25].ravel().astype(str))

graph = Graph()
im = ImageConverter()

graph.generate_graph(im.convert("bwcliff.jpg"))

graph.save("digits.dat")
