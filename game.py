from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import winsound
import threading
def play_sound():
    winsound.PlaySound("./sounds/start_background.wav", winsound.SND_FILENAME) 
sound_playing = False
def play_sound():
    global sound_playing
    if not sound_playing:
        sound_playing = True
        winsound.PlaySound("./sounds/start_background.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
def stop_sound():
    global sound_playing
    if sound_playing:
        winsound.PlaySound(None, winsound.SND_PURGE)
        sound_playing = False
def help_window():
    stop_sound()
def story_animation():
    stop_sound()
def start_game():
    stop_sound()
