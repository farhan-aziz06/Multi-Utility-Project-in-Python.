import pyttsx3

# Text to Speach Method

def speech_to_text(text):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    engine.say(text)

    engine.runAndWait()

def main():
    
    print("Welcome to the Text-to-Speech (TTS) module!")
    text_input = input("Enter the text you want to convert to speech: ")
    speech_to_text(text_input)
    print("Speech has been successfully converted!")

if __name__ == "__main__":
    main()