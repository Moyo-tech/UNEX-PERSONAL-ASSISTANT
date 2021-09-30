import speech_recognition as sr  # recognise speech
from gtts import gTTS #google text to speech
from time import ctime #get time details
import webbrowser #open browser
import time
import playsound  # to play an audio file
import os # to remove created audio file
import random
import pyjokes

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_is(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer () #Initialise a recogniser
#listen for audio to convert to text
def record_audio(ask=False):
    with sr.Microphone () as source:
        if ask:
            speak ( ask )
        audio = r.listen ( source )
        voice_data = " "
        try:
            voice_data = r.recognize_google ( audio )
        except sr.UnknownValueError:
            speak ( 'Sorry I did not get that, could you come again' )
        except sr.RequestError:
            speak ( "Sorry my speech service is down" )
            print(f">> {voice_data.lower()}")
        return voice_data.lower()



def speak(audio_string):
    tts = gTTS ( text=audio_string, lang='en' )
    r = random.randint ( 1, 200000000 )
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save ( audio_file ) #to save as mp3
    playsound.playsound ( audio_file ) #to play the audio file
    print (f"unex: {audio_string}")
    os.remove ( audio_file )


def respond(voice_data):
    #greeting
    if there_is(['hey', 'hi', 'hello', 'hey unex', 'yo']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        speak(greet)

    #Unex name
    if there_is ( ["what is your name", "what's your name", "tell me your name"] ):
        if person_obj.name:
            speak ( "my name is Unex" )
        else:
            speak ( "my name is Unex. what's your name?" )
    if there_is( ["my name is"] ):
        person_name = voice_data.split ( "is" )[-1].strip ()
        speak ( f"ohh what a nice name, i will remember that {person_name}" )
        person_obj.setName ( person_name )  # remember name in person object

    #greeting
    # 3: greeting
    if there_is(["how are you","how are you doing"]):
        speak ( f"I'm very well, thanks for asking {person_obj.name}" )

        # time
    if there_is( ["what's the time", "tell me the time", "what time is it", "what is today's date", "what day is this"] ):
        speak(ctime())


#search google
    if there_is( ["search for"] ) and 'youtube' not in voice_data:
        search_term = voice_data.split ( "for" )[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get ().open ( url )
        speak ( f'Here is what I found for {search_term} on google' )
#location
    if there_is ( ["location"] ) :
        location = voice_data.split ( "for" )[-1]
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get ().open ( url )
        speak ( f'Here is the location for  {location} on google' )

    #search youtube
    if there_is( ["youtube"] ):
        search_term = voice_data.split ( "for" )[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get ().open ( url )
        speak ( f'Here is what I found for {search_term} on youtube' )

    if there_is(["joke"]):
        speak( pyjokes.get_joke () )

    if there_is(['exit', 'stop', 'go to sleep unex' ,'talk to you later unex', 'bye unex']):
        speak('going offline')
        exit()


time.sleep (1)

person_obj = person()
while (1):
    voice_data = record_audio () #get the voice input
    respond ( voice_data ) #respond
