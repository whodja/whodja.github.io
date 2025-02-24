#Reid Holloway
#~/csc1710/program5/dungeon.py
#CSC1710-02
#12/8/2022
#Creating a dungeon
#For this program I created a dungeon that requires 10 encounters to escape from
#This program includes the 95% program as I did not import my monsters
#In this program I gave the user a chance to flee, multiple attack options, a random chance of retreet failure, a shop with items to help the user
#I included status updates after battles, encounters, a menu, input validation, and a complete story throughout it all
import random
#First the allgolf class keeps track of the gold the player has
#it transfers in and out gold as it is used in shops and gained in battle
class AllGold:
    def __init__(self, bal):
        self.__balance = bal
    def deposit(self, amount):
        self.__balance += amount
    def lost(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
    def balance(self):
        return self.__balance
#This Inventory class organizes the inventory of the player as they upgrade weapons and use spells
class Inventory:
    def __init__(self, store):
        self.__storage = store
    def get_slayer(self):
        self.__storage[0][0] = "slayer sword"
        self.__storage[0][1] = 10
    def get_potion(self):
        self.__storage[2][1] += 1
    def get_iron(self):
        self.__storage[0][0] = "iron sword"
        self.__storage[0][1] = 6
    def total(self):
        for x in range(len(self.__storage)):
                print(self.__storage[x][0], end=", ")
    def battle(self):
        return self.__storage
    def oneshot(self):
        self.__storage[1][1] = 100
    def invisi(self):
        self.__storage[2][1] -= 1
#The health class keeps track of the user's health as they take damage or get healed
class Health:
    def __init__(self, h):
        self.__health = h
    def taken(self, left):
        self.__health = left
    def remaining(self):
        h = self.__health
        return h
    def for_battle(self):
        num = int(self.__health)
        return num
    def healing(self):
        self.__health += 10
        if self.__health >= 100:
            self.__health = 100
    def showshop(self):
        self.__health += 10
        if self.__health >= 100:
            self.__health = 100
        return self.__health


#The main function introduces the story and as well as continues the loop for 10 full encounters
def main():
    x = input("Please input your character's name: ")
    print("Welcome ",x ,", you are an adventurer looking for weary foes to fight." '\n' "You stumble upon a cave with a weary old man out front" '\n' "He warns you of a dungeon ahead and the tretcherous foes that lie within it." '\n' "After hearing your interest to enter the dungeon he bestows upon you these words:" '\n' '\n' '"Its dangerous to go alone! Take this!"' '\n' '\n' "He bestows you with a wooden sword as you enter the dark and gloomy entrance hoping you come out the exit" '\n')
    print("As you walk in you look back on last time on the old man when the doors begin to shut")
    print("You see a group of zombies surround him but its too late for you to react, the door has almost sealed")
    print("You must remember what the old man told you and navigate through 10 encounters in the dungeon to reach the end and avenge him")
    print("Good luck traveler")
    encounterProb = 80  # probability of encountering a monster
    monsterDictionary = loadMonsterDictionary()
#The base variables for the classes are added in to use the same vaiables with the same class the entire time
    storage = ["Wood sword", 2], ["Spell", 20], ["Invisibility potion", 1]
    money = 0
    wealth = AllGold(money)
    mystuff = Inventory(storage)
    health = 100
    life = Health(health)
    step = 0
    endlife = life.for_battle 
#this while loop tracks if 10 encounters have happened
#if they have it ends the loop and ends the program
    while step < 10:
#The user is sent to the menu function to decide what direction they would like to go
        choice = mainMenu()
        while choice == "r":
#if the user choses to rest they are sent to the shop to purchase upgrades and healing
            shop(wealth, mystuff, life)
            choice = mainMenu()
#an 80% chance for a monster occurs where if a monster appears then the monster and its information is sent to the battle function
        if random.randint(0, 100) < encounterProb:
           battle(monsterDictionary, wealth, mystuff, life)
#if the user dies they are sent straight out of the loop and to the ending text
           if life.for_battle <= 0:
            step == 10
        else:
#if no monster appears in the room it does not count as an encounter 
            print("\nThe room is empty.")
            step -= 1
#after the user's battle their stats are then displayed in the stats function
        printPlayerStats(wealth, mystuff, life)
        step = step + 1
#A message appears to the user after their 5th encounter to continue the story and its impact on the game
        if step == 5:
            print("(Suddenly, you hear the voice of the old man who gave you your sword)" '\n')
            print("Weary Traveler, while your journey so far has been trecherous you must still keep your head up!" '\n' "For there are monsters afoot, defeat 5 more and you may go free!")
            print("Knowing that he believes in you, you stay ready for battle and what may come in the next room" '\n')
#if the user is still alive at the end they will be greated with the ending
    if endlife > 0:
        print("\n" "Now, you have finally defeated your last foe" '\n' "You finaly stumble upon a chest filled with all the riches you could imagine but ")
#if the user dies they are given and end of game text after dying
    else: 
        print("As your vision slowly fades to black you remember the old man as the memmory of you both fades from existance left to the dungeon")
        print("GAME OVER")
#the shop function is drawn to when the user decides to chose the shop in the menu
def shop(w, m, h): 
    print('\n' "Welcome to the Shop!" '\n')
    items = 0
    fire = 0 
    slayer = 0
    iron = 0
    health = h.for_battle()
    while fire == 0:  
#while the loop is going the user will not be able to leave the function unless they enter the correct digit
#the user is only allowed to pick from the given menu provided for the shop
        usermoney = w.balance()
        print("Your current gold: ", usermoney, '\n')
        print("(1). Slayer Sword: 30 coins")
        print("(2). Invisibility Potion: 10 coins")
        print("(3). One-Shot Spell: 30 coins")
        print("(4). Iron Sword: 15 coins") 
        print("(5). Healing Potion: 10 coins") 
        print("(6) to exit back to the room")
        buy = int(input(""))
        while buy != 1 and buy != 2 and buy != 3 and buy != 4 and buy != 5 and buy != 6:
            print('\n' "Please enter a valid value to navigate the shop" '\n')
            print("Your current gold: ", usermoney, '\n')
            print("(1). Slayer Sword: 30 coins")
            print("(2). Invisibility Potion: 10 coins")
            print("(3). One-Shot Spell: 30 coins")
            print("(4). Iron Sword: 15 coins") 
            print("(5). Healing Potion: 10 coins") 
            print("(6) to exit back to the room")
            buy = int(input(""))
#if the user buys a sword that sword then replaces the sword they already own along with its stats
        if buy == 1 and slayer == 0:
#if the user can afford the item the money is removed from the AllGold class and the item is added to the Inventory class
            if usermoney >= 30:
                m.get_slayer()
                print("Congratulations!! With the power of the Slayer Sword you may now slaughter every beast with ease!")
                w.lost(30)
            else:
                print("You are need more coins to purchase this item!" '\n')
        if buy == 1 and slayer == 1:
#if the user owns the item they will be reminded of so to make sure they do not waste gold on something they already own
            print("You already own this item! Why would you buy it again?"'\n'"Go! Pick another item!")
#The user has no limit on potions so they are not told when to stop
        if buy == 2:
            if usermoney >= 10: 
                m.get_potion()
                w.lost(10)
                print("Congratulations!! With another potion you may now swiftly maneuver around enemies 2 turns at a time!")
            else:
                print('\n' "You are need more coins to purchase this item!" '\n')
#if the user enters 6 the while loop will end and end the function
        if buy == 6:
            fire = 1  
        if buy == 3:
#if the user has the funds they may buy a spell but they will be told if otherwise
            if usermoney >= 30:
                m.oneshot()
                w.lost(30)
                print("Congratulations! With this spell you may do 20 damage to any enemy!" '\n' "Use this power wisely...")
            else:
                ("You do not have the funds to buy this right now" '\n')
        if buy == 4 and iron == 0:
#just like the other sword, the user will be told if they already own it to not waste their money
            if usermoney >= 15:
                m.get_iron()
                print("Congratulations!! With the power of the Iron Sword you may now slaughter every beast with ease!")
                w.lost(15)
            else:
                print("You are need more coins to purchase this item!" '\n')
        if buy == 4 and iron == 1:
            print("You already own this item! Why would you buy it again?"'\n'"Go! Pick another item!")    
        if buy == 5 and health < 100:
#the user may heal themsealves but cannot exceed 100 health
            if usermoney >= 10:
                w.lost(10)
                h.healing()
                health = h.for_battle()
                print("You have successfully gained 10 health" '\n' "Your Health:", health )
 


        
                
        
        


# The loadMosterDictionary() function returns a hard-coded dictionary
# For 5 points, it could read a file and load a better dictionary
def loadMonsterDictionary():
#This dictionary contains all the monsters and their chance of appearing, health, gold drop, and attack damage
    md = {"Skeleton":[20, 3, 6, 0, 4, 5, 10],
          "Zombie":[10, 4, 8, 2, 7, 10, 20],
          "Vampire":[10, 5, 10, 1, 10, 5, 30],
          "Vampire Queen":[8, 8, 15, 2, 15, 1, 50],
          "Dragon":[4, 10, 30, 5, 20, 50, 200]}
    return md


# The mainMenu() function displays a menu and returns the desired move
def mainMenu():
# the user inputs what move they would like to to 
# input validation makes sure it is a possible move to be read by the program
    move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (r)est to use the shop>")
    while move != "n" and move != "s" and move != "w" and move != "e" and move != "r":
        print("Please input the proper letter of what you would like to do next" '\n')
        move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (r)est to use the shop>")
    return move


# The printPlayerStats() function shows the player's info
# the classes are called back to to show the current health, wealth, and inventory of the user
def printPlayerStats(w, m, h):
    yours = m.battle()
    health = h.for_battle()
    print("\nStats\n")
    print("Total Gold: ", w.balance() )
    print("Weapons available: " )
    for x in range(len(yours)):
        print(yours[x][0])
    print("Current Health:", health )

# The battle() function needs to loop until there is a winner
def battle(md, w, m, h):
    mKey = selectMonster(md)
# in the battle function a battle occurs until the user or monster wins
    print("\nYou have encountered a", mKey)
# the class variables are converted to other variables to make them easier to use with other variables
    inventory = m.battle()
    health = h.for_battle()
    flee_attempt = 1
    flee_success = 0
    monsterhealth = random.randint(md[mKey][1], md[mKey][2])
    while health > 0 and monsterhealth > 0 and flee_success == 0:
# the user is told their health and the monsters as well as the damage the monster has done to them
        print("Your Health:", health)
        print("Monster Health:", monsterhealth, '\n')
        mattack = random.randint(md[mKey][3], md[mKey][4])
        health -= mattack
        print("The ",mKey, "strikes you and does", mattack, "damage !" '\n' "Your Health: ", health)
        print("Your turn to strike! Would you like to use your (s)word, (p)otion, (c)ast a spell, or (f)lee?" )
        attack = input("")
# there is input validation to make sure the user enters an attack that can be used
        while attack != "f" and attack != "s" and attack != "p" and attack != "c":
            print("Please input a valid meathod to attack" '\n')
            print("Your turn to strike! Would you like to use your (s)word, (p)otion, (c)ast a spell, or (f)lee?" )
            attack = input("")
# the variable attached to the Inventory function is called to do the proper damage of the sword
        if attack == "s":
            print("With your sword you slash the beast and deal ",inventory[0][1], " damage")
            monsterhealth -= inventory[0][1]
# the Inventory variable calls to the number of spells left for use and the damage they do
        if attack == "c":
            if inventory[1][1] == 0:
                print("You used your last spell! After you realizer your mistake you lose your turn!")
                print("With your spell you cast fire to the beast and deal ",inventory[1][1], " damage")
            monsterhealth -= inventory[1][1]
            inventory[1][1] = 0 
# the Inventory variable makes sure the user has a potion to use and tells them if they dont
        if attack == "p" and inventory[2][1] == 1:
            print("With your invisibility potion you swiftly move undetected for the rest of the fight!")
            m.invisi()
            inventory[2][1] -= 1
        if attack == "p" and inventory[2][1] == 0:
            print("As you rush to find your next potion you realize you are out!!!!")
            print("While you panic the beast gets a hit on you!")
# the user has a 80% flee rate but still have 20% for it to fail
        if attack == "f" and flee_attempt == 1:
            rand = random.randint(0, 10)
            if rand > 8:
                print("You attempted to runaway but failed!" '\n' "Continue the Fight!!!")
                flee_attempt = 0
            if rand <= 8:
                print('\n' "You throw a nearby stone to distract the beast and safely get away" '\n')
                flee_success = 1 
                h.taken(health)
# if the monster is then killed the user is told the number of gold they drop which is then sent to the AllGold class
    if monsterhealth <= 0 and flee_success == 0:
        print("You have slayed the beast")
        monstergold = random.randint(md[mKey][5], md[mKey][6])
        print("The ", mKey, "dropped ", monstergold, "gold")
        w.deposit(monstergold)
        h.taken(health)
        
    
    

# The selectMonster() function takes a dictionary as an argument.
# It returns a randomly selected key (a monster name).
# You are allowed to use this function as is.
def selectMonster(md):
    # Create 2d list of monster names and likelihoods.
    allMonsters = []
    for key in md:
        allMonsters.append([key, md[key][0]])
    # Find total of all likelihoods.
    total = 0
    for m in allMonsters:
        total = total + m[1]
    # Randomly, generate a number within the total
    selection = random.randint(0, total-1)
    # find the key based on random number
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]
# the main function is called to in order to properly commence the program
main()
