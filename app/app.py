import re

from flask import Flask, jsonify, request
from tensorflow.keras.preprocessing.sequence import pad_sequences

from static import model, word_to_index, tokenizer, max_len

app = Flask(__name__)


@app.route('/api')
def hello():
    """
    api test
    """
    return "Hello World"


@app.route('/api/predict', methods=["GET", "POST"])
def predict():
    """
    Predict sentiment of movie review
    """

    data = {"success": False}
    params = request.json
    score = 0

    if(params == None):
        params = request.args

    if(params != None):
        data["response"] = params.get("msg")
        data["success"] = True

        print(params['contents'])

        score = sentiment_predict(params['contents'])

    return jsonify(str(score))


def sentiment_predict(sentence):
    """
    
    """
    # 알파벳과 숫자를 제외하고 모두 제거 및 알파벳 소문자화
    sentence = re.sub('[^0-9a-zA-Z ]', '', sentence).lower()

    # 정수 인코딩
    encoded = []
    for word in sentence.split():
        # 단어 집합의 크기를 10,000으로 제한.
        try:
            if word_to_index[word] <= 10000:
                encoded.append(word_to_index[word]+3)
            else:
                # 10,000 이상의 숫자는 <unk> 토큰으로 취급.
                encoded.append(2)
            # 단어 집합에 없는 단어는 <unk> 토큰으로 취급.
        except KeyError:
            encoded.append(2)

    pad_new = pad_sequences([encoded], maxlen=max_len)  # 패딩
    score = float(model.predict(pad_new))  # 예측
    pred = []
    pred.append("Positive" if score > 0.5 else "Negative")
    pred.append(score * 100 if score > 0.5 else (1 - score) * 100)

    return pred


if __name__ == "__main__":
    """
    start flask server
    """
    app.run(debug=True)
