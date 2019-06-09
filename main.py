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
    print("Button {} is pressed.".format(num))

class ImageButton(ButtonBehavior, Image):
    pass

class TestApp(App):
    def build(self):
        #layout = GridLayout(cols=2, row_force_default=True, col_default_width=100)
        layout = StackLayout(orientation='lr-tb')

        btn1 = ImageButton(source="images/1.png", size_hint_x=0.5, size_hint_y=0.5)
        btn1.bind(on_press=partial(button,1))

        btn2 = ImageButton(source="images/2.png", size_hint_x=0.5, size_hint_y=0.5)
        btn2.bind(on_press=partial(button,2))

        btn3 = ImageButton(source="images/3.png", size_hint_x=0.5, size_hint_y=0.5)
        btn3.bind(on_press=partial(button,3))

        btn4 = ImageButton(source="images/4.png", size_hint_x=0.5, size_hint_y=0.5)
        btn4.bind(on_press=partial(button,4))

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

TestApp().run()
