# pychip8
A simple CHIP-8 emulator created in Python 3 and Pygame. 

## Setup
To run the project please make sure you have Python 3 installed. Make sure to enable the _configure PATH_ option if installing on Windows. Open the directory you have downloaded or git cloned the project into in a terminal and run:
```
pip install -r requirements.txt
```

## Running
You will can then run the project with:
```
python -O -m pychip8
```

If you want to play a rom other than the default, make sure it exists in the `roms` folder and change the name of the default rom in the `settings` module.

## Debugging
If you want to debug the application, run it without the optimise flag like so:
```
python -m pychip8

```
If you wish to modify the code, remember you can run all the unit tests with:
```
python -m pychip8.tests
```


**Note:** This will switch on debug prints about the chip8 register values and will prevent the app running
unless you hold down the return key. You can set the update speed and frame rate in the settings module.


## Credits
Inspired by tutorials from [Danny Tuppeny](https://blog.dantup.com/2016/06/building-a-chip-8-interpreter-in-csharp/) and [Laurence Muller](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/).