import tkinter as tk
from PIL import ImageTk, Image
import winsound
import random
window = tk.Tk()
window.title("Scrolling Background Image Example")
window.geometry("1920x1080")
canvas = tk.Canvas(window, width=1920, height=1080)
canvas.pack()

enemyimage_right = Image.open("./images/zombie.png")
enemyimage_right = enemyimage_right.resize((80, 80))
enemyimage_right = ImageTk.PhotoImage(enemyimage_right)
enemy = canvas.create_image(500, 540, image=enemyimage_right)

enemyimage = Image.open("./images/zombie2.png")
enemyimage = enemyimage.resize((80, 80))
enemyimage = ImageTk.PhotoImage(enemyimage)
enemy2 = canvas.create_image(330, 337, image=enemyimage)

# ======== enemy image =======
enemy_images = [
    Image.open("./images/zombie.png"),
    Image.open("./images/zombie.png"),
    Image.open("./images/zombie.png")
]
enemy_images_resized = []
for enemy_image in enemy_images:
    enemy_image_resized = enemy_image.resize((100, 100))
    enemy_image_resized = ImageTk.PhotoImage(enemy_image_resized)
    enemy_images_resized.append(enemy_image_resized)

def create_enemy():
    if enemy_collisions < 3:
        x = random.randint(600, 800)
        y = random.randint(340,350)
        enemy_image = random.choice(enemy_images_resized)
        enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        move_enemy(enemy)

#============ varable =========
enemy_count = 5
move = "right"
spece = 20
count_left = 0
count_right = 0
enemy_collisions = 0
def move_enemy(enemy):
    global count_right, move, count_left, enemy_count,enemy_collisions
    if move == "right":
        if count_right < 20:
            count_right += 1
            canvas.move(enemy, 50, 0)
        else:
            move = "left"
            count_left = 0
    elif move == "left":
        if count_left < 20:
            count_left += 1
            canvas.move(enemy, -50, 0)
        else:
            move = "right"
            count_right = 0
    player_coords = canvas.coords(player)
    enemy_coords = canvas.coords(enemy)
    if (enemy_coords[0] < player_coords[0] + 200 and enemy_coords[0] + 200 > player_coords[0] and enemy_coords[1] < player_coords[1] + 200 and enemy_coords[1] + 200 > player_coords[1]):
        enemy_collisions += 1
        if enemy_collisions >= 3:
            canvas.delete(player)
            game_over()
    canvas.after(200, lambda: move_enemy(enemy))

def game_over():
    winsound.PlaySound("win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_text(700, 200, text="😢😒Game Over🎌🎌", font=("Arial", 50), fill="red", tags="game_over")
#============ bullet ==============
def shoot_bullet(event):
    x, y = canvas.coords(player)
    bullets = canvas.create_rectangle(x + 90, y - 38, 100 + x , y - 33, fill="red", tags="bullet")
    winsound.PlaySound("whip-shot.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.after(10, lambda: move_bullet(bullets))
    bullet_coords = canvas.coords(bullets)
    enemy_list = canvas.find_withtag("enemy")
    for enemy in enemy_list:
        enemy_coords = canvas.coords(enemy)
        overlap = canvas.find_overlapping(bullet_coords[0], bullet_coords[1], bullet_coords[2], bullet_coords[3])
        if enemy in overlap:
            canvas.delete(enemy)
            canvas.delete(bullets)
        else:
            canvas.after(200, lambda: canvas.delete(bullets))
#============ move bullet =========
def move_bullet(bullets):
    canvas.move(bullets, 900, 0)
    bullet_coords = canvas.coords(bullets)
    enemy_list = canvas.find_withtag("enemy")
    for enemy in enemy_list:
        enemy_coords = canvas.coords(enemy)
        overlap = canvas.find_overlapping(bullet_coords[0], bullet_coords[1], bullet_coords[2], bullet_coords[3])
        if enemy in overlap:
            canvas.delete(enemy)
            canvas.delete(bullets)
            break
    else:
        if not enemy_list:
            winsound.PlaySound("win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
# ==============images_player============

player_image = Image.open("./images/army.png")
player_image = player_image.resize((70, 70))
player_image = ImageTk.PhotoImage(player_image)
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
GRAVITY_FORCE = 9
# ===========check_movement player_image ================
def check_movement(dx=0, dy=0):
    player_coords = canvas.coords(player)
    new_x1 = player_coords[0] + dx
    new_y1 = player_coords[1] + dy
    new_x2 = player_coords[0] + dx -20 + player_image.width()
    new_y2 = player_coords[1] + dy -20+ player_image.height()
    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
    for wall_id in canvas.find_withtag("wall"):
        if wall_id in overlapping_objects:
            return False

    return True

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIME, jump, force-1)

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
            jump(30)
        window.after(TIME, move)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

def gravity():
    if check_movement(0, GRAVITY_FORCE):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIME, gravity)

# =========shoot bullet===========
def shoot_bullet(event):
    x, y = canvas.coords(player)
    bullets = canvas.create_rectangle(x + 90, y - 38, 100 + x , y -33 ,fill="red")
    canvas.after(50, lambda: canvas.move(bullets, 200, 0))
    canvas.after(100, lambda: canvas.delete(bullets))

gravity()
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
canvas.bind('<Control_L>', shoot_bullet)
# scroll_background()
window.mainloop()