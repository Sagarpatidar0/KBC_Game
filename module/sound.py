import sys
import os

# Redirect stdout to a null device to suppress print output
sys.stdout = open(os.devnull, 'w')

import pygame


# Restore stdout
sys.stdout.close()
sys.stdout = sys.__stdout__

def play_sound(url):
    # Initialize pygame
    pygame.init()

    # Load the MP3 file
    # audio_file = "E:\\college_5th_sem\\PW_DS\\KBC\\sound\\KBC_intro.mp3"
    audio_file = url

    # Initialize the mixer module for audio playback
    pygame.mixer.init()

    # Load the audio file into a Sound object
    sound = pygame.mixer.Sound(audio_file)

    # Play the audio
    sound.play()

    # Wait for the audio to finish playing
    while pygame.mixer.get_busy():
        pygame.time.wait(100)

    # Clean up resources
    pygame.quit()

