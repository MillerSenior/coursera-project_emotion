import pytest

from EmotionDetection import emotion_detector

# Define test cases: (input_text, expected_dominant_emotion)
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]


@pytest.mark.parametrize("text, expected_emotion", test_cases)
def test_emotion_detector(text, expected_emotion):
    result = emotion_detector(text)
    assert result[
               "dominant_emotion"] == expected_emotion, f"Expected '{expected_emotion}', but got '{result['dominant_emotion']}'"
