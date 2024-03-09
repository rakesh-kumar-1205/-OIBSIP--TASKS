import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query1 = r.recognize_google(audio, language='en-in')
        print(f"User said : {query1}\n")
    except Exception as e:
        print("Say that Again:", e)
        return "None"
    return query1


query = take_command().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_google(query):
    try:
        if "google" in query:
            query = query.replace("NEO", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This is what I found on Google:")
            pywhatkit.search(query)
            result = googleScrap.summary(query, sentences=1)
            speak(result)
    except Exception as e:
        speak("No speakable output available: {}".format(str(e)))


def search_youtube(query):
    try:
        if "youtube" in query:
            speak("This is what I found for your search:")
            query = query.replace("NEO", "")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, Sir")
    except Exception as e:
        speak("Error in searching YouTube: {}".format(str(e)))


def search_wikipedia(query):
    if "wikipedia" in query:
        speak("Searching From Wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("NEO", "")  # Assuming "NEO" needs to be removed
        query = query.strip()  # Remove leading and trailing whitespaces
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Ambiguous search term. Suggestions: {', '.join(e.options)}")
            print(f"Ambiguous search term. Suggestions: {', '.join(e.options)}")
        except wikipedia.exceptions.PageError:
            speak("No page found for the given query.")
            print("No page found for the given query.")



