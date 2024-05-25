import speech_recognition as sr
from textblob import TextBlob

# Step 1: Record audio
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking...")
        audio = r.listen(source)
    return audio

# Step 2: Convert audio to text
def audio_to_text(audio):
    try:
        text = sr.recognize_google(audio)
        return text
    except Exception as e:
        print("Error:", str(e))
        return None

# Step 3: Perform sentiment analysis
def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Main function
def main():
    # Record audio
    audio = record_audio()

    # Convert audio to text
    if audio:
        text = audio_to_text(audio)
        if text:
            print("Transcribed text:", text)

            # Perform sentiment analysis
            sentiment = sentiment_analysis(text)
            print("Sentiment:", sentiment)
        else:
            print("Failed to transcribe audio.")
    else:
        print("Failed to record audio.")

if __name__ == "__main__":
    main()
