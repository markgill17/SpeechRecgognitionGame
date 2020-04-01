import random
import time

import red as red
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    ObjectProperty,
    StringProperty, NumericProperty)
from kivy.uix.widget import Widget

Builder.load_string("""
<MainGame>:
    word: word

    Label:
        font_size: root.word.font_size
        center_x: root.width /2
        top: root.top/2 + 35
        markup: True
        text: '[color=' + root.word.color + ']' + root.word.text + '[/color]'

    ColorWord:
        id: word
        x: root.x
        center_y: root.center_y
""")

my_colours = {
    '#ff0000': 'red',
    '#0000ff': 'blue',
    '#00ff00': 'green',
    '#ffff00': 'yellow',
    '#ff00ff': 'pink',
    '#5600ff': 'purple',
    '#ff8f00': 'orange',
}


class ColorWord(Widget):
    font_size = NumericProperty(90)
    text = StringProperty('apple')
    color = StringProperty('#ffffff')


class MainGame(Widget):
    word = ObjectProperty(None)
    last_update = int(time.time())

    def update(self, dt):
        if int(time.time()) > self.last_update + 1:
            self.last_update = int(time.time())
            self.word.font_size = random.randrange(60, 260)
            self.word.color = random.choice(list(my_colours.keys()))
            with open("dathanna.txt", "r") as file:
                line = next(file)
                for num, aline in enumerate(file, 2):
                    if random.randrange(num): continue
                    line = aline
                self.word.text = line


class MainApp(App):
    def build(self):
        game = MainApp()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    MainApp().run()
