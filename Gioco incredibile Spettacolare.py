import builtin
from time import sleep
import random
# Credentials
print("Insert your username")
name = input()
print("Hello, " + name)
print("Please enter the PIN to try out the Program")

# Builtin Variables

x = builtin.randomperc["x"]


builtin.checkpin()
print("Prepare yourself for this game!")
print("Please wait 1 minute before continuing, we need to load at least 1 TB of functionalities")
sleep(2)
print("Just joking! All the features should've loaded since you started the program")
sleep(0.5)
# Asks you where you want to start your adventure
print("Where would you like to start your adventure at? Type the ID of the area you want to start at to actually start!")
print("Options:\n\"1\" to start in the woods\n\"2\" to start in a dungeon\n\"3\" to start in an haunted mansion")
start = int(input())
print("Quick instructions: type the choice you want to make by saying the letter (ID) of the option you want to "
      "choose\nRemember, this program is CASE SENSITIVE")
# Woods arc
if start == 1:
    print("You find yourself in the woods of MaterTua and there is a mysterious chest behind you")
    sleep(0.5)
    print("What do you do?")
    print("a: You open the chest and see if it has something useful in it")
    print("b: You just don't open it because you don't know if it has something that will kill you")
    print("c: You- wait, why would you eat it")
    opt = input()
    if opt == "a":
        builtin.percentual()
        if x <= 75:
            print("You obtained...")
            sleep(3)
            print("Nothing!")
            # Continue from here
        
        elif x == 76:
            print("EXPlOOOOOOOOOOOOOSION")
            exit()

        else:
            print("Even I don't know how, but you died thanks to something")
            builtin.ask_restart()

# Dungeon arc
elif start == 2:
    print("We're indev lmao")
# Haunted Mansion arc
elif start == 3:
    print("We're indev lmao")
