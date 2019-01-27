from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import time
from mutagen.mp3 import MP3

#database for questions

questions = {
    "what is software security?" : "Software security is a kind of computer security that focuses on the secure design and implementation of software.",
    "what is cyber security about?": "Cyber Security also known as computer security is the practice/study of protecting systems, networks, and programs from digital attacks.",
    "who and what are the main figures in cyber security?": "There are mainly 3 figures in cyber security:  The User, the software/ operating system and the hacker.",
    "what does a cyber security person do?":"Cybersecurity analysts help prevent attacks through their knowledge of databases, networks, hardware, firewalls and encryption. They also keep intruders away from personal information or accessing important data.",
    "what are cyber risks?":"Cyber risks can be referred to as any risks that are connected with financial loss resulting from the failure of its information technology systems or because of unauthorized access to informational data.",
    "what kinds of undesired behaviors are there?":"There are 3 types of undesired behaviors:  stealing information which is the opposite of confidentiality, modifying information or functionality which is the opposite of integrity and denying access which is the opposite of availability.",
    "what is Confidentiality in cyber security?":"Confidentiality is roughly equivalent to privacy. Measures undertaken to ensure confidentiality are designed to prevent sensitive information from reaching the wrong people, while making sure that the right people can in fact get it.",
    "what is functionality in cyber security?":"Measures undertaken to ensure confidentiality are designed to prevent unauthorized modification of information, installation of unwanted software and destroying records or data.",
    "what is availability in cyber security?":"Measures undertaken to ensure availability are designed to prevent denying access like when a user is unable to purchase products or for example when a user is Unable to access banking information.",
    "what is the difference between a flaw and a bug?":"A flaw and a bug are both defects in a system but they are different types of defects: a flaw is a defect in the design but a bug is a defect in the implementation.",
}

#recognizez your mic
r = sr.Recognizer()
mic = sr.Microphone()


# starts over
def startover():
    with mic as source:
        audio_time = MP3("answer.mp3")      # answer.mp3 time
        time.sleep(audio_time.info.length + 1.5)      # sleeps for answer.mp3 time + 1sec
        global commandst    #declare commandst as global
        print ("Do you want to ask another question?")

        r.adjust_for_ambient_noise(source)
        audio=r.listen (source)
    try:
        commandst=r.recognize_google(audio)
        print (commandst)
        if commandst == "yes":      # if answer is yes goes to mycommand(); if no exits program
            mycommand()
        elif commandst == "no":
            print("see you later!")
            exit(0)

    except sr.UnknownValueError:    # if program can't hear you says i can't hear you and starts over
        time.sleep(0.5)
        print("I can't hear you!")
        startover()
    return commandst

#text-to-speech
def t2s (audio):
    print(audio)
    tts=gTTS(text=audio, lang="en")
    tts.save("tts.mp3")
    os.system("tts.mp3")

#assistant
def assistant():
    if "open scsa" in command:
        url = "https://scsa.ge/en/"
        webbrowser.open_new(url)
    elif "open facebook" in command:
        url = "https://www.facebook.com/"
        webbrowser.open_new(url)
    elif "open google" in command:
        url = "https://www.google.com/"
        webbrowser.open_new(url)
    elif "open instagram" in command:
        url = "https: // www.instagram.com /"
        webbrowser.open_new(url)


#main
def mycommand ():
    with mic as source:     # accepts audio though mic

        global command      #globally declares command
        print ("Ask a Question")
        r.adjust_for_ambient_noise(source)
        audio=r.listen (source)
    try:
        command=r.recognize_google(audio).lower()
        print (command)

    except sr.UnknownValueError: # if program can't hear you says i can't hear you and starts over
        time.sleep(0.5)
        print("I can't hear you!")
        mycommand ()
    return command

#searching through the database(dictionary)
def search():
    #if your voice input == to cyber or cyber security or security it will say "what is cyber security about?" key
    if command == "cyber" or command == "cyber security" or command == "security":
        tts = gTTS(text=questions["what is cyber security about?"], lang='en')
        mp3bef = MP3("answer.mp3")
        tts.save("answer.mp3")
        os.system("answer.mp3")
        mp3aft = MP3("answer.mp3")


        startover()
        #if mp3 file before the new save and after are the same play the same file
        if mp3bef == mp3aft:
            tts.save("answer.mp3")
            os.system("answer.mp3")
            startover()
    assistant()
    # goes through every key in dictionary questions
    for key in questions.keys():
        # goes through every key of the key in dictionary questions
        for k in key:
            if command in k or command == "what" or command == "who":   # if command is in k or command is what or who says more details needed
                tts = gTTS(text="more details needed", lang='en')
                mp3bef = MP3("answer.mp3")
                tts.save("answer.mp3")
                os.system("answer.mp3")
                mp3aft = MP3("answer.mp3")
                startover()
                if mp3bef == mp3aft:
                    tts.save("answer.mp3")
                    os.system("answer.mp3")
                    startover()

        # if input is in the key of questions if says the value
        if command in key:
            tts = gTTS(text=questions[key], lang='en')
            mp3bef = MP3("answer.mp3")
            tts.save("answer.mp3")
            os.system("answer.mp3")
            mp3aft = MP3("answer.mp3")
            startover()

            # if mp3 before the save and after the save are the same saves the file all over again and plays
            if mp3bef == mp3aft:
                tts.save("answer.mp3")
                os.system("answer.mp3")
                startover()

    if command not in key:
        exit(0)
        # if the answer is not in the dictionary it should google here

mycommand()
search()