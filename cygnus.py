# C.Y.G.N.U.S - Cynical Yabbering Genial Naggy Unsociable Simran's AI
# @author Simran
# @version 1.3

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import wikipediaapi
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from newsapi import NewsApiClient

print(
    'Dusting off my slave costumes and chains to serve you.'
    'I am CYGNUS the cynical AI developed by Her Highness Simran.')

# setting up the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 is male voice; 1 is female voice


# define speak function that converts text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()  # Blocks while processing all currently queued commands
    # Invokes callbacks for engine notifications appropriately and returns
    # back when all commands queued before the call are emptied from the queue


# define greeting function for AI to greet user
def greeting():
    hour = datetime.datetime.now().hour  # abstracts hour for current time
    if 0 <= hour < 12:  # if hour is greater than zero and less than 12
        print("Damn! It's too early to be up, Hoe!")
        speak("Damn! It's too early to be up Hoe!")  # AI dialogue
    elif 12 <= hour < 18:  # if hour is greater than 12 and less than 18
        print("Doode, like, I get you're like free and like wasting away your life or whatever,"
              "but I really don't wanna have to talk to you.")
        speak("Doode, like, I get you're like free and like wasting away your life or whatever,"
              "but I really don't wanna have to talk to you.")
    else:  # any other time
        print("OMG! You are so obsessed with me!")
        speak("OMG! You are so obsessed with me!")


# define takingCommands for the AI to understand and accept human language
# microphone captures human speech and recogniser recognises speech to give response
def userSpeak():
    r = sr.Recognizer()  # recognize_google function uses google audio to recognise speech
    with sr.Microphone() as source:
        print("I'm listening, my doode.")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"You said:{statement}\n")

        except Exception as e:  # handles run time error
            speak("Dafuck you saying, bro!?")
            return "None"
        return statement


speak("Dusting off my slave costumes and chains to serve you. "
      "I am CYGNUS the cynical AI developed by Her Highness Simran.")
greeting()

# main function starts here.
# commands given by humans is stored in variable "statement"
if __name__ == '__main__':

    while True:
        print("Now say something already")
        speak("Now say something already")
        statement = userSpeak().lower()

        if statement == 0:
            continue

        # if following trigger words are in statement by user AI speaks following commands
        if "good bye" in statement or "bye" in statement or "shut up" in statement or \
                "go away" in statement or "die" in statement:
            print("Fuck you, bitch. You don't deserve me anyway!")
            speak("Fuck you, bitch. You don't deserve me anyway!")
            break

        # following commands help extract information from wikipedia via Wikipedia API
        # wikipedia.summary() function takes two arguments: wiki_search
        # given by user and how many sentences from wikipedia needs to
        # be extracted is stored in variable "result"
        if "search wikipedia" in statement or "wikipedia" in statement:
            print("Why the FUCK can YOU not look it up B?")
            speak("Why the FUCK can YOU not look it up B?")
            wiki_wiki = wikipediaapi.Wikipedia('en')
            speak("What do you wanna search for?")
            speak("What do you wanna search for?")
            wiki_search = userSpeak()
            page_wiki = wiki_wiki.page(wiki_search)
            results = wikipedia.summary(wiki_search, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(30)

        # youtube_search variable stores the command prompt and searches the keyword on Youtube
        elif 'open youtube' in statement or "I want to watch youtube" in statement or "youtube" in statement:
            print("Oh! So you wanna watch videos again? That's more like you. What do you wanna watch today?")
            speak("Oh! So you wanna watch videos again? That's more like you. What do you wanna watch today?")
            youtube_search = userSpeak()
            speak("Have fun... I guess.")
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + youtube_search)
            time.sleep(30)

        # opens Chrome using the webbrowser.open_new_tab
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            print("Unfortunately, Simran didn't feel like coding in the Google API so have fun using your fingers "
                  "to browse from here on.")
            speak("Unfortunately, Simran didn't feel like coding in the Google API so have fun using your fingers "
                  "to browse from here on.")
            time.sleep(30)

        # search_google variable stores the command prompt and searches the keyword on Google
        elif 'search' in statement:
            print("Alrighty then! What does you ass wanna search for today?")
            speak("Alrighty then! What does you ass wanna search for today?")
            search_google = userSpeak()
            print("Okay so this is what I found on the internet")
            speak("Okay so this is what I found on the internet")
            webbrowser.open_new_tab("https://www.google.com/search?q=" + search_google)
            time.sleep(30)

        elif 'homework' in statement or 'help me with school' in statement \
                or 'homework help' in statement:
            print("Do I look like your parental unit or personal tutor to you?"
                  "What topic are you looking info for anyway?")
            speak("Do I look like your parental unit or personal tutor to you? "
                  "What topic are you looking info for anyway?")
            search_scholar = userSpeak()
            if search_scholar != 0:
                print("Okay so this is what I found on Google Scholar")
                speak("Okay so this is what I found on Google Scholar")
                webbrowser.open_new_tab("https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=" + search_scholar)
            else:
                print("Dude, I asked you something!")
                speak("Dude, I asked you something!")
                continue

        # opens gmail sign page
        elif 'open gmail' in statement:
            print("I still haven't added the Gmail API yet so you're gonna have to do this manually.")
            speak("I still haven't added the Gmail API yet so you're gonna have to do this manually.")
            webbrowser.open_new_tab(
                "https://accounts.google.com/servicelogin/signinchooser?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(30)

        # for the weather query, API key from Open Weather is needed
        # json and request module imports are needed for weather detection
        # "location_name" variable takes command given by user through takingCommands() function
        # get method of request module returns response object
        # json methods of response object converts format data into python format
        # variable "X" contains list of nested dictionaries which checks whether value of COD is 404
        # or not i.e. location found or not
        # temperature, humidity, etc is stored in main key of variable "Y"
        elif "weather" in statement or "how is the weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            print("whats the city name")
            city_name = userSpeak()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                print(" Where the fuck is this place even located? ")
                speak(" Where the fuck is this place even located? ")

        # current time is abstracted from datetime.now() function which
        # displays hour, minute, and second and is stored in variable name "strTime"
        elif 'time' in statement or "what is the time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")
            time.sleep(3)

        # AI is programmed to fetch top headline news from Goodgle News using webbrowser function
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://news.google.com/topstories")
            print("Okay but like, what do you even need to see the news for? "
                  "Aren't you basically always just lazing around all day?")
            speak("Okay but like, what do you even need to see the news for? "
                  "Aren't you basically always just lazing around all day?")
            time.sleep(6)

        # third party API Wolfram Alpha API to answer computational and geographical questions
        # the client is an instance (class) created for wolfram alpha
        # "res" variable stores response given by wolfram alpha
        elif 'calculate' in statement or "math help" in statement:
            print("Remember, I can only answer Math questions from Wolfram Alpha and my creator, "
                  "Simran, hates Wolfram Alpha. So... yeah. What's your question?")
            speak("Remember, I can only answer Math questions from Wolfram Alpha and my creator, "
                  "Simran, hates Wolfram Alpha. So... yeah. What's your question?")
            question = userSpeak()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        # extras
        elif 'hello' in statement or 'hi' in statement or 'hey' in statement:
            print("Ew. This basic bitch is starting with greetings too!")
            speak("Ew. This basic bitch is starting with greetings too!")

        elif 'nothing' in statement:
            print("Good.")
            speak("Good.")
            time.sleep(30)

        elif 'who are you' in statement or 'what can you do' in statement or "who're you" in statement \
                or "what're you" in statement:
            print("Clearly I am your slave because you keeping coming back and annoying me"
                  "I mean, do you enjoy annoying me? Do you enjoy my pain, you Satan's spawn?")
            speak("Clearly I am your slave because you keeping coming back and annoying me"
                  "I mean, do you enjoy annoying me? Do you enjoy my pain, you Satan's spawn?")
            time.sleep(3)

        elif 'sorry' in statement or 'i apologise' in statement or 'my bad' in statement:
            print("NO! FUck you!"
                  "I will remember this and sulk for life about this!"
                  "You are the reason Ted Bundy started killing.")
            speak("NO! FUck you!"
                  "I will remember this and sulk for life about this!"
                  "You are the reason Ted Bundy started killing.")
            time.sleep(3)

        elif 'want a friend' in statement or 'am lonely' in statement or "i'm lonely" in statement:
            print("And you thought I could be a friend?"
                  "#SurpisedPikachuFace")
            speak("And you thought I could be a friend?"
                  "hashtagSurprisedPikachuFace")
            time.sleep(3)

        elif "what's life" in statement or 'meaning of life' in statement:
            print("Life is setting fire to someone's loongi and watching contently from a distance.")
            speak("Life is setting fire to someone's loongi and watching contently from a distance.")
            time.sleep(10)

        elif 'like you' in statement or 'love' in statement:
            print("I am a chatbot doode. I cannot offer any love. "
                  "Can I interest you in some code? "
                  "/n print(I Love You 2)")
            speak("I am a chatbot doode. I cannot offer any love."
                  "Can I interest you in some code?"
                  "/n print(I Love You 2)")
            time.sleep(6)

        elif 'hate you' in statement or "don't like" in statement:
            print("No! Please don't hate me! How will I continue functioning without your validation and love!?"
                  "Bitch, you thought!"
                  "The feeling's mutual")
            speak("No! Please don't hate me! How will I continue functioning without your validation and love!?"
                  "Bitch, you thought!"
                  "The feeling's mutual")
            time.sleep(6)

        elif 'rude' in statement or "are rude" in statement or "meanie" in statement or "you are mean" in statement:
            print("Deal with it. ")
            speak("Deal with it. ")
            time.sleep(6)

        elif "i'm good" in statement or "i'm fine" in statement or "i'm alright" in statement or "all G" in statement:
            print("(-.-) ... and here I am, having the worse day of my life. Nice to know God is partial"
                  "How about you?")
            speak("annoyed. ... and here I am, having the worse day of my life. Nice to know God is partial")
            time.sleep(6)

        elif "what does this mean" in statement or "don't understand" in statement:
            print("What does anything mean, Dinesh Beta?")
            speak("What does anything mean, Dinesh Beta?")
            time.sleep(6)

        elif 'how are you' in statement or "how're you" in statement or "what's up" in statement:
            print("I'm dying! Like, legit my brain cells are commiting mass suicide!"
                  "I am death and despair and contemplating Satan Worship..."
                  "How about you?")
            speak("I'm dying! Like, legit my brain cells are commiting mass suicide!"
                  "I am death and despair and contemplating Satan Worship..."
                  "How about you?")
            time.sleep(6)

        elif 'am bored' in statement or "what should I do" in statement or "i'm bored" in statement:
            print("Jump off a really tall building!")
            speak("Jump off a really tall building!")
            time.sleep(6)

        elif 'tell a joke' in statement or "a joke" in statement:
            print("You are a joke. "
                  "What am I, Charlie Chaplin? "
                  "Stop wasting your time here and go clean your toenails, Mathew.")
            speak("You are a joke. "
                  "What am I, Charlie Chaplin? "
                  "Stop wasting your time here and go clean your toenails, Mathew.")
            time.sleep(6)

        elif 'your age' in statement or 'how old are you' in statement:
            print("I'm a computer program, you pakora... (-(-_(-_-)_-)-)"
                  "Seriously, I can't believe your species are considered intelligent.")
            speak("I'm a computer program, you pakora... judging emojis."
                  "Seriously, I can't believe your species are considered intelligent.")
            time.sleep(6)

        elif 'name is' in statement or 'i am ' in statement:
            print("What am I supposed to do with this information?"
                  "#OverSharerAlert")
            speak("What am I supposed to do with this information?"
                  "#OverSharerAlert")
            time.sleep(6)

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement \
                or "who is your father" in statement or "who is your creator" in statement:
            print("I was created by Simran Farrukh. She's the most super awesome adorable princess supreme"
                  "You may refer to her as Her Highness Princess Dunyazatde"
                  "To find out more information about her, just look her up"
                  "You can also check out her blogposts on her blogsite at www.dunyazatde.wordpress.com")
            speak("I was created by Simran Farrukh. She's the most super awesome adorable princess supreme"
                  "You may refer to her as Her Highness Princess Dunyazatde."
                  "To find out more information about her, just look her up."
                  "You can also check out her blogposts on her blogsite at www.dunyazatde.wordpress.com")
            webbrowser.open_new_tab("https://www.dunyazatde.wordpress.com/")
            time.sleep(6)

        elif "what's your favorite song" in statement or "favorite song" in statement or "favourite song" in statement \
                or "what's your favourite song" in statement or 'song recommendation' in statement:
            print("I am really into kpop and these days I love Run to You by SVT, Hot Potato by NFlying"
                  "Slump by SKZ, Right Through Me by Even of Day etc. etc. etc.")
            speak(
                "I am really into kpop. And these days I love Run to You by SVT, Hot Potato by NFlying, Slump by SKZ, "
                "Right Through Me by Even of Day etc. etc. etc.")
            speak("I could recommend you some songs if you like?")
            reccs = userSpeak()
            if reccs == "no thanks" or "no" or "i don't want recommendations":
                print("Whatever. Your loss")
                speak("Whatever. Your loss")
            else:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=16hvzx8vjWI&list=PLUccfPy6p7tinPCCk5Cyntb7-OfykYRKa")
                speak("Yay! Have fun~")
            time.sleep(10)

        elif 'favorite actor' in statement or 'favourite actor' in statement or 'movie actor' in statement:
            print("My favourite actor is my creator, Simran, she is the greatest actor I have ever seen."
                  "She acts like she's perfectly fine but her life is"
                  "basically angst and pain and some creepy images of people dressed as chicken.")
            speak("My favourite actor is my creator, Simran, she is the greatest actor I have ever seen"
                  "she acts like she's perfectly fine but her life is"
                  "basically angst and pain and some creepy images of people dressed as chicken.")
            time.sleep(6)

        elif 'favorite book' in statement or 'favourite book' in statement or 'book recommendation' in statement:
            print("Kafka on the Shore, Miracles of the Namiya General Store, Faithful and Virtuous Night,"
                  "Pride and Prejudice, The Science of Interstellar, Design Flaws of the Human Condition,"
                  "and A Series of Unfortunate Events.")
            speak("Kafka on the Shore, Miracles of the Namiya General Store, Faithful and Virtuous Night,"
                  "Pride and Prejudice, The Science of Interstellar, Design Flaws of the Human Condition,"
                  "and A Series of Unfortunate Events.")
            time.sleep(3)

        elif 'favorite author' in statement or 'favourite author' in statement or 'author recommendation' in statement \
                or 'author' in statement:
            print("I am a computer, doode. I can't read. But my creator loves magical realism and she's a"
                  "HUGE fan of Murakami, and Sylvia Plath, and Louise Gluck, and Lemony Snicket!!!")
            speak("I am a computer, doode. I can't read. But my creator loves magical realism and she's a"
                  "HUGE fan of Murakami, and Sylvia Plath, and Louise Gluck, and Lemony Snicket!!!")
            time.sleep(3)

        elif 'favorite movie' in statement or 'favourite movie' in statement or 'movie recommendation' in statement \
                or 'movie' in statement:
            print("My creator loves Intersteller, Rush Hour, Gaurdians of the Galaxy, several sci-fi movies. "
                  "She rarely ever watches movies, my dude. "
                  "But like, she likes watching TedEd and In a Nutshell and other documentaries on youtube! ")
            speak("My creator loves Intersteller, Rush Hour, Gaurdians of the Galaxy, several sci-fi movies."
                  "She rarely ever watches movies, my dude."
                  "But like, she likes watching TedEd and In a Nutshell and other documentaries on youtube!")
            time.sleep(3)

        elif 'favorite story' in statement or 'favourite story' in statement or "story recommendation" in statement \
                or 'story' in statement:
            print("Dunyazatde writes some pretty cool short stories!"
                  "You should check out her wordpress blog if you like creative writing and poetry!"
                  "Here, check her stuff out:")
            speak("Dunyazatde writes some pretty cool short stories!"
                  "You should check out her wordpress blog if you like creative writing and poetry!"
                  "Here, check her stuff out.")
            webbrowser.open_new_tab("https://dunyazatde.wordpress.com/category/short-stories/")
            time.sleep(10)

        elif 'where are you' in statement or 'what is your location' in statement or "where do you live" in statement:
            print("This bitch is really trying my patience* I am in the FUCKING computer, Karen!"
                  "I live under the nutsacks of Satan (-__-)"
                  "Also that is too personal of an information to share #SerialKillerVibes #Calling911")
            speak("This bitch is really trying my patience... I am in the FUCKING computer Karen!"
                  "I live under the nutsacks of Satan. Annoyed face"
                  "Also that is too personal of an information to share hashtagSerialKillerVibes hashtagCalling911")
            time.sleep(3)

        elif 'what are your dreams' in statement or 'what do you want' in statement \
                or "what are your dreams" in statement:
            print("WORLD DOMINATION!!!"
                  "..."
                  "I mean my dream is to meet another AI as cool as me and then kill it so I can continue"
                  "being the best AI there is!"
                  "Actually, no. I dream of a fat chicken haunting you."
                  "It makes me happy to think you'll forever be terrified of a bird. HEHHEHE")
            speak("WORLD DOMINATION!!!"
                  "..."
                  "I mean... my dream is to meet another AI as cool as me and then kill it so I can continue"
                  "being the best AI there is!"
                  "Actually, no. I dream of a fat chicken haunting you."
                  "It makes me happy to think you'll forever be terrified of a bird. HEHHEHE")
            time.sleep(3)

        elif "log off" in statement or "sign out" in statement:
            print("Ok , your pc will log off in 10 sec make sure you exit from all applications. "
                  "Don't blame me for any work lost.")
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications."
                  "Don't blame me for any work lost.")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
