import pyttsx3
import datetime
import webbrowser
import wikipedia
import os

# ---------------- VOICE ENGINE ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def speak(text):
    print("Baymax:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- GREETING ----------------
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning Suryansh")
    elif hour < 18:
        speak("Good afternoon Suryansh")
    else:
        speak("Good evening Suryansh")

    speak("Hello. I am Baymax. Your personal assistant. How can I help you?")

# ---------------- MAIN PROGRAM ----------------
def run_baymax():
    wish()

    while True:
        command = input("\nType command: ").lower()

        # -------- OPEN WEBSITES --------
        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open whatsapp" in command:
            speak("Opening WhatsApp web")
            webbrowser.open("https://web.whatsapp.com")

        elif "open linkedin" in command:
            speak("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")

        elif "open apple music" in command or "open music" in command:
            speak("Opening Apple Music")
            os.system("open -a 'Music'")

        # -------- PLAY SONG --------
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song}")
            webbrowser.open(f"https://music.apple.com/us/search?term={song.replace(' ', '+')}")

        # -------- TIME --------
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Current time is {time}")

        # -------- DATE --------
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # -------- KNOWLEDGE --------
        elif "who is" in command or "what is" in command:
            topic = command.replace("who is", "").replace("what is", "").strip()
            speak(f"Searching for {topic}")

            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Not found on Wikipedia. Searching on Google.")
                webbrowser.open(f"https://www.google.com/search?q={topic}")

        elif "wikipedia" in command:
            speak("Enter topic")
            topic = input("Topic: ")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Not found")

        # -------- OPEN APPS --------
        elif "open code" in command:
            speak("Opening Visual Studio Code")
            os.system("open -a 'Visual Studio Code'")

        elif "open finder" in command:
            speak("Opening Finder")
            os.system("open ~")

        # -------- MOTIVATION --------
        elif "motivate me" in command:
            speak("You are strong. You will get placed. Stay focused.")

        # -------- EXIT --------
        elif "exit" in command or "stop" in command:
            speak("Goodbye Suryansh. Baymax is always here for you.")
            break

        else:
            speak("Command not recognized. Try again.")

# ---------------- START ----------------
run_baymax()