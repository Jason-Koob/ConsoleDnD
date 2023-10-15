import random
import DnD


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
    PrimaryStat = DnD.playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.WIS, DnD.playerStats.CHA]
    Skills = stat2skill


class Warlock:
    HitDie = random.randrange(1, 6)
    PrimaryStat = DnD.playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.INT, DnD.playerStats.WIS]
    Skills = stat2skill


class Sorcerer:
    HitDie = random.randrange(1, 6)
    PrimaryStat = DnD.playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.CON, DnD.playerStats.CHA]
    Skills = stat2skill


class Rogue:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.DEX
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.DEX, DnD.playerStats.INT]
    Skills = stat2skill


class Ranger:
    HitDie = random.randrange(1, 10)
    PrimaryStat = DnD.playerStats.DEX, DnD.playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.STR, DnD.playerStats.DEX]
    Skills = stat2skill


class Paladin:
    HitDie = random.randrange(1, 10)
    PrimaryStat = DnD.playerStats.STR, DnD.playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.WIS, DnD.playerStats.CHA]
    Skills = stat2skill


class Monk:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.DEX, DnD.playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.STR, DnD.playerStats.DEX]
    Skills = stat2skill


class Fighter:
    HitDie = random.randrange(1, 10)
    PrimaryStat = DnD.playerStats.STR, DnD.playerStats.DEX
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.STR, DnD.playerStats.CON]
    Skills = stat2skill


class Druid:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.INT, DnD.playerStats.WIS]
    Skills = stat2skill


class Cleric:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.WIS
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.WIS, DnD.playerStats.CHA]
    Skills = stat2skill


class Bard:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.CHA
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.DEX, DnD.playerStats.CHA]
    Skills = stat2skill


class Barbarian:
    HitDie = random.randrange(1, 12)
    PrimaryStat = DnD.playerStats.STR
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.STR, DnD.playerStats.CON]
    Skills = stat2skill


class Artificer:
    HitDie = random.randrange(1, 8)
    PrimaryStat = DnD.playerStats.INT
    SpellSlots = 0
    TotalCantrips = 0
    Saves = [DnD.playerStats.CON, DnD.playerStats.INT]
    Skills = stat2skill
