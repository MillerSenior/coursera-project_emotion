from flask import Flask, request, jsonify, render_template

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")  # Serves the provided frontend UI


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    API endpoint to detect emotions in user input.
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input, please provide 'text' field"}), 400

    text_to_analyze = data["text"]

    # Get emotion analysis results
    results = emotion_detector(text_to_analyze)
    print("Raw Model Output:", results)

    # Formatting the response as required
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {results['emotions']['anger']}, "
        f"'disgust': {results['emotions']['disgust']}, "
        f"'fear': {results['emotions']['fear']}, "
        f"'joy': {results['emotions']['joy']}, "
        f"and 'sadness': {results['emotions']['sadness']}. "
        f"The dominant emotion is {results['dominant_emotion']}."
    )

    return jsonify({"response": response_message, **results})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
