import speech_recognition as sr;

def recognize_speech_from_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak Something")
        recognizer.adjust_for_ambient_noice(source)
        try:
            audio = recognizer.listen(source)
            print("Recognizing")
            text = recognizer.recognize_google(audio)
            print(f"You said {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry,  I could not understand what you said.")
            return None
        except sr.RequestError:
            print("Sorry, I could not request results from the service.")
            return None


def main():
    print("Welcome to the Speech-to-Text module!")
    
    speech_text = recognize_speech_from_text()

    if speech_text:
        print(f"Speech converted to text: {speech_text}")
    else:
        print("No speech was recognized.")
if __name__ == "__main__":
    main()