import pyttsx3
import datetime
import webbrowser
import os

class UtilityAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

    def text_to_speech(self, text):
        """Convert text to speech."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def greet_user(self):
        """Greet the user based on the time of day."""
        hour = datetime.datetime.now().hour
        if hour < 12:
            greeting = "Good morning!"
        elif 12 <= hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
        self.text_to_speech(greeting)
        self.text_to_speech("How can I assist you today?")

    def perform_task(self, command):
        """Perform tasks based on user command."""
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.text_to_speech(f"The time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.text_to_speech(f"Today's date is {current_date}")

        elif "notepad" in command:
            os.system("notepad")
            self.text_to_speech("Opening Notepad.")
        elif "browser" in command:
            webbrowser.open("https://www.google.com")
            self.text_to_speech("Opening your browser.")

        elif "search" in command:
            self.text_to_speech("What would you like to search for?")
            query = input("Enter your search query: ").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                self.text_to_speech(f"Here are the results for {query}.")


        elif "exit" in command or "quit" in command:
            self.text_to_speech("Goodbye! Have a great day.")
            exit()

        else:
            self.text_to_speech("I didn't catch that. Could you please repeat?")

    def start_assistant(self):
        """Start the assistant."""
        self.greet_user()
        while True:
            command = input("Enter your command: ").strip().lower()
            self.perform_task(command)

def main():
    """Main entry point for the assistant."""
    print("Starting the Utility Assistant...")
    assistant = UtilityAssistant()
    assistant.start_assistant()

# Run the main method
if __name__ == "__main__":
    main()
