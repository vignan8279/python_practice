from sys import exit
def gold_rooms():
    print("this room is full of gold. HOw do you want to take?")
    choice = input(">")
    if "o" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a nuber.")
    if how_much < 50:
        print("Nice,you're not greedy, you win!")
        exit(0)
    else:
        dead("you greedy man!")
def bear_room():
    print("there is a bear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door.")
    print("How are you going to move the bear.")
    bear_moved = False
    while True:
        choice = input(">")
        if choice == "take honey":
            dead("the bear looks at you and slaps the face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.")
            print("you can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print("the bear gets pissed off and chews your leggs off.")
        elif choice == "open door" and bear_moved:
            gold_rooms()
        else:
            print("I have noo idea what that means.")
def cthulhu_room():
    print("here see the great evil cthulhu.")
    print("He,it,whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()
def dead(why):
    print(why,"good job")
    eixt(0)
def start():
    print("you are in a dark room.")
    print("there is a door to your right and left.")
    print("which one do you take?")
    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice =="right":
        cthulhu_room()
    else:
        dead("you stumble arountd the room until you starve.")
start()
