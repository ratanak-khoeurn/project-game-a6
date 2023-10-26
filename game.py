from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import winsound
import threading

#=============play sound on background start================
def play_sound():
    winsound.PlaySound("./sounds/start_background.wav", winsound.SND_FILENAME) 
sound_playing = False

def play_sound():
    global sound_playing
    if not sound_playing:
        sound_playing = True
        winsound.PlaySound("./sounds/start_background.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

#=============stop play sound on background start================
def stop_sound():
    global sound_playing
    if sound_playing:
        winsound.PlaySound(None, winsound.SND_PURGE)
        sound_playing = False

#=============stop play sound on background start================
def help_window():
    stop_sound()

#=============stop play sound on story animation============
def story_animation():
    stop_sound()

#=============stop play sound on start game window================
def start_game():
    stop_sound()
window = tk.Tk()
window.geometry('2000x1200')
window.title("🐱‍👤 ARMY HERO 🐱‍👤")

frame = tk.Frame(window, width=2000, height=1000)
frame.pack()

canvas = tk.Canvas(frame, width=2000, height=1000)
canvas.pack()