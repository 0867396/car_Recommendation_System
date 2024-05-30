import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def get_label_prediction(description):

    # Inlezen van het JSON-bestand
    with open('data.json') as json_file:
        auto_beschrijvingen_per_label = json.load(json_file)

    beschrijvingen = []
    labels = []

    # Loop door de gegevens en verzamel de beschrijvingen en labels
    for label, beschrijvingen_voor_label in auto_beschrijvingen_per_label.items():
        beschrijvingen.extend(beschrijvingen_voor_label)  # Selecteer slechts 10 beschrijvingen per label
        labels.extend([label] * len(beschrijvingen_voor_label))

    # TF-IDF vectorizer TF-IDF Vectorizer is a measure of originality of a word by comparing the number of times a word appears in document with the number of documents the word appears in.
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(beschrijvingen)

    # Train een Naive Bayes classificatiemodel
    model = MultinomialNB()
    model.fit(X, labels)
    
    # Verwerk de nieuwe tekst
    input_vector = vectorizer.transform([description])

    # Doe een voorspelling
    voorspelde_label = model.predict(input_vector)

    print("Label:", voorspelde_label[0])

    return voorspelde_label
