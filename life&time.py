from tkinter import *
from PIL import Image, ImageTk
import time

window = Tk()
window.title("Game Timer")
window.geometry('900x800')

score = 0

def update_score(points):
    global score
    score += points
    score_label.config(text=f"Score: {score}")

def clock():
    elapsed_time = time.time() - start_time
    seconds = int(elapsed_time % 60)
    minutes = int(elapsed_time // 60)
    my_label.config(text=f'Time: {minutes:02d}:{seconds:02d}')

    if minutes >= 2:
        my_label.config(text='Time: 02:00')
    else:
        my_label.after(1000, clock)

def generate_life():
    life_image1 = PhotoImage(file="./images/heart.png")
    life_label1.config(image=life_image1)
    life_label1.image = life_image1

    life_image2 = PhotoImage(file="./images/heart.png")
    life_label2.config(image=life_image2)
    life_label2.image = life_image2

    life_image3 = PhotoImage(file="./images/heart.png")
    life_label3.config(image=life_image3)
    life_label3.image = life_image3

    life_image4 = PhotoImage(file="./images/heart.png")
    life_label4.config(image=life_image4)
    life_label4.image = life_image4

    life_image5 = PhotoImage(file="./images/heart.png")
    life_label5.config(image=life_image5)
    life_label5.image = life_image5

def increase_score(event):
    update_score(1)

def update_objects(objects):
    for obj in objects:
        obj['x'] += obj['dx']
        obj['y'] += obj['dy']

        if obj['x'] <= 0 or obj['x'] >= simulation_width - obj['width']:
            obj['dx'] *= -1
        if obj['y'] <= 0 or obj['y'] >= simulation_height - obj['height']:
            obj['dy'] *= 1

def draw_objects(canvas, objects):
    canvas.delete(ALL)
    for obj in objects:
        canvas.create_image(obj['x'], obj['y'], image=obj['image'], anchor=NW)

def run_simulation():
    update_objects(objects)
    draw_objects(canvas, objects)
    window.after(10, run_simulation)

start_time = time.time()

my_label = Label(window, text='', font=("Helvetica", 20), fg='black', bg='pink')
my_label.pack(pady=10)

life_label1 = Label(window, image=None)
life_label1.pack(pady=10)

life_label2 = Label(window, image=None)
life_label2.pack(pady=10)

life_label3 = Label(window, image=None)
life_label3.pack(pady=10)

life_label4 = Label(window, image=None)
life_label4.pack(pady=10)

life_label5 = Label(window, image=None)
life_label5.pack(pady=10)

score_label = Label(window, text="Score: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

clock()

# Define position of time element
my_label.place(x=10, y=10)

# Define position of life elements
life_label1.place(x=10, y=60)
life_label2.place(x=40, y=60)
life_label3.place(x=70, y=60)
life_label4.place(x=100, y=60)
life_label5.place(x=130, y=60)

# Define position of score label
score_label.place(x=10, y=110)

generate_life()

# Bind keyboard events to score actions
window.bind("<KeyPress-a>", increase_score)

# Create the simulation window
simulation_width =500
simulation_height = 700
canvas = Canvas(window, width=simulation_width, height=simulation_height)
canvas.pack()

# Load the ball image
cloud_image = ImageTk.PhotoImage(Image.open("./images/clouds.png").resize((100, 100)))

# Create and add objects to the simulation
objects = [
    {'x': 5, 'y': 100, 'image': cloud_image, 'width': 100, 'height': 100, 'dx':1, 'dy': 0},
    {'x': 80, 'y': 100, 'image': cloud_image, 'width': 70, 'height': 70, 'dx': 1, 'dy': 0},
    {'x': 130, 'y': 150, 'image': cloud_image, 'width': 110, 'height': 110, 'dx': 1, 'dy': 0},
    {'x': 160, 'y': 100, 'image': cloud_image, 'width': 120, 'height': 120, 'dx':1, 'dy': 0},
    {'x': 220, 'y': 150, 'image': cloud_image, 'width': 120, 'height': 120, 'dx':1, 'dy': 0},
    {'x': 250, 'y': 100, 'image': cloud_image, 'width': 65, 'height': 65, 'dx': 1, 'dy': 0},
    {'x': 330, 'y': 100, 'image': cloud_image, 'width': 70, 'height': 70, 'dx':1, 'dy': 0}
]
run_simulation()
window.mainloop()