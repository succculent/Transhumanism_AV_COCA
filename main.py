import numpy
import PySimpleGUI as sg
import os
import sys

FRAME_WIDTH = 480
FRAME_HEIGHT = 270

frame = numpy.zeros((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=numpy.uint8)

def main():
    sg.theme('dark')
    layout = [
            [sg.Image(filename='', key='image')],

            [sg.Button('Play'), 
             sg.Button('Pause'), 
             sg.Exit()]]

    window = sg.Window('videoPlayer.py',
            layout, location=(600, 200))
    play = False
    # Main Event Loop for GUI
    while True:
        event, values = window.Read(timeout=1)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            print('Exiting')
            break
        if event == 'Play':
            print('Pressed Play')
            play = True
        elif event == 'Pause':
            print('Pressed Pause')
            play = False
        if (play == True):
            print('playing')

    # Close and terminate the stream
    window.Close()

if __name__ == "__main__":
    main()