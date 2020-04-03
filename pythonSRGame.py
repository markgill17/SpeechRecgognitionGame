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
                        if guess == color:
                            print(fg("green") + f.renderText("Correct"))
                            score += 1
                        else:
                            print(fg("red") + f.renderText("Wrong"))
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
                        if guess == text:
                            print(fg("green") + f.renderText("Correct"))
                            score += 1
                        else:
                            print(fg("red") + f.renderText("Wrong"))
                            wrong_guesses += 1
                        time.sleep(2)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if wrong_guesses >= 0:
                running = False
                break
    print(fg("blue") + f.renderText("Game over! You scored " + str(score) + " points"))
    time.sleep(5)
    if running is False:
        print(fg("green") + f.renderText("Wanna play again?"))
        time.sleep(4)
        with microphone as source:
            print(attr("reset") + f.renderText("Yes or no?"))
            audio = r.listen(source)
            decision = r.recognize_google(audio)
            decision = decision.split(" ")[0]
            if decision == "yes" or decision == "Yes":
                print(fg("green") + f.renderText("Get Ready"))
                running = True
                time.sleep(7)
                pass
            else:
                print(fg("red") + f.renderText("Bye"))
                sys.exit()
        Game()


Game()
