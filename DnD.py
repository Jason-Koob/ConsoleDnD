import random

class playerInfo:
        User = "Player_User"                     # The person playing the game
        Name = "Player_name"                     # The name of the character
        Class = "Player_class"                   # The class of the character
        Level = 0                                # The level of the character
        XP = 0                                   # The amount of experience a player has
        AC = 0                                   # Character Armor Class
        TotalHP = 8                              # Total Character Hitpoints
        CurrentHP = 8                            # The current character Hitpoints
        Speed = 0                                # Chacter Speed (ft)
        CharacterAlignment = "Default_alignment" # Chacter social alignment used for choices

class playerStats: # class for storing character stats
        STR = random.randrange(3,18)
        DEX = random.randrange(3,18)
        CON = random.randrange(3,18)
        INT = random.randrange(3,18)
        WIS = random.randrange(3,18)
        CHA = random.randrange(3,18)

class playerModifier: # class for storing chacter modifers
        STR = (playerStats.STR - 10)//2
        DEX = (playerStats.DEX - 10)//2
        CON = (playerStats.CON - 10)//2
        INT = (playerStats.INT - 10)//2
        WIS = (playerStats.WIS - 10)//2
        CHA = (playerStats.CHA - 10)//2

class world:
        regionChoice = ["Argonia", "Scandanavia", "The Forgotten Realms", "Brazil", "Estonia", "Stronghelm"]  # List of possible regions for the player to play in
        locChoice = ["tavern", "library", "blacksmith", "apothicary", "townhall", "sewer system"]             # List of possible buildings within a town to play in
        NPC_names = ["Garzog", "Skeeb", "Angus", "Yonna", "John", "Pengu"]
        region = random.choice(regionChoice)
        location1 = random.choice(locChoice)
        shopkeeper1 = random.choice(NPC_names)
        location2 = random.choice(locChoice)
        shopkeeper2 = random.choice(NPC_names)

class story:
        mainChoice = ["recover stolen goods", "kill some mischevious goblins", "recover a relgious artifact"] # List of possible main quests
        mainquest = random.choice(mainChoice)                                                                 # Determines main quest of the story

# Testing
print(playerStats.STR,    playerStats.DEX,    playerStats.CON,    playerStats.INT,    playerStats.WIS,    playerStats.CHA)
print(playerModifier.STR, playerModifier.DEX, playerModifier.CON, playerModifier.INT, playerModifier.WIS, playerModifier.CHA)
print("Main Quest:       " +story.mainquest)
print("World:            " + world.region)
print("shopkeep1:        " + world.shopkeeper1)
print("Location1:        " + world.location1)
print("shopkeep2:        " + world.shopkeeper2)
print("Location2:        " + world.location2)
