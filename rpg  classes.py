from random import randint, choice  #importing modules for use later
from time import sleep
import tkinter as tk

window = tk.Tk()  #we make our window
x = 300  #define variables to be used later
y = 100
wid = 500
h = 500

window.wm_title("RPG")  #give the window a title
window.geometry('%dx%d+%d+%d' % (wid, h, x, y))  #specify the window location and size




difficulty = 1  #preset variables to be used later
pause = 1
level = 1

def reset():   #this is the opening statement to begin the function definition
    '''Reset the stuff in our window'''
    for child in window.winfo_children():   #for every thing in the window, run this set of code
        if str(child) == '.!menu':     #if the object is our menu, then continue with the loop without destroying it
             continue
        else:
            child.destroy()   #if it isn't a menu, destroy the object
#if statement so the program doesn't remove the menu

class Player():   #the player
    def __init__(self, enemy):
        self.mults = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
        self.multiplier = choice(self.mults)
        self.health = 50
        
        def sword():    #these functions decide the amount of damage the player does to their opponent, for each turn the player takes the enemy takes another
            enemy.health -= self.multiplier * 8
            self.health -= enemy.multiplier*1.2
            tk.Label(window, text=str(self.health) +"HP Left").place(relx=0.8, rely=0.1)
        def wws():
            enemy.health -= enemy.health/25
            self.health -= enemy.multiplier*1.2
            tk.Label(window, text=str(self.health) +"HP Left").place(relx=0.8, rely=0.1)
        def spear():
            enemy.health -= randint(0, 12)
            self.health -= enemy.multiplier*1.2
            tk.Label(window, text=str(self.health) +"HP Left").place(relx=0.8, rely=0.1)
        def heal():
            self.health += 5
            self.health -= enemy.multiplier*1.2
            tk.Label(window, text=str(self.health) +"HP Left").place(relx=0.8, rely=0.1)
        self.attacks = {"Sword": sword(),
                        "Whack with shield":wws(),
                        "Spear": spear(),
                        "Heal": heal()}

class Enemy():
    def __init__(self):
        self.health = 50
        self.names = ["Mr Smith","Ms Cathcart", "Mr Soulsby", "Mr Timmins"]
        self.name = choice(self.names)
        self.mults = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
        self.multiplier = choice(self.mults)
        self.multiplier = self.multiplier * (difficulty+level)

class rpg():
    def __init__(self, player, enemy):
        self.narrative = [ "o===[]:::::::::::::>\n",  "It is a dark time for students",  "You wander nervously through the hallowed halls of",
                    "Altrincham Grammar School for Boys",  "Dark creatures stalk the corridors"]

def end():
    window.quit()
    
enemy = Enemy()
player = Player(enemy)
game = rpg(player, enemy)
def fight(player, enemy):
    reset()
    global level
    i = 1
    for attack in player.attacks:
        tk.Button(window, text=attack, command = player.attacks[attack]).place(x=20, y=20*i)
        i += 2
    while True:
        if player.health == 0 or player.health < 0:
            end()
            break
        elif enemy.health == 0 or enemy.health < 0:
            level += 1
            Game()
            break
        else:
            continue

def run(player, enemy):
    pass

def instructions():
    reset()
    n = 1
    instruction = ["This is an rpg game", "You have to fight or run from enemies", "Good luck!"]
    for item in instruction:
        tk.Label(window, text=item).place(x = 20, y = 10*n)
        n += 2
def narrative():
    i = 1
    for item in game.narrative:
        i += 2
        tk.Label(window, text=item).place(x=20, y=10*i)

def Game():
    reset()
    if level == 1:
        narrative()
        y_val = 130
    else:
        y_val = 20
    tk.Label(window, text="Your opponent in level " + str(level) + " is " + enemy.name + "!!" ).place(x=20, y=y_val)
    tk.Button(window, text = "Fight", command = lambda : fight(player, enemy)).place(relx=0.2, rely=0.3)
    tk.Button(window, text = "Run", command = lambda : run(player, enemy)).place(relx=0.4, rely=0.3)

def Difficulty():
    reset()
    def easy():
        difficulty  = 1
    def normal():
        difficulty = 2
    def hard():
        difficulty = 3

    Easy = tk.Button(window,  text = "Easy", command = easy).place(relx = 0.167)
    Normal = tk.Button(window,  text = "Normal", command = normal).place(relx = 0.267)
    Hard = tk.Button(window,  text = "Hard", command = hard).place(relx = 0.367)

def __main__():
    reset()
    # creating a root menu to insert all the sub menus
    root_menu = tk.Menu(window)
    window.config(menu = root_menu)

    # creating sub menus in the root menu
    file_menu = tk.Menu(root_menu) # it intializes a new sub menu in the root menu
    root_menu.add_cascade(label = "Menu", menu = file_menu) # it creates the name of the sub menu
    file_menu.add_command(label = "Instructions", command = instructions)
    file_menu.add_command(label = "Change difficulty", command = Difficulty) # it adds a option to the sub menu 'command' parameter is used to do some action
    file_menu.add_command(label = "Play", command = Game)
    file_menu.add_separator() # it adds a line after the options
    file_menu.add_command(label = "Exit", command = window.quit)
__main__()
tk.mainloop()
