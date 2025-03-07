import requests
import json 

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers=headers)

    formatted = json.loads(response.text)
    formatted = formatted['emotionPredictions'][0]
    highest = 0
    highest_emotion = ""

    for emotion, score in formatted["emotion"].items():
        if highest < score :
            highest_emotion = emotion
            highest = score

    result = {}

    if response.status_code == 200:
        result = {
        'anger': formatted['emotion']['anger'],
        'disgust': formatted['emotion']['disgust'],
        'fear': formatted['emotion']['fear'],
        'joy': formatted['emotion']['joy'],
        'sadness': formatted['emotion']['sadness'],
        'dominant_emotion': highest_emotion
        }
    elif response.status_code == 500:
        result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }


    return result

