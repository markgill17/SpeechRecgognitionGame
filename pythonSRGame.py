import random
import sys
import time

from pyfiglet import Figlet
from colored import fg, bg, attr
import speech_recognition as sr

r = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    r.adjust_for_ambient_noise(source, duration=1)

font_colours = ['red', 'blue', 'green', ]
bg_colours = ['red', 'blue', 'green', ]
fonts = [
    'banner',
    'banner3',
    'basic',
    'letters',
    'nancyj',
    'o8',
    'roman',
    'univers',
]

def Game():
    wrong_guesses = 0
    score = 0

    running = True

    while running is True:
        color = random.choice(font_colours)
        text = random.choice(font_colours)
        font = random.choice(fonts)
        background = random.choice(bg_colours)
        if color != background:
            f = Figlet(font)
            print(fg(color) + f.renderText(text))
            objectiveDecider = random.randint(1, 2)
            # print(objectiveDecider)
            # print(font)

            if objectiveDecider == 1:
                with microphone as source:
                    print(attr("reset") + "Say the colour of the text")
                    audio = r.listen(source)
                    try:
                        guess = r.recognize_google(audio)
                        guess = guess.split(" ")[0]
                        if guess.lower() == color:
                            print(fg("green") + "Correct")
                            score += 1
                        elif guess.lower() == "quit" or guess.lower() == "close" or guess.lower() == "leave":
                            sys.exit()
                        else:
                            print(fg("red") + "Wrong")
                            print(fg("red") + "Correct answer was: "+ color + ". You said : " +guess)

                            wrong_guesses += 1
                        time.sleep(2)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
            elif objectiveDecider == 2:
                with microphone as source:
                    print(attr("reset") + "Say the word!")
                    audio = r.listen(source)
                    try:
                        guess = r.recognize_google(audio)
                        guess = guess.split(" ")[0]
                        if guess.lower() == text:
                            print(fg("green") + "Correct")
                            score += 1
                        elif guess.lower() == "quit" or guess.lower() == "close" or guess.lower() == "leave":
                            sys.exit()
                        else:
                            print(fg("red") + "Wrong")
                            print(fg("red") + "Correct answer was: "+ color + ". You said : " +guess)
                            wrong_guesses += 1
                        time.sleep(2)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if wrong_guesses == 5:
                running = False
                break
    print(fg("blue") + "Game over! You scored " + str(score) + " points")
    time.sleep(5)
    if running is False:
        print(fg("green") + "Wanna play again?")
        time.sleep(4)
        with microphone as source:
            print(attr("reset") + "Yes or no?")
            audio = r.listen(source)
            decision = r.recognize_google(audio)
            decision = decision.split(" ")[0]
            if decision == "yes" or decision == "Yes":
                print(fg("green") + "Get Ready")
                running = True
                time.sleep(7)
                pass
            else:
                print(fg("red") + f.renderText("Bye"))
                sys.exit()
        Game()

#Game()


def Main():
    with microphone as source:
        print(attr("reset") + "Welcome to the colour aptitude test")
        print(attr("reset") + "You will be prompted to either say the colour of the text displayed, or the actual "
                              "word itself")
        print(attr("reset") + "Do you want to play?")
        print(attr("reset") + "Yes or No")
        try:
            audio = r.listen(source)
            decision = r.recognize_google(audio)
            decision = decision.split(" ")[0]
            if decision == "yes" or decision == "Yes":
                print(fg("green") + "Get Ready")
                running = True
                time.sleep(3)
                pass
            else:
                print(fg("red") + "Bye")
                sys.exit()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    Game()

Main()