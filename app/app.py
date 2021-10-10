import re

from flask import Flask, jsonify, request
from tensorflow.keras.preprocessing.sequence import pad_sequences

from static import model, word_to_index, tokenizer, max_len

app = Flask(__name__)


@app.route('/api')
def hello():
    """
    test
    """
    return "Hello World"


@app.route('/api/predict', methods=["GET", "POST"])
def predict():
    """
    Predict sentiment of movie review
    """
    pred = []

    params = request.json

    if(params == None):
        params = request.args

    if(params != None):
        print(params['contents'])

        pad_new = sentiment_predict(params['contents'])
        score = float(model.predict(pad_new))

        pred.append("Positive" if score > 0.5 else "Negative")
        pred.append(score * 100 if score > 0.5 else (1 - score) * 100)

    return jsonify(
        sentiment=pred[0],
        score=pred[1]
    )


def to_lowercase(sentence):
    sentence = re.sub('[^0-9a-zA-Z ]', '', sentence).lower()
    return sentence


def encoding(sentence):
    encoded = []

    for word in sentence.split():
        try:
            if word_to_index[word] <= 1000:
                encoded.append(word_to_index[word] + 3)
            else:
                encoded.append(2)
        except KeyError:
            encoded.append(2)

    return encoded


def sentiment_predict(sentence):
    """
    text preprocessing
    """
    pred = []

    sentence = to_lowercase(sentence)
    encoded = encoding(sentence)
    pad_new = pad_sequences([encoded], maxlen=max_len)  # 패딩

    return pad_new


if __name__ == "__main__":
    app.run(debug=True)
