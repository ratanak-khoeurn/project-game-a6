mport tkinter as tk
from PIL import ImageTk, Image
import winsound
import random

window = tk.Tk()
window.title("Scrolling Background Image Example")
window.geometry("1920x1080")
canvas = tk.Canvas(window, width=1920, height=1080)
canvas.pack()

#======= move player ===============
def move_left(event):
    canvas.move(player, -10, 0)

def move_right(event):
    canvas.move(player, 10, 0)

def jump(event):
    canvas.move(player, 0, -100)
    canvas.after(50, lambda: canvas.move(player, 0, 100))
#=========== player image ==========
player_image = Image.open("./image/soldier.png")
player_image = player_image.resize((200, 200))
player_image = ImageTk.PhotoImage(player_image)
player = canvas.create_image(100, 600, image=player_image)

# ======== enemy image =======
enemy_images = [
    Image.open("./image/zombie.png"),
    Image.open("./image/zombie.png"),
    Image.open("./image/zombie.png")
]
enemy_images_resized = []
for enemy_image in enemy_images:
    enemy_image_resized = enemy_image.resize((200, 200))
    enemy_image_resized = ImageTk.PhotoImage(enemy_image_resized)
    enemy_images_resized.append(enemy_image_resized)

# ========== create enemy ==========
def create_enemy():
    if enemy_collisions < 3:
        x = random.randint(400, 600)
        y = random.randint(500, 600)
        enemy_image = random.choice(enemy_images_resized)
        enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        move_enemy(enemy)
# ========== create enemy ==========
def create_enemy():
    if enemy_collisions < 3:
        x = random.randint(400, 600)
        y = random.randint(500, 600)
        enemy_image = random.choice(enemy_images_resized)
        enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        move_enemy(enemy)


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
        enemy_count -= 1
        if enemy_count <= 0:
            game_win()

    if (enemy_coords[0] < player_coords[0] + 200 and enemy_coords[0] + 200 > player_coords[0] and enemy_coords[1] < player_coords[1] + 200 and enemy_coords[1] + 200 > player_coords[1]):
        enemy_collisions += 1
        if enemy_collisions >= 3:
            canvas.delete(player)
            game_over()

    canvas.after(50, lambda: move_enemy(enemy))

#============= win codition ================
def game_win():
    canvas.create_text(700, 200, text="😎😎Victory!😎😎", font=("Arial", 50), fill="green", tags="game_win")

def game_over():
    canvas.create_text(700, 200, text="😢😒Game Over🎌🎌", font=("Arial", 50), fill="red", tags="game_over")

# Both sokheang, [10/26/2023 1:03 PM]
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
            canvas.after(50, lambda: move_bullet(bullets))
#============ move bullet =========
def move_bullet(bullets):
    canvas.move(bullets, 90, 0)
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
            canvas.create_text(700, 200, text="😎😋YOU WIN!🎉🎁", font=("Arial", 50), fill="green", tags="victory")
            canvas.after(300, lambda: move_bullet(bullets))

# ======= key bindings ===============
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<space>', jump)
canvas.bind('<Control_L>', shoot_bullet)
canvas.focus_set()

# ======= create enemy images =========
for _ in range(5):
    create_enemy()

window.mainloop()