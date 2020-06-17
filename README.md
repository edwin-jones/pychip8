# pychip8
A simple CHIP-8 emulator created in Python 3 using [Pygame](https://www.pygame.org/wiki/about).
This is a _simplified_ version of the original project to make it easier to explain the code in certain contexts.

## Setup

To run the project please make sure you have Python 3 and Pygame installed.

## Running the emulator

You can run the emulator from its install folder like so:

```
python pychip8
```
A small selection of roms are included inside the `roms` folder. If you want to play a rom other than the default debug rom (*which just prints the default font characters*), make sure it exists in the `roms` folder and pass the exact name of the rom with the
`--rom` selection argument, e.g.

```
python pychip8 --rom "Airplane.ch8"
```

_NB: On some systems, you may need to type `python3` instead of `python`._

If you haven't already it's a good idea to look up the summary of the CHIP-8 and its operations on [Wikipedia](https://en.wikipedia.org/wiki/CHIP-8) as well as [Cowgod's technical guide.](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM)

## Credits
Inspired by tutorials from [Danny Tuppeny](https://blog.dantup.com/2016/06/building-a-chip-8-interpreter-in-csharp/) and [Laurence Muller](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/).