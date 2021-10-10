from tensorflow import keras

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.text import Tokenizer

model = keras.models.load_model('GRU_model.h5')
word_to_index = imdb.get_word_index()
tokenizer = Tokenizer()
max_len = 30