# Joke detection api

implemented as docker container using a flask api and tensorflow nlp

This a a simple Flask API inside a docker container.
The Base image for the container is `tensorflow/tensorflow`


Aktuelle version laufen lassen
```bash
docker run -p 8080:8080 lukeroy/humor-prototype-2-bert:latest
```
Humor detector zum testen bauen 
```bash
docker build -t humordetector .
```

lokale version starten zum testen 
```bash
docker run --rm -p 8080:8080 humordetector
```