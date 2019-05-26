# pychip8
A simple CHIP-8 emulator created in Python 3 using [Pygame](https://www.pygame.org/wiki/about).

![preview](https://media.giphy.com/media/5WfOGIAqptoooERlKQ/giphy.gif)

## Setup

To run the project please make sure you have Python 3 installed. Make sure to enable the _configure PATH_ option if installing on Windows. Open the directory you have downloaded or git cloned the project into in a terminal and run:

```
pip install -r requirements.txt
```

## Running the emulator

You can run the emulator from its install folder like so:

```
python -O -m pychip8
```
A small selection of roms are included inside the `roms` folder. If you want to play a rom other than the default debug rom (*which just prints the default font characters*), make sure it exists in the `roms` folder and pass the exact name of the rom with the
`--rom` selection argument, e.g.

```
python -O -m pychip8 --rom "Airplane.ch8"
```

The other runtime options are as follows:

```
 -m, --mute    pass this flag to turn audio off
 -s, --scale   the scale to apply to the CHIP-8's 64x32 video output - defaults to 10 for 640x320 pixels
```

## Debugging
If you want to debug the application, run it without the [optimize](https://docs.python.org/3/using/cmdline.html#cmdoption-o) flag:

```
python -m pychip8

```

**Note:** This will switch on debug prints about the CHIP-8 register values and will prevent the app running
unless you hold down the return key. You can set the update speed and frame rate in the settings module.
If you haven't already it's a good idea to look up the summary of the CHIP-8 and its operations on [Wikipedia](https://en.wikipedia.org/wiki/CHIP-8) as well as [Cowgod's technical guide.](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM)

If you wish to modify the code, remember you can run all the unit tests with:

```
python -m pychip8.tests
```

## Credits
Inspired by tutorials from [Danny Tuppeny](https://blog.dantup.com/2016/06/building-a-chip-8-interpreter-in-csharp/) and [Laurence Muller](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/).
