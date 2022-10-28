import numpy
import PySimpleGUI as sg
import os
import sys
import time
from audio import Audio

FRAME_WIDTH = 480
FRAME_HEIGHT = 270
BPM = 128;
BPM_DELTA = 60.0 / BPM; #seconds per beat

frame = numpy.zeros((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=numpy.uint8)

def main():
    #setup for GUI
    sg.theme('dark')
    layout = [
            [sg.Image(filename='', key='image')],

            [sg.Button('Play'), 
             sg.Button('Pause'), 
             sg.Exit()]]

    window = sg.Window('videoPlayer.py',
            layout, location=(600, 200))
    play = False

    #audio and video class set up
    a = Audio()
    #TODO...call constructors here

    # Main Event Loop for GUI
    time_stamp = time.time()
    while True:
        event, values = window.Read(timeout=1)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            print('Exiting')
            break
        if event == 'Play':
            play = True
        elif event == 'Pause':
            print('Pressed Pause')
            play = False
        if (play == True):
            if (time.time() - time_stamp >= BPM_DELTA*4):
                #SOUND TRIGGER
                a.update()

                #VIDEO TRIGGER

                time_stamp = time.time()

    # Close and terminate the stream
    window.Close()

if __name__ == "__main__":
    main()