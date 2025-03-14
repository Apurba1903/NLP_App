import requests

class API:
    
    def __init__(self):
        # Sentiment Analysis API
        self.sentiment_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"
        self.sentiment_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",
            "x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
        }

        # Named Entity Recognition (NER) API
        self.ner_url = "https://named-entity-extraction1.p.rapidapi.com/api/lingo"
        self.ner_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",
            "x-rapidapi-host": "named-entity-extraction1.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        # Emotion Analysis API
        self.emotion_url = "https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/"
        self.emotion_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",
            "x-rapidapi-host": "twinword-emotion-analysis-v1.p.rapidapi.com",
            "Content-Type": "application/x-www-form-urlencoded"
        }


    # Sentiment Analysis
    def sentiment_analysis(self, text):
        response = requests.get(self.sentiment_url, headers=self.sentiment_headers, params={"text": text})
        return response.json()

    # Named Entity Recognition (NER)
    def entity_extraction(self, text):
        payload = {
            "extractor": "en",
            "text": text
        }
        response = requests.post(self.ner_url, json=payload, headers=self.ner_headers)
        return response.json()

    # Emotion Analysis
    def emotion_analysis(self, text):
        payload = {"text": text}
        response = requests.post(self.emotion_url, data=payload, headers=self.emotion_headers)
        return response.json()