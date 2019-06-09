#!/usr/bin/env python3

from functools import partial
import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

os.environ['KIVY_GL_BACKEND'] = 'gl'

def button(num, event):
    if (num == 1):
      print("I love it when button 1 is pressed.")
    elif (num == 4):
      print("Come on.  Button 4 is dumb.")
    else:
      print("Button {} is pressed.".format(num))

class ImageButton(ButtonBehavior, Image):
    pass

class TestApp(App):
    def build(self):
        layout = StackLayout(orientation='lr-tb')

        for i in range(1,5):
          btn = ImageButton(source="images/{}.png".format(i), size_hint_x=0.5, size_hint_y=0.5)
          btn.bind(on_press=partial(button,i))
          layout.add_widget(btn)

        return layout

TestApp().run()
