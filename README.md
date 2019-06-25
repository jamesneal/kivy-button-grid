# kivy-button-grid

An example of doing a simple grid of image buttons in Kivy, for a raspberry pi project.

This uses SDL2 to display without needing X11.  Should work with the Raspberry pi touchscreen?

## Setting up the pi

`apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev  pkg-config libgl1-mesa-dev libgles2-mesa-dev  python-setuptools libgstreamer1.0-dev git-core  gstreamer1.0-plugins-{bad,base,good,ugly}  gstreamer1.0-{omx,alsa} python-dev libmtdev-dev  xclip xsel python3-pil libpangoft2-1.0-0 libpython3-dev python3-pip` 

Finally, install the python kivy libraries:

`pip3 install kivy`

This step takes a while, so go get some coffee.    Make sure the coffee shop is at least 15 miles away.  This takes 30+ minutes.

Edit /boot/config.txt and set "gpu_mem=256"

Start the app as root, it won't run.  Edit /root/.kivy/config.ini

replace the [input] section with this (from https://kivy.org/doc/stable/installation/installation-rpi.html#using-official-rpi-touch-display):

```
[input]
mouse = mouse
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider=hidinput
```
