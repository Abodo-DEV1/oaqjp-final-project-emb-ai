
import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    # Custom header specifying the model ID for the detector emotion service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    # Sending a POST request to the detector emotion API
    response = requests.post(url, json=myobj, headers=header)
    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        anger = formatted_response['emotionPredictions'][0]["emotion"]["anger"]
        disgust = formatted_response['emotionPredictions'][0]["emotion"]["disgust"]
        fear = formatted_response['emotionPredictions'][0]["emotion"]["fear"]
        joy = formatted_response['emotionPredictions'][0]["emotion"]["joy"]
        sadness = formatted_response['emotionPredictions'][0]["emotion"]["sadness"]
        dominant_emotion_result = dominant_emotion(**{'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness})

    # If the response status code is 400, set emotions to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion_result = None

    # Returning a dictionary containing emotion detector results
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion_result}

def dominant_emotion(**kargs):
    best_score = -1 
    res = ""
    for key, value in kargs.items():
        if value > best_score : 
            res = key 
            best_score = value
    return res         


