import math

class ActionTypes():
    DefaultAction, MoveAction, AttackAction, CollectAction, UpgradeAction, StealAction, PurchaseAction, HealAction = range(8)

class UpgradeType():
    CarryingCapacity, AttackPower, Defence, MaximumHealth, CollectingSpeed = range(5)

class ItemTypes():
    MicrosoftSword, UbisoftShield, DevolutionBackpack, DevolutionPickaxe, HealthPotion = range(5)

class ItemPrices():
    MicrosoftSword, UbisoftShield, DevolutionBackpack, DevolutionPickaxe, HealthPotion = [40000] * 4 + [5000]

class TileContent():
    Empty, Wall, House, Lava, Resource, Shop, Player = range(7)


class Point(object):

    # Constructor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    # Overloaded operators
    def __add__(self, point):
        return Point(self.X + point.X, self.Y + point.Y)

    def __sub__(self, point):
        return Point(self.X - point.X, self.Y - point.Y)

    def __mul__(self, integer):
        return Point(self.X * integer, self.Y * integer)

    __rmul__ = __mul__

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __ne__(self, other):
        return not self.__eq__(other)

    # Distance between two Points
    def getDistance(self, p2):
        delta_x = self.X - p2.X
        delta_y = self.Y - p2.Y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

    def getManDistance(self, p2):
        return abs(p2.X - self.X) + abs(p2.Y - self.Y)


class GameInfo(object):

    def __init__(self, json_dict):
        self.__dict__ = json_dict
        self.HouseLocation = Point(json_dict["HouseLocation"])
        self.Map = None
        self.Players = dict()


class Tile(object):

    def __init__(self, content=None, x=0, y=0):
        self.Content = content
        self.X = x
        self.Y = y

class PlayerStat(object):
    def __init__(self):
        self.CollectingAmount = 100
        self.AttackPower = 1
        self.Defense = 1
        self.ItemBoughtValue = 0

class Player(object):

    def __init__(self, health, maxHealth, position, houseLocation, score, carriedRessources,
                 carryingCapacity=1000):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position
        self.HouseLocation = houseLocation
        self.Score = score
        self.CarriedRessources = carriedRessources
        self.CarryingCapacity = carryingCapacity
        self.otherStats = PlayerStat()

class PlayerInfo(object):

    def __init__(self, health, maxHealth, position, oldHealth = None, house = None):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position
        self.OldHealth = oldHealth
        self.House = house

class ActionContent(object):

    def __init__(self, action_name, content):
        self.ActionName = action_name
        self.Content = str(content)


class Directions():
    North, West, South, East = Point(0,-1), Point(-1,0), Point(0,1), Point(1,0)

class Strategies():
    DefaultStrategy, Mining, Warring, Stealing = range(4)

class Goals():
    DoNothing, GoEmpty, GoMine, GoHeal, GoShop, GoSteal = range(6)


