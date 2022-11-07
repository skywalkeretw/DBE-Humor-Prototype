FROM tensorflow/tensorflow

RUN pip install flask && pip install pandas

COPY main.py /main.py
COPY dataset.csv /dataset.csv
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]