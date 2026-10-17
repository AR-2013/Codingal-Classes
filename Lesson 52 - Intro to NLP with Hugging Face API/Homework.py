import requests

API_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"

HF_API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def classify_message(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        predictions = response.json()[0]
        # Find the prediction with the highest score
        top_prediction = max(predictions, key=lambda x: x["score"])

        label = top_prediction["label"].lower()
        if "spam" in label or label == "label_1":
            status = "Spam"
        else:
            status = "Safe"

        confidence = top_prediction["score"] * 100
        return status, confidence
    else:
        return f"Error {response.status_code}", 0.0


test_messages = [
    "Congratulations! You won a $1,000 Walmart gift card. Click here to claim now!",
    "Hey, are we still meeting for lunch tomorrow at 12?",
    "URGENT! Your account has been suspended. Reply with your password immediately to verify.",
    "Don't forget to submit your project assignment before midnight.",
]

print("=== AI Message Classifier Results ===\n")
for message in test_messages:
    status, confidence = classify_message(message)
    print(f"Message: '{message}'")
    print(f"Classification: {status} ({confidence:.1f}% confidence)\n")