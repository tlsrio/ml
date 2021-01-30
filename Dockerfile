FROM tensorflow/tensorflow
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
