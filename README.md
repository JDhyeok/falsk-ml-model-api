# falsk-ml-model-api

## Installation
### Source Code
```
$ git clone https://github.com/JDhyeok/falsk-ml-model-api.git
```

## Project Setup/Start

### Dependency
- Docker (Optional)
- Tensorflow
- Keras
- Python >= 3.x

### Option1 - Local

- Setup virtual environment
    ```shell
    $ virtualenv venv
    ```
- Start python virtual environment
   ```shell
   $ .\venv\Script\activate
   # or source .\venv\Script\activate
   ```

- Install dependencies
    ```shell
    $ pip install -r requirements
    ```

- Start Flask server
    ```shell
    $ cd app
    $ flask run
    ```

### Option2 - Docker
- Build docker image
    ```shell
    $ docker-compose build
    ```

- Start docker container
    ```shell
    $ docker-compose up
    ```

### Request
You can use cURL examples below or use third party application such as PostMan.

- api test
    ```shell
    $ curl http://localhost:5000/api
    ```

- Predict sentiment score
    ```shell
    $ curl -X GET -H "Content-Type: application/json" --data '{"contents":"It is the best movie i've ever seen in my whole life"}' http://localhost:5000/api/predict
    ``` 

- Response JSON example
    ```json
    {
        sentiment: "Positive"
        score: 95.1245
    }
    ```
# Ref.
http://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf

https://www.kaggle.com/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews
