FROM lukeroy/dbe-models:latest as data

# use tensorflow/tensorflow to run the flask server containing the trained Model
FROM tensorflow/tensorflow
# install dependancies
RUN pip install openpyxl numpy pandas matplotlib tensorflow-text flask Jinja2 waitress

RUN mkdir model
COPY --from=data /models/model_small_bert_bert_en_uncased_L-2_H-128_A-2_20221121-234352 /model/

RUN curl -o answers.json https://raw.githubusercontent.com/skywalkeretw/DBE-Humor-Prototype/master/Datasets/answers.json

# Copy html templates and static into container
COPY templates/ templates/
COPY static/ static/
# Copy python application into container
COPY main.py /main.py
# expose Application on port 8080 to be able to access the webapp
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]