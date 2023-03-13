# Humorerkennung im Natural Language Processing (NLP)
### Hochschule Reutlingen  
### Master Digital Business Engineering


__Betreuerin:__ Prof. Dr. Elena Kuß  
__Projektteam:__ Maria Katharina Fürholzer, Gowseegan Kanagaratnam, Luke Roy, Lucas Schweizer  
__Zeitraum:__ März 2022 - März 2023

## Milestones des Projekts:
1.	Analyse von Humortheorien aus der Philosophie und Psychologie

    Etablierung von drei Humortheorien: Inkongruenztheorie, Überlegenheitstheorie, Entlastungstheorie
    Das eigene, menschliche Humorverständnis ist durch viele Faktoren geprägt (Kontext, Kultur, Nationalität, Alter, Bildung, Intelligenz..)
    Fazit: Humor ist sehr individuell und benötigt oft Vorwissen und logische Verknüpfungen
 
1.	Analyse der verschiedenen Ansätze der Humorerkennung in der Computerlinguistik 

    NLP = Natural Language Processing = ein Computer muss menschliche Sprache semantisch und kontextuell "verstehen" können
    Viele verschiedene Ansätze in der Computerlinguistik
    Weit verbreitet: BERT als Pre-Trained Language Model für NLP-Aufgaben

1.	Verstehen und Implementieren verschiedener Algorithmen 

    Training und Evaluation von Google BERT als Pre-trained Language Model mit TensorFlow als Deep Learning Classifier in Python zzgl. Implementierung einer prototypischen WebApp mit dem erfolgreichsten Modell.
    Trainieren von 26 Modellen mit einem unimodalen (textuellen) Datensatz (aufgrund Leistungsverfügbarkeit wurde kein multimodaler Datensatz gewählt). Die 26 Modelle bestehen aus sechs small_bert und einer ALBERT Konfigurationen [Bert](https://tfhub.dev/google/collections/bert/).

1.	Vergleich und Evaluation der Modelle

    Bestimmung eines finalen Testdatensatzes (30 Witze und 30 Aussagesätze)
    Testen der 26 Modelle mit finalem Testdatensatz 
    Einfache mathematische Berechnung zur Definition des besten Modells (siehe Präsentation und Excel-Datei)
    Modell gibt Prozentwert zurück, dieser gibt an, mit welcher Wahrscheinlichkeit es sich bei dem Satz um einen Witz handelt
    Anmerkungen zum Modell: englische Sprache verwenden, keine Unterscheidung von Groß- und Kleinbuchstaben, Schwarzer Humor und Inhalte zu Politik, Ethik, Religion werden neutral betrachtet

1.	Entwicklung der Webanwendung "JOKY"

    Link: [JOKY](https://humor-detector-bert.8kyziehrspg.eu-de.codeengine.appdomain.cloud/home)

    Die Anwendung braucht ein paar Sekunden bis Minuten, da sie bei Nichtbenutzung auf null herunterskaliert.  
    __Verwendung des besten Modells:__ model_small_bert_bert_en_uncased_L-2_H-128_A-2
    ### Funktionsweise
    1.	User tippen englischen Satz ein
    2.	Modell berechnet, mit welcher Wahrscheinlichkeit es sich bei der Eingabe um einen Witz bzw.
    nicht um einen Witz handelt
    3.	Direkte Ausgabe der Wahrscheinlichkeit und entsprechende schlagfertige Rückmeldung an die User
    ### Aktuell ist kein Filter für unangemessene Inhalte implementiert 
    
    % | Schlagfertige Antwort  | EmojiLink 
    --- | --- | ---
    0-10  | Why so serious?  | ![smiling-face-with-tea](https://em-content.zobj.net/thumbs/240/apple/325/smiling-face-with-tear_1f972.png)
    11-20 |	Pretty serious stuff you're telling me here. | ![](https://em-content.zobj.net/thumbs/240/apple/325/face-with-peeking-eye_1fae3.png)
    21-30 |	Did you copy that from Wikipedia or the news? | ![](https://em-content.zobj.net/thumbs/240/apple/325/nerd-face_1f913.png)
    31-40 |	This is not a real joke you are telling me here, is it? | ![](https://em-content.zobj.net/thumbs/240/apple/325/yawning-face_1f971.png )
    41-50 |	I don't get this joke...Maybe it's because it isn't one? | ![](https://em-content.zobj.net/thumbs/240/apple/325/face-with-raised-eyebrow_1f928.png)
    51-60 |	Well, you can let it pass as a joke. | ![](https://em-content.zobj.net/thumbs/240/apple/325/face-with-monocle_1f9d0.png)
    61-70 |	I also laughed a bit in 010100101 – Thank you! | ![](https://em-content.zobj.net/thumbs/240/apple/325/grinning-face-with-sweat_1f605.png)
    71-80 |	You are quite funny today! | ![](https://em-content.zobj.net/thumbs/240/apple/325/grinning-squinting-face_1f606.png)
    81-90 |	Haha, good joke, buddy! Keep up the good work! | ![](https://em-content.zobj.net/thumbs/240/apple/325/face-with-tears-of-joy_1f602.png)
    91-100 |	Damn, that‘s funny as hell! Have you ever tried a comedy career?  | ![](https://em-content.zobj.net/thumbs/240/apple/325/rolling-on-the-floor-laughing_1f923.png)

    ### LESSONS LEARNED: Inhaltliche Aspekte
    - NLP ist verdammt komplex! Humorerkennung ist noch komplexer!
    - Unsichere Interpretation der Genauigkeit, da BERT-Embeddings für uns eine nicht zu kontrollierende Blackbox sind und es sich um ein sehr subjektives Thema handelt
	- Durch die Nutzung von BERT ist ein genereller englischer Sprach- und Kultur-Bias zu erwarten
	- Durch die gelabelten Trainingsdaten (isJoke = TRUE / FALSE) wurde bereits ein spezifisches, subjektives Humorempfinden (= Bias) in das Modelltraining eingebracht
	- Auch eine menschliche Testgruppe (bspw. mittels Amazon Mechanical Turk) hätte keine 100% Genauigkeit beim Thema Humor

    ### LESSONS LEARNED: Technische Aspekte
    - Einbindung von NLP-Modellen bedarf großer Rechenleistung
	- Der INF-Server hatte für größere BERT-Modelle zu wenig Leistung
	- Auf der IBM Cloud mit GPUs (Danke an Lukes Manager bei IBM) konnte unser     automatisiertes Skript leider nicht adhoc initialisiert werden
	 -Ein remote Jupyter Notebook ist nicht ideal für den Use Case „Automatisiertes Training von ML-Modellen im Hintergrund“ 
     Zellen-Output geht verloren, siehe Restoring computation output after disconnect in Jupyter notebook
	- Wenig praxisnahe Dokumentation zur Optimierung von BERT in Zusammenspiel mit Tensor Flow


## Development 

### JokeAPI

Containerized Flask server that uses a Tensorflow to detect humor.
Model is trained during build step. And loaded when the server is started.

Build image from inside JokeAPI dir
```bash
docker build -t humor-prototype-1 .
```

Run the image locally 
```bash
docker run -p 8080:8080 humor-prototype-1
```

### JokeAPIBert

Containerized Flask server that uses a pre trained Bert  Model  from our `lukeroy/dbe-models:latest` image.
Detects if Senteces are Jokes or not.
There are 2 endpoints `/home` and `/joke`

Build image from inside JokeAPIBert dir
```bash
docker build -t humor-prototype-2-bert .
```

Run the image locally 
```bash
docker run -p 8080:8080 humor-prototype-2-bert
```

### scripts_and_snippets

Contains the notebooks, scripts and Dockerfiles used to generate and store our models and test them.

### Datasets

Contains all our Datasets and Datafiles used during the project

### experiments 

Contains all our experiments and test we did during development