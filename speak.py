import pyttsx3

eng = pyttsx3.init()

x = False

while x is False:

    t = input("Say something: ")

    if t != 'fin':
        eng.say(t)
    else:
        x = True

    eng.runAndWait()
