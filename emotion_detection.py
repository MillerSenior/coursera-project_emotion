from transformers import pipeline

# Load a local emotion classification model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")


def emotion_detector(text_to_analyse):
    """
    Uses a local Hugging Face Transformers model for emotion detection.

    Args:
        text_to_analyse (str): The input text to analyze.

    Returns:
        dict: The extracted emotion prediction results.
    """
    result = emotion_classifier(text_to_analyse)
    return result[0]  # Return the first result


# Example usage
#print(emotion_detector("I love this new technology."))
