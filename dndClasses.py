import random
from DnD import playerStats


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


class armor:
    # Light (AC + DEX)
    Padded = 11
    Leather = 11
    Studded = 12
    Hide = 12

    # Medium (AC + DEX (MAX 2))
    Chain = 13
    ScaleMail = 14
    Breastplate = 14

    # Heavy
    Ring = 14
    ChainMail = 16
    Splint = 17


class armorMovement:
    Leather = 11
    Studded = 12
    Hide = 12
    Chain = 13
    ScaleMail = 14
    Breastplate = 14
    Ring = 14
    ChainMail = 16
    Splint = 17


class Race:
    class Tiefling:
        Movement = 30
        DarkVision = 1
        Stats = int(playerStats.CHA)+2, int(playerStats.INT)+1

    class Human:
        Movement = 30
        DarkVision = 0
        Stats = int(playerStats.STR)+1, int(playerStats.DEX)+1, int(playerStats.CON) + \
            1, int(playerStats.INT)+1, int(playerStats.WIS) + \
            1, int(playerStats.CHA)+1

    class Gnome:
        Movement = 25
        DarkVision = 1
        Stats = int(playerStats.INT)+2

    class Elf:
        Movement = 30
        DarkVision = 1
        Stats = int(playerStats.DEX)+2

    class Dward:
        Movement = 25
        DarkVision = 1
        Stats = int(playerStats.CON)+2


# print(Race.Tiefling.Stats)


class Wizard:
    HitDie = random.randrange(1, 6)
    PrimaryStat = playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.WIS, playerStats.CHA]
    Skills = stat2skill


class Warlock:
    HitDie = random.randrange(1, 6)
    PrimaryStat = playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.INT, playerStats.WIS]
    Skills = stat2skill


class Sorcerer:
    HitDie = random.randrange(1, 6)
    PrimaryStat = playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.CON, playerStats.CHA]
    Skills = stat2skill


class Rogue:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.DEX
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.DEX, playerStats.INT]
    Skills = stat2skill


class Ranger:
    HitDie = random.randrange(1, 10)
    PrimaryStat = playerStats.DEX, playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.STR, playerStats.DEX]
    Skills = stat2skill


class Paladin:
    HitDie = random.randrange(1, 10)
    PrimaryStat = playerStats.STR, playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.WIS, playerStats.CHA]
    Skills = stat2skill


class Monk:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.DEX, playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.STR, playerStats.DEX]
    Skills = stat2skill


class Fighter:
    HitDie = random.randrange(1, 10)
    PrimaryStat = playerStats.STR, playerStats.DEX
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.STR, playerStats.CON]
    Skills = stat2skill


class Druid:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.INT, playerStats.WIS]
    Skills = stat2skill


class Cleric:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.WIS, playerStats.CHA]
    Skills = stat2skill


class Bard:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.DEX, playerStats.CHA]
    Skills = stat2skill


class Barbarian:
    HitDie = random.randrange(1, 12)
    PrimaryStat = playerStats.STR
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.STR, playerStats.CON]
    Skills = stat2skill


class Artificer:
    HitDie = random.randrange(1, 8)
    PrimaryStat = playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [playerStats.CON, playerStats.INT]
    Skills = stat2skill
