# Use tensorflow/tensorflow as Trainer Image to train the model 
FROM tensorflow/tensorflow AS trainer

# install dependancies
RUN pip install flask && pip install pandas

# Copy dataset into container
COPY dataset.csv /dataset.csv

COPY train.py /train.py

RUN python train.py



# use tensorflow/tensorflow to run the flask server containing the trained Model 
FROM tensorflow/tensorflow

# install dependancies
RUN pip install flask && pip install pandas

# Copy html templates into container
COPY templates/ templates/
# Copy python application into container
COPY main.py /main.py
COPY --from=trainer joke/ joke/ 
COPY --from=trainer tokenizer.pickle tokenizer.pickle
# expose Application on port 8080 to be able to access the webapp
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]
