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
#=============play sound on story animation and play sound================
def story_animation():
#=============close story window ================
    def close_story():
        story.destroy()
    winsound.PlaySound("./sounds/history.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    
    story_text = " 😱 THE ARMY HISTORY 😱 \n He was a soldier loyal to the motherland and \n defended the motherland from aggression. His name \n is Ratanak and he also has two other friends  who are \n loyal to the motherland. But now they are dead, their are \n ☠☠☠ Sok Heang and Channy ☠☠☠ \n ----------✨✨✨✨----------"
    
#=============animation text ================
    def animate_text(label, text, index=0, delay=80):
        if index < len(text):
            label.config(text=text[:index+1])
            label.after(delay, animate_text, label, text, index+1, delay)
    
    story = Toplevel(window)
    story.attributes("-fullscreen", True)
    story.attributes("-alpha", 0.9)
    story.attributes("-topmost", True)
    story_label = Label(story, font=("GOLDROPS PERSONAL USE", 36), bg="black", fg="white")
    story_label.pack(fill=BOTH, expand=True)
    animate_text(story_label, story_text)
    
#=============create button back================
    button_back = Button(story, text="Back", width=10, height=2, bg="dark red", font=("GOLDROPS PERSONAL USE", 12), border=5, command=close_story)
    button_back.pack()
    button_back.place(x=650, y=680)
#=============start game================
def start_game():
    level_window = tk.Toplevel(window)
    level_window.title("🐱‍👤 START GAME 🐱‍👤")
    level_window.geometry("2000x900")

    canvas = tk.Canvas(level_window, width=1920, height=1080)
    canvas.pack()

    image = Image.open("./images/sunrise.png")
    background_image = ImageTk.PhotoImage(image)
    background = canvas.create_image(0, 0, anchor="nw", image=background_image)
    scroll_speed = 0.3
    scroll_direction = "right"

    
#=============back ground animation================
    def scroll_background():
        if scroll_direction == "right":
            canvas.move(background, -scroll_speed, 0)
            if canvas.coords(background)[0]<=-image.width:
                canvas.move(background, image.width, 0)
        elif scroll_direction == "left":
            canvas.move(background, scroll_speed, 0)
            if canvas.coords(background)[0] >= 0:
                canvas.move(background, -image.width, 0)
        window.after(10, scroll_background)

#=============create army image================
    player_image = Image.open("./images/army.png")
    player_image = player_image.resize((70, 70))
    player_image = ImageTk.PhotoImage(player_image)

#=============create walls================
    player = canvas.create_image(110, 110, anchor="nw", image=player_image)
    wall_image = Image.open("./images/walls.png")
    wall_image = wall_image.resize((250, 50))
    wall_image = ImageTk.PhotoImage(wall_image)
    wall_coords = [
        (0, 600),
        (230, 360),
        (100, 250),
        (20, 600),
        (400, 560),
        (500, 460),
        (600, 400),
        (600, 180),
        (600, 180),
        (1000, 460), 
        (700, 260),
        (1000, 160),
        (600, 90),
        (800, 600)
    ]

    for x, y in wall_coords:
        canvas.create_image(x, y, anchor="nw", image=wall_image, tags="wall")

    keyPressed = []
    SPEED = 7
    TIME = 10
    GRAVITY_FORCE = 5
    
#=============check player movement================
    def check_movement(dx=0, dy=0):
        player_coords = canvas.coords(player)
        new_x1 = player_coords[0] + dx
        new_y1 = player_coords[1] + dy
        new_x2 = player_coords[0] + dx-20 + player_image.width()
        new_y2 = player_coords[1] + dy-20 + player_image.height()
        overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
        for wall_id in canvas.find_withtag("wall"):
            if wall_id in overlapping_objects:
                return False

        return True

#=============start movement================
    def start_move(event):
        if event.keysym not in keyPressed:
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

#=============jump================
    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0,-force)
                window.after(TIME,jump,force-1)

    def move():
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed:
                x = -SPEED
            if "Right" in keyPressed:
                x = SPEED
        if check_movement(x, 0):
            canvas.move(player, x, 0)
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE):
            jump(20)
        level_window.after(TIME, move)

#=============stop movement================
    def stop_move(event):
        global keyPressed
        if event.keysym in keyPressed:
            keyPressed.remove(event.keysym)

#=============gravity================
    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player, 0, GRAVITY_FORCE)
        level_window.after(TIME, gravity)

    gravity()
    level_window.bind("<Key>", start_move)
    level_window.bind("<KeyRelease>", stop_move)

    scroll_background()
    level_window.mainloop()
#=============background_game_image================
background_game_image = Image.open('images/sunrise.png')
bg_img = ImageTk.PhotoImage(background_game_image)

#=============player_image================
player_image = Image.open("./images/army.png")
player_image = player_image.resize((70, 70))
player_image = ImageTk.PhotoImage(player_image)

#=============wall_image================
wall_image = Image.open("./images/walls.png")
wall_image = wall_image.resize((250, 50))
wall_image = ImageTk.PhotoImage(wall_image)

#=============background_start_image================
bg_image = Image.open('./images/shooter.png')
bg_image = bg_image.resize((1400, 700))
background_login = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=background_login, anchor=NW)


#=============Button_help================
help_button = Button(canvas, text='HELP!', width=10, height=-15, bg='dark red', font=('DRIPINK PERSONAL USE Black', 30), border=5, cursor="spider", command=help_window)
help_button.pack()
help_button.place(x=100, y=400)



#=============Button_start================
start_game_button = Button(canvas, text='START GAME', width=10, height=-15, bg='dark red', font=('DRIPINK PERSONAL USE Black', 30), border=5, cursor="spider", command=start_game)
start_game_button.pack()
start_game_button.place(x=420, y=400)

#=============Button_exit================
exit_button = Button(canvas, text='EXIT!', width=10, height=-15, bg='dark red', font=('DRIPINK PERSONAL USE Black', 30), border=5, cursor="spider", command=window.quit)
exit_button.pack()
exit_button.place(x=730, y=400)

#=============Button_story================
def story_button():
    story_game_button = Button(canvas, text='STORY GAME', width=10, height=-15, bg='darkred', font=('DRIPINK PERSONAL USE Black', 30), border=5, cursor="spider", command=story_animation)
    story_game_button.pack()
    story_game_button.place(x=1050, y=400)

story_button()

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()
window.mainloop()