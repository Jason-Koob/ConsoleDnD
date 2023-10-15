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
