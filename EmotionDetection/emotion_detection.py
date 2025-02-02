from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

try:
    print("🚀 Loading the model...")
    emotion_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Model loading failed: {e}")


def emotion_detector(text_to_analyse):
    try:
        labels = ["anger", "disgust", "fear", "joy", "sadness"]
        results = emotion_classifier(text_to_analyse, candidate_labels=labels)

        # Map emotions and scores correctly
        emotions = {label: score for label, score in zip(results["labels"], results["scores"])}

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Ensure a proper response
        response_text = f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."

        return {
            "emotions": emotions,
            "dominant_emotion": dominant_emotion,
            "response": response_text
        }
    except Exception as e:
        print(f"❌ ERROR processing text: {text_to_analyse}\n{e}")
        return {"error": str(e)}


@app.route("/")
def index():
    return "Emotion Detector API Running!"


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text = request.json.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        result = emotion_detector(text)
        return jsonify(result)
    except Exception as e:
        print(f"❌ ERROR in API: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
