import random
import os
from art import *
# from dndClasses import *
import time


class playerInfo:
    Name = "Player_name"                     # The name of the character
    Class = "Player_class"                   # The class of the character
    Level = 0                                # The level of the character
    XP = 0                                   # The amount of experience a player has
    AC = 0                                   # Character Armor Class
    TotalHP = 0                              # Total Character Hitpoints
    CurrentHP = 0                            # The current character Hitpoints
    Speed = 0                                # Chacter Speed (ft)
    CharacterAlignment = "Default_alignment"
    # Chacter social alignment used for choices
    Inventory = []


class playerStats:  # class for storing character stats
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0


class playerModifier:  # class for storing chacter modifers
    STR = (playerStats.STR - 10)//2
    DEX = (playerStats.DEX - 10)//2
    CON = (playerStats.CON - 10)//2
    INT = (playerStats.INT - 10)//2
    WIS = (playerStats.WIS - 10)//2
    CHA = (playerStats.CHA - 10)//2


class world:
    regionChoice = ["Argonia", "Scandanavia", "The Forgotten Realms", "Brazil",
                    "Estonia", "Stronghelm"]  # List of possible regions for the player to play in
    # List of possible buildings within a town to play in
    locChoice = ["tavern", "library", "blacksmith",
                 "apothicary", "townhall", "sewer system"]
    # List of possible names for NPCs around town
    NPC_names = ["Garzog", "Lydia", "Angus", "Yonna", "John", "Pengu", "Skeeb"]
    region = random.choice(regionChoice)
    location1 = random.choice(locChoice)
    shopkeeper1 = random.choice(NPC_names)
    location2 = random.choice(locChoice)
    shopkeeper2 = random.choice(NPC_names)


class story:
    mainChoice = ["recover stolen goods", "kill some mischevious goblins",
                  "recover a relgious artifact"]  # List of possible main quests
    # Determines main quest of the story
    mainquest = random.choice(mainChoice)


playerRolls = []
playerRolls.append(random.randrange(3, 18))
playerRolls.append(random.randrange(3, 18))
playerRolls.append(random.randrange(3, 18))
playerRolls.append(random.randrange(3, 18))
playerRolls.append(random.randrange(3, 18))
playerRolls.append(random.randrange(3, 18))


playerRollsModifer = []

for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)


# ---------------------- START ---------------------- #
os.system('cls')
tprint("Command Line\nDungeons and Dragons", font="Cybermedium")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress Enter to continue.")
option = input()
os.system('cls')

# Naming the character
tprint("Naming your\ncharacter", font="Cybermedium")
print("What would you like your character to be called?\n")

playerInfo.Name = str(input())
os.system('cls')

# Describing each character class
tprint("Choosing your\ncharacter's class", font="Cybermedium")
print("Now it's time to choose a character class. Here are all the classes to choose from in DnD.\nEach class has a description of what they do and how they do it.\n\n The hit die is used to get your initial hit points and is used to determine how much health is healed/gained.\n The primary ability is the ability or stat that is used to most in that class.\n The saves stat is used to determine if you character lives or dies when fatally wounded.\n")
time.sleep(1)
print("\n\n--------- Wizard ----------")
print("A scholarly magic-user capable of manipulating the structure of reality.\nHit Die: d6\nPrimary Ability: Intelligence\nSaves: Intelligence & Wisdom")
time.sleep(3)
print("\n\n--------- Warlock ---------")
print("A wielder of magic that is derived from a bargin with an extraplanar entity.\nHit Die: d8\nPrimary Ability: Charisma\nSaves: Wisdom & Charisma")
time.sleep(3)
print("\n\n--------- Sorcerer --------")
print("A spellcaster who draws on inherent magic from a gift or bloodline.\nHit Die: d6\nPrimary Ability: Charisma\nSaves: Constitution & Charisma")
time.sleep(3)
print("\n\n--------- Rogue -----------")
print("A scondrel who uses stealth and trickery to overcome obstacles and enemies.\nHit Die: d8\nPrimary Ability: Dexterity\nSaves: Dexterity & Intelligence")
time.sleep(3)
print("\n\n--------- Ranger ----------")
print("A warrior who combats threats on the edges of civilization.\nHit Die: d10\nPrimary Ability: Dexterity & Wisdom\nSaves: Strength & Dexterity")
time.sleep(3)
print("\n\n--------- Paladin ---------")
print("A holy warrior bound to a sacred oath.\nHit Die: d10\nPrimary Ability: Strength & Charisma\nSaves: Wisdom & Charisma")
time.sleep(3)
print("\n\n--------- Monk ------------")
print("A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.\nHit Die: d8\nPrimary Abiliy: Dexterity & Wisdom\nSaves: Strength and Dexterity")
time.sleep(3)
print("\n\n--------- Fighter ---------")
print("A master of martial combat, skilled with a variety of weapons and armor.\nHit Die: d10\nPrimary Ability: Strength or Dexterity\nSaves: Strength & Constitution")
time.sleep(3)
print("\n\n--------- Druid -----------")
print("A priest of the Old Faith, wielding the powers of nature and adopting animal forms.\nHit Die: d8\nPrimary Ability: Wisdom\nSaves: Intelligence & Wisdom")
time.sleep(3)
print("\n\n--------- Cleric ----------")
print("A priestly champion who wields divine magic in service of a higher power.\nHit Die: d8\nPrimary Ability: Wisdom\nSaves: Wisdom & Charisma")
time.sleep(3)
print("\n\n--------- Bard ------------")
print("An inspiring magician whose power echoes the music of creation.\nHit Die: d8\nPrimary Ability: Charisma\nSaves: Dexterity & Charisma")
time.sleep(3)
print("\n\n--------- Barbarian -------")
print("A fierce warrior who can enter a battle rage.\nHit Die: d12\nPrimary Ability: Strength\nSaves: Strength & Constitution")
time.sleep(3)
print("\n\n--------- Artificer -------")
print("Masters of invention, artificers use ingenuity and magic to unlock extraordinary capabilities in objects.\nHit Die: d8\nPrimary Ability: Intelligence\nSaves: Constitution & Intelligence")

# Choosing a character class
time.sleep(1)
print("\n\nOut of those, which would you like to choose?\n")

classChoosing = True

while classChoosing == True:
    option = input()
    if option == "Wizard" or option == "wizard":
        playerInfo.Class = "Wizard"
        classChoosing = False

    if option == "Warlock" or option == "warlock":
        playerInfo.Class = "Warlock"
        classChoosing = False

    if option == "Sorcerer" or option == "sorcerer":
        playerInfo.Class = "Sorcerer"
        classChoosing = False

    if option == "Rogue" or option == "rogue":
        playerInfo.Class = "Rogue"
        classChoosing = False

    if option == "Ranger" or option == "ranger":
        playerInfo.Class = "Ranger"
        classChoosing = False

    if option == "Paladin" or option == "paladin":
        playerInfo.Class = "Paladin"
        classChoosing = False

    if option == "Monk" or option == "monk":
        playerInfo.Class = "Monk"
        classChoosing = False

    if option == "Fighter" or option == "fighter":
        playerInfo.Class = "Fighter"
        classChoosing = False

    if option == "Druid" or option == "druid":
        playerInfo.Class = "Druid"
        classChoosing = False

    if option == "Cleric" or option == "cleric":
        playerInfo.Class = "Cleric"
        classChoosing = False

    if option == "Bard" or option == "bard":
        playerInfo.Class = "Bard"
        classChoosing = False

    if option == "Barbarian" or option == "barb":
        playerInfo.Class = "Barbarian"
        classChoosing = False

    if option == "Artificer" or option == "artificer":
        playerInfo.Class = "Artificer"
        classChoosing = False

    else:
        print()

# Stat distribution
tprint("Character Stats\nand modifers", font="Cybermedium")
print("Selected class: " + playerInfo.Class + "\n")
print("Normally you would roll a 6-sided die (d6) 4 times and remove the lowest value.\nThese numbers are then distributed to different stats choosen by the player(you).")
print("The number called the modifer is applied to your dice rolls and changes your rolls for better or worse.\n\n")
# Describing what a stat is used for
time.sleep(10)
print("Strength (STR) - Being able to crush a tomato\n")
time.sleep(1)
print("Dexterity (DEX) - Being able to dodge a tomato\n")
time.sleep(1)
print("Constitution (CON) - Being able to eat a bad tomato\n")
time.sleep(1)
print("Intelligence (INT) - Knowing the signs of a bad tomato\n")
time.sleep(1)
print("Wisdom (WIS) - The ability to notice the signs of a bad tomato\n")
time.sleep(1)
print("Charisma (CHA) - Being able to sell a bad tomato\n")
time.sleep(1)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Strength?\n")
option = input()
# Getting the index value of the chosen roll
RollLocation = playerRolls.index(int(option))
# Removing that roll for the list so it can't be used again
playerRolls.pop(RollLocation)
playerStats.STR = option  # Setting the chosen value to the chosen stat
# Getting the modifer of the value
playerModifier.STR = (int(playerStats.STR) - 10)//2

playerRollsModifer.clear()  # Clearing the list of modifers
for rolls in playerRolls:
    # A for loop to get the modifers of the values still in the 'rolls' list
    playerRollsModifer.append((int(rolls) - 10)//2)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Dexterity?\n")
option = input()
RollLocation = playerRolls.index(int(option))

playerRolls.pop(RollLocation)
playerStats.DEX = option
playerModifier.DEX = (int(playerStats.DEX) - 10)//2

playerRollsModifer.clear()
for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Constitution?\n")
option = input()
RollLocation = playerRolls.index(int(option))
playerRolls.pop(RollLocation)
playerStats.CON = option
playerModifier.CON = (int(playerStats.CON) - 10)//2

playerRollsModifer.clear()
for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Intelligence?\n")
option = input()
RollLocation = playerRolls.index(int(option))
playerRolls.pop(RollLocation)
playerStats.INT = option
playerModifier.INT = (int(playerStats.INT) - 10)//2

playerRollsModifer.clear()
for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Wisdom?\n")
option = input()
RollLocation = playerRolls.index(int(option))
playerRolls.pop(RollLocation)
playerStats.WIS = option
playerModifier.WIS = (int(playerStats.WIS) - 10)//2

playerRollsModifer.clear()
for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)

print("\nROLLS:\n" + str(playerRolls) +
      "\nMODS: \n" + str(playerRollsModifer))

print("\n\nWhich roll will go to Charisma?\n")
option = input()
RollLocation = playerRolls.index(int(option))
playerRolls.pop(RollLocation)
playerStats.CHA = option
playerModifier.CHA = (int(playerStats.CHA) - 10)//2

# Print Stats
print("Your stats are: \n"
      + "STR: " + str(playerStats.STR) + " (" + str(playerModifier.STR) + ")\n"
      + "DEX: " + str(playerStats.DEX) + " (" + str(playerModifier.DEX) + ")\n"
      + "CON: " + str(playerStats.CON) + " (" + str(playerModifier.CON) + ")\n"
      + "INT: " + str(playerStats.INT) + " (" + str(playerModifier.INT) + ")\n"
      + "WIS: " + str(playerStats.WIS) + " (" + str(playerModifier.WIS) + ")\n"
      + "CHA: " + str(playerStats.CHA) + " (" + str(playerModifier.CHA) + ")\n")
time.sleep(5)
