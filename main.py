import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests #pip install requests
# from openai import OpenAI


r = sr.Recognizer()  #its a class that helps in speech recognition
engine = pyttsx3.init()
newsapi = "7797e5b28e1b44dabf43fb22d6e10616"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musiclib.music:

            link = musiclib.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.") 
    elif "news" in c.lower():
        read_news()
    # else:
    #     # let openAI handel requests
    #     output = AIprocess(c)
    #     speak(output)
    else:
        speak("sorry can't process you command")


def read_news():
    # Fetch and read out top news headlines.
    URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    try:
        response = requests.get(URL)
        data = response.json()

        # print(data)
        
        if data["status"] == "ok":
            articles = data["articles"][:3]  # Get top 3 news
            for i, article in enumerate(articles, start=1):
                headline = article["title"]
                print(f"{i}. {headline}")
                speak(headline)  # Read headline aloud
        else:
            speak("Sorry, I couldn't fetch the news.")
    
    except Exception as e:
        speak("There was an error fetching the news.")
        print("Error:", e)

# Call read_news() when needed


# def AIprocess(command):
#     client = OpenAI(api_key="")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are virtual assistant named Jarvis "}
#             {"role": "user", "content": command}
#         ]
#     )
#     return completion.choices[0].message.content

def speak(text):
    engine.say(text)
    engine.runAndWait()


if (__name__ == "__main__"):
    speak("waking up Jarvis")

    while True:
        # listen for the wake word jarvis
        # obtain audio from microphine
        # r = sr.Recognizer()

        try:

            with sr.Microphone() as source:
                print("listining")
                # r.adjust_for_ambient_noise(source, duration= 1)
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            
            word = r.recognize_google(audio)
            print(word)

            if(word.lower() == "jarvis"): 
                speak("yes, how may i help you")

                #listen for command

                with sr.Microphone() as source:
                    print("speak your command for jarvis")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)

                processCommand(command)


        # except sr.UnknownValueError:
        #     print("could not understand you, please speak again")

        except Exception as e:
            print(f"error: {e}")


