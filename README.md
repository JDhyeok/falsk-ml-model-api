# falsk-ml-model-api

## Installation
```
$ git clone https://github.com/JDhyeok/falsk-ml-model-api.git
```

## Project Setup

- Build docker image
    ```shell
    $ docker-compose build
    ```

## Project Start

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
Ref.
