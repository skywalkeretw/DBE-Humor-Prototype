FROM lukeroy/dbe-models:latest as data
FROM tensorflow/tensorflow

RUN mkdir models

COPY --from=data /models /models/

RUN curl -o /models/ourExamples.csv https://raw.githubusercontent.com/skywalkeretw/DBE-Humor-Prototype/master/Datasets/ourExamples.csv
RUN pip install openpyxl numpy pandas matplotlib tensorflow-text==2.10.0

COPY eval.py /models/
WORKDIR /models

ENTRYPOINT [ "python3", "/models/eval.py" ]