FROM tensorflow/tensorflow
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY *.py /
ENTRYPOINT ["python", "/app.py"]