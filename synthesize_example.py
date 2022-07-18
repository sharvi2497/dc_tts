#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
This code file runs an example of synthesize
params: 
"""

import sounddevice
import soundfile
from dc_tts.synthesize import Synthesizer
import time


# default values
CHECKPOINT_TEXT2MEL = "dc_tts/models/LJ01-1/model_gs_2280k"
CHECKPOINT_SSRN = "dc_tts/models/LJ01-2/model_gs_132k"


def playsound(filename: str):
    """This function plays the sound of the given filename
    params : filename : string of file location
    """
    data, fs = soundfile.read(filename, dtype='float32')
    sounddevice.play(data, fs)
    status = sounddevice.wait()

def run(checkpoint_text2mel, checkpoint_ssrn):
    """this function
    params: checkpoint_text2mel: string - location of Text2Mel model
    checkpoint_ssrn: string - location of SSRN model
    """
    if checkpoint_text2mel and checkpoint_ssrn:
        synthesizer = Synthesizer(checkpoint_text2mel, checkpoint_ssrn)
    else:
        synthesizer = Synthesizer(CHECKPOINT_TEXT2MEL, CHECKPOINT_SSRN)
    while True:
        utterance = input("Enter an utterance: ")
        if not utterance:
            break
        current_time = time.strftime("%Y:%m:%d-%H:%M:%S")
        filename = f'utterance-{current_time}.wav'
        synthesizer.synthesize(utterance, filename)
        print("Utterance saved in %s" % filename)
        playsound(filename)

