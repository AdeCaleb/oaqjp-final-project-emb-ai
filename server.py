"""The server file"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion_Detector')

@app.route('/emotionDetector')
def emotion():
    """Emotion detector"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        result = "Invalid text! Try again."
    else:
        result = f"For the given statement, the system response\
         is 'anger': {response['anger']}, 'disgust':\
          {response['disgust']}, 'fear': {response['fear']},\
           'joy': {response['joy']} and 'sadness': {response['sadness']}.\
            The dominant emotion is {response['dominant_emotion']}."

    return result

@app.route("/")
def render_index_page():
    """Main"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
