FROM tensorflow/tensorflow
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD ./app /app
WORKDIR /app
ENTRYPOINT [ "python", "app.py" ]
