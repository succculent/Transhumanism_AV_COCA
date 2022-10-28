from ossaudiodev import SOUND_MIXER_ALTPCM
import numpy
import PySimpleGUI as sg
import os
import sys
import time

FRAME_WIDTH = 480
FRAME_HEIGHT = 270
BPM = 128;
BPM_DELTA = 60.0 / BPM; #seconds per beat

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

    time_stamp = time.time()

    while True:
        event, values = window.Read(timeout=1)
        if (time.time() - time_stamp >= BPM_DELTA*4):
            #SOUND TRIGGER

            #VIDEO TRIGGER

            time_stamp = time.time()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            print('Exiting')
            break
        if event == 'Play':
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