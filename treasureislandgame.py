print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



#Write your code below this line 👇
choice1=input('you are at the croosroad where u want to go . Type "right" if right and Type "left" if left').lower()
if choice1=="left":
    choice2=input('you come to lake. There is an island in the middle of the lake. Type "wait" if want wait for boat. Type "swim" if you want to swim.').lower()
    if choice2=="wait":
        choice3=input("which color door you want to choose . One 'red'. one 'blue' and one 'red'. Which color do you want to choose ").lower()
        if choice3=="red":
            print("The room is full of fire. Game over Guys")
        elif choice3=="blue":
            print("You Win the game and now you have a lot gold in your bank")
        elif choice3=="yellow":
            print("you win the game the treasure is in this door")
    else:
        print("you loose the game")
else:
    print("you are move to the hole sorry! Game over")
    



