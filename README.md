# kivy-button-grid

An example of doing a simple grid of image buttons in Kivy, for a raspberry pi project.

This uses SDL2 to display without needing X11.  Should work with the Raspberry pi touchscreen?

## Setting up the pi

`apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev  pkg-config libgl1-mesa-dev libgles2-mesa-dev  python-setuptools libgstreamer1.0-dev git-core  gstreamer1.0-plugins-{bad,base,good,ugly}  gstreamer1.0-{omx,alsa} python-dev libmtdev-dev  xclip xsel python3-pil libpangoft2-1.0-0 libpython3-dev python3-pil`

This is going to take a long time, since they don't have binary packages available for rpi.

`pip3 install kivy`

Edit /boot/config.txt and set "gpu_mem=256"

