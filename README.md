# falsk-ml-model-api
## Project Setup
### Build Docker Image
```shell
$ docker build -t myapp .
```

## Project Start
```shell
$ docker run -v /:/app -p 5000:5000 myapp
```