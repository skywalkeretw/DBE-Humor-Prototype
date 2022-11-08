FROM tensorflow/tensorflow

# install dependancies
RUN pip install flask && pip install pandas

# Copy html templates into container
COPY templates/ templates/
# Copy python application into container
COPY main.py /main.py
# Copy dataset into container
COPY dataset.csv /dataset.csv

# expose Application on port 8080 to be able to access the webapp
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]