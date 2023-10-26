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

#=============play sound on help window================
def help_window():
    winsound.PlaySound("./sounds/play_game.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

    help_window = tk.Toplevel(window)
    help_frame = tk.Frame(help_window, width=help_window.winfo_screenwidth(), height=help_window.winfo_screenheight())
    help_frame.pack()
    help_canvas = tk.Canvas(help_frame, width=help_window.winfo_screenwidth(), height=help_window.winfo_screenheight())
    help_canvas.pack()
    help_image = Image.open('images/rules.png')
    help_image = help_image.resize((help_window.winfo_screenwidth(), help_window.winfo_screenheight()))
    help_background = ImageTk.PhotoImage(help_image)
    help_canvas.create_image(0, 0, image=help_background, anchor=NW)

#=============create button back on help window================
    button_back = Button(help_frame, text='Back', width=10, height=2, bg='dark red', font=('DRIPINK PERSONAL USE Black', 12), border=5, command=help_window.destroy)
    button_back.place(x=80, y=600)
    help_canvas.image = help_background
