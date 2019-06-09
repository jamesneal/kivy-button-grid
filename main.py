#!/usr/bin/env python3

from functools import partial
import os

from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

os.environ['KIVY_GL_BACKEND'] = 'gl'

##
# This is our button press event.
def button(num, event):
    if (num == 1):
      print("I love it when button 1 is pressed.")
    elif (num == 4):
      print("Come on.  Button 4 is dumb.")
    else:
      print("Button {} is pressed.".format(num))

##
# This makes a new class called an "ImageButton" that combines the behaviors of a button and an image.
#   (e.g, an image you can click on.)
#  
class ImageButton(ButtonBehavior, Image):
    pass

class TestApp(App):
    def build(self):
        ##
        # Kivy has several "layouts" to choose from: https://kivy.org/doc/stable/gettingstarted/layouts.html
        # This one is a simple "grid".  You can also add layouts to layouts to make more complex layouts.
        layout = GridLayout(cols=2)

        ## This makes four buttons and adds them to the layout.
        for i in range(1,5):
          btn = ImageButton(
                    source="images/{}.png".format(i),
                    on_press=partial(button,i)
                )
          layout.add_widget(btn)

        ## You can also do something like this:
        #
        # btn = ImageButton(source="image.jpg", on_press=engage_thrusters)
        # layout.add_widget(btn)
        #
        # That'll call the "engage_thrusters" instead of the "button" function I defined above.
        #

        return layout

TestApp().run()
