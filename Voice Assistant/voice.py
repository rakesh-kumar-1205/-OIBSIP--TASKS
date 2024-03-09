import pyttsx3
import speech_recognition
import webbrowser
import random
import datetime
import requests
import smtplib
import wolframalpha
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query1 = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query1}\n")
    except Exception as e:
        print("Say that again:", e)
        return "None"
    return query1


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': "api_id",
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data['cod'] == '404':
            return "City not found. Please provide a valid city name."

        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        result = f"The current weather in {city} is {temperature} degrees Celsius with {description}."
        return result
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"


def send_email(subject, body, to_email):
    # Replace the following variables with your email credentials
    sender_email = "rakeshkumar.mca1205@gmail.com"
    sender_password = "password"

    # Create a connection to the SMTP server
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=sender_email,password=sender_password)

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    connection.sendmail(sender_email, to_email, message)

    # Close the connection
    connection.close()


def set_reminder():
    # Get reminder details from the user
    reminder_text = input("What would you like to be reminded of? ")
    date_input = input("When (YYYY-MM-DD)? ")
    time_input = input("At what time (HH:MM AM/PM)? ")

    # Combine date and time inputs into a single string
    reminder_datetime_str = f"{date_input} {time_input}"

    try:
        # Convert the string to a datetime object
        reminder_datetime = datetime.datetime.strptime(reminder_datetime_str, "%Y-%m-%d %I:%M %p")
        # Calculate the time difference until the reminder
        time_difference = (reminder_datetime - datetime.datetime.now()).total_seconds()
        # Check if the reminder time is in the future
        if time_difference > 0:
            print(f"Reminder set for {reminder_datetime}.")
            # Sleep until the reminder time
            time.sleep(time_difference)
            # Notify the user when it's time for the reminder
            print(f"Reminder: {reminder_text}")
            # Use pyttsx3 to convert the reminder text to speech
            engine = pyttsx3.init()
            engine.say(f"Reminder: {reminder_text}")
            engine.runAndWait()
        else:
            print("Invalid reminder time. Please set a future time.")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid date and time formats.")


if __name__ == "__main__":
    while True:
        query = take_command().lower()
        if "wake up alexa" in query:
            from GreetMe import greetme
            greetme()
            while True:
                query = take_command().lower()
                if "go to sleep alexa" in query:
                    speak("Ok Sir, You can call me anytime")
                elif "hello alexa" in query:
                    speak("Hello Sir, How are You?")
                elif "fine alexa" in query:
                    speak("It's good to hear that you're doing well.")
                elif "how are you alexa" in query:
                    speak("I am doing well, thank you for asking.")
                elif "thank you alexa" in query:
                    speak("You're welcome, how can I help you now?")
                elif "tired alexa" in query:
                    speak("Playing your favourite song , sir")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=gJLVTKhTnog")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=5KLIKObg7LM")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=bL6dJjxm0x0")
                elif "google" in query:
                    from SearchAnything import search_google

                    search_google(query)
                elif "youtube" in query:
                    from SearchAnything import search_youtube

                    search_youtube(query)
                elif "wikipedia" in query:
                    from SearchAnything import search_wikipedia

                    search_wikipedia(query)
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                elif "weather in" in query:
                    city = query.split("weather in")
                    if len(city) > 1:
                        city = city[1].strip()
                        if city:
                            weather_report = get_weather(city)
                            speak(weather_report)
                            print(weather_report)
                        else:
                            speak("Please specify a city for the weather report.")
                    else:
                        speak("Please specify a city for the weather report.")
                elif "send email" in query:
                    speak("Sure! Please provide the subject of the email.")
                    subject = str(input("enter subject details:"))
                    speak("Now, please provide the body of the email.")
                    body = str(input("enter Body of the Email:"))
                    speak("Great! Lastly, provide the recipient's email address.")
                    to_email = str(input("enter the email whom to send:"))

                    try:
                        send_email(subject, body, to_email)
                        speak("Email sent successfully!")
                    except Exception as e:
                        print(f"Sorry, there was an error sending the email: {str(e)}")
                elif "turn on the lights" in query:
                    speak("Sorry, I can't control smart home devices yet.")
                elif 'what is' in query or 'who is' in query or 'which is' in query:
                    app_id = "app_id"
                    client = wolframalpha.Client(app_id)
                    try:

                        ind = query.lower().index('what is') if 'what is' in query.lower() else \
                            query.lower().index('who is') if 'who is' in query.lower() else \
                                query.lower().index('which is') if 'which is' in query.lower() else None

                        if ind is not None:
                            text = query.split()[ind + 2:]
                            res = client.query(" ".join(text))
                            ans = next(res.results).text
                            speak("The answer is " + ans)
                            print("The answer is " + ans)
                        else:
                            speak("I couldn't find that. Please try again.")
                    except StopIteration:
                        speak("I couldn't find that. Please try again.")
                elif "set reminder" in query:
                    speak("What do you want to reminder ,Sir")
                    set_reminder()

                elif "sleep alexa" in query:
                    speak("Going to Sleep sir")
                    exit()


