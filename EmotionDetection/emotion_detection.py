from transformers import pipeline

# Load a local emotion classification model
#emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
emotion_classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")


def emotion_detector(text_to_analyse):
    # Get the prediction from the model
    results = emotion_classifier(text_to_analyse)

    # Define the emotions we care about
    relevant_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    emotions = {emotion: 0.0 for emotion in relevant_emotions}  # Initialize with 0.0 scores

    # Convert model output into structured format
    for res in results:
        label = res["label"].lower()  # Ensure label is in lowercase
        if label in emotions:
            emotions[label] = res["score"]  # Store the confidence score

    # Determine the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Add dominant emotion to the result
    findings = {
        "emotions": emotions,
        "dominant_emotion": dominant_emotion
    }

    return findings


# Example usage
#print(emotion_detector("Make America great again"))

# Example Test Case
if __name__ == "__main__":
    text = "I am so happy I am doing this."
    result = emotion_detector(text)
    print(result)  # Expected dominant emotion: "joy"
