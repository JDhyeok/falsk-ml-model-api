FROM tensorflow/tensorflow

# COPY ./app /app

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=development

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run" ]