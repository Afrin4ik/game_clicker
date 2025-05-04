import pgzrun

import pgzero.game
import pgzero.keyboard
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.clock import schedule_interval
from pgzero.constants import mouse

keyboard: pgzero.keyboard.keyboard
screen: pgzero.game.screen



WIDTH = 600
HEIGHT = 400

TITLE = "Clicker"

FPS = 30

fon = Actor("fon")
enemy = Actor("enemy", (400, 230))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))
win = Actor("win")
button_game = Actor("bonus", (300, 180))
button_gallery = Actor("bonus", (300, 280))
button_menu = Actor("bonus", (300, 280))

enemy_1 = Actor("enemy", (150, 80))
enemy_2 = Actor("enemy_2", (280, 80))
enemy_3 = Actor("enemy_3", (450, 80))
enemy_4 = Actor("enemy_4", (220, 230))
enemy_5 = Actor("enemy_5", (400,230))
button_menu_2 = Actor("bonus", (300, 350))

count = 0
price_1 = 15
price_2 = 100
hp = 50
damage = 1

mode = "menu"

def draw():
    global hp
    if mode == "game":
        fon.draw()
        enemy.draw()
        screen.draw.text(f"Счёт: {str(count)}", center=(510, 20), color="black", fontname="segoeprintbold", fontsize=30)
        bonus_1.draw()
        bonus_2.draw()
        screen.draw.text("1 урон каждые 2 секунды", center=(100, 80), color="black", fontname="segoeprintbold", fontsize=13)
        screen.draw.text("+5 к счёту каждые 3 секунды", center=(100, 180), color="black", fontname="segoeprintbold", fontsize=12)
        screen.draw.text(str(price_1), center=(100, 110), color="black", fontname="segoeprintbold", fontsize=25)
        screen.draw.text(str(price_2), center=(100, 210), color="black", fontname="segoeprintbold", fontsize=25)
        screen.draw.text(str(hp), center=(400, 130), color="red", fontname="segoeprintbold", fontsize=36)
        if hp <= 0 and enemy.image == "enemy":
            hp = 100
            enemy.image = "enemy_2"
        elif hp <= 0 and enemy.image == "enemy_2":
            hp = 250
            enemy.image = "enemy_3"
        elif hp <= 0 and enemy.image == "enemy_3":
            hp = 500
            enemy.image = "enemy_4"
        elif hp <= 0 and enemy.image == "enemy_4":
            hp = 1000
            enemy.image = "enemy_5"
        elif hp <= 0 and enemy.image == "enemy_5":
            win.draw()
            screen.draw.text("Вы победили!", center=(300, 100), color="white", fontname="segoeprintbold", fontsize=40)
            button_menu.draw()
            screen.draw.text("Вернуться в меню", center=(300, 270), color="black", fontname="segoeprintbold", fontsize=20)

    elif mode == "menu":
        win.draw()
        button_game.draw()
        button_gallery.draw()
        screen.draw.text("Играть", center=(300, 170), color="black", fontname="segoeprintbold", fontsize=24)
        screen.draw.text("Коллекция", center=(300, 270), color="black", fontname="segoeprintbold", fontsize=24)

    elif mode == "gallery":
        win.draw()
        enemy_1.draw()
        enemy_2.draw()
        enemy_3.draw()
        enemy_4.draw()
        enemy_5.draw()
        button_menu_2.draw()
        screen.draw.text("Вернуться в меню", center=(300, 350), color="black", fontname="segoeprintbold", fontsize=20)



def for_bonus_1():
    global hp
    hp -= 1

def for_bonus_2():
    global count
    count += 5



def on_mouse_down(button, pos):
    global count, mode, hp, damage, price_1, price_2
    if button == mouse.LEFT or button == mouse.RIGHT:
        if enemy.collidepoint(pos) and mode == "game":
            count += 1
            hp -= damage
            enemy.y = 200
            animate(enemy, tween="bounce_end", duration=0.5, y=230)
        elif bonus_1.collidepoint(pos):
            if count >= price_1:
                schedule_interval(for_bonus_1, 2)
                count -= price_1
                price_1 *= 2
        elif bonus_2.collidepoint(pos):
            if count >= price_2:
                schedule_interval(for_bonus_2, 3)
                count -= price_2
                price_2 *= 2

        elif button_game.collidepoint(pos):
            mode = "game"
        elif button_gallery.collidepoint(pos):
            mode = "gallery"

        elif button_menu.collidepoint(pos):
            mode = "menu"

        elif button_menu_2.collidepoint(pos):
            hp = 5
            mode = "menu"
            enemy.image = "enemy"
            count = 0







pgzrun.go()