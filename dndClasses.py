import random


class stat2skill:
    Acrobatics = "DEX"
    AnimalHandling = "WIS"
    Arcana = "INT"
    Decption = "CHA"
    History = "INT"
    Insight = "WIS"
    Intimidation = "CHA"
    Investigation = "INT"
    Medicine = "WIS"
    Nature = "INT"
    Perception = "WIS"
    Performance = "CHA"
    Persuasion = "CHA"
    Religion = "INT"
    SlightOfHand = "DEX"
    Stealth = "DEX"
    Survival = "WIS"


class Wizard:
    HitDie = random.randrange(1, 6)
    Armor = 0
    SimpleWeapons = ["Dagger", "Darts", "Slings",
                     "Quarterstaff", 'Light Crossbow']
    SimpleWeaponDamage = [random.randrange(1, 4), random.randrange(
        1, 4), random.randrange(1, 4), random.randrange(1, 6), random.randrange(1, 8)]
    SimpleWeaponAction = ["throw", "shoot", "sling", "hit", "shoot"]
    Tools = 0
    Skills = ["Arcana", "History", "Insight",
              "Investigation", "Medicine", "Religion"]
    StartingInventory = [SimpleWeapons[4], "Component Pouch", "Backpack", "Bedroll", "mess kit",
                         "tinderbox", "10 torches", "10 days of rations", "a waterskin", "50 ft of hempen rope"]
    CantripLimit = 3
    TotalCantrips = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill touch", "Control Flames", "Create Bonfire", "Dancing Flames", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Gust", "Infestastion", "Light", "Lightning Lure",
                     "Mage Hand", "Mending", "Message", "Mind Silver", "Minor Illusion", "Mold Earth", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shape Water", "Shocking Grasp", "Sword Burst", "Thunderclap", "Toll the Dead", "True Strike"]
    TotalCantripDescriptions = [""]
    TotalCantripDamage = []
    TotalCantripRange = [60, 0, 5, 120, 60, 60, 120, 120, 0, 60, 5, 30,
                         30, 5, 15, 30, 5, 120, 60, 30, 30, 10, 10, 60, 30, 5, 5, 5, 60, 30]
    SpellSlots = 2
    SpellsKnown = 6
    TotalSpells = []
    TotalSpellsDescriptions = []
    TotalSpellsDamage = []
    TotalSpellsRange = []

    print(len(TotalCantrips))
    print(len(TotalCantripRange))

    class Warlock:
    
    class Sorcerer:
    
    class Rogue:

    class Ranger:

    class Paladin:

    class Monk:

    class Fighter:

    class Druid:

    class Cleric:

    class Bard:

    class Barbarian:

    class Artificer:

      