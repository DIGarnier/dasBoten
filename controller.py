from structs import *
import json
from resources import *
import numpy as np
import b3

class Controller:
    def __init__(self):
        self.player = Player(0, 0, Point(0,0), Point(0, 0), 0, 1000)
        self.past_player = Player(0, 0, Point(0,0), Point(0, 0), 0, 1000)
        self.potions = 0
        self.path = []
        self.goalPos = Point(-1, -1)
        self.goal = Goals.DoNothing
        self.nextMove = Point(0,-1)
        self.lastDirection = Point(0,0)
        self.action = []
        self.stats = PlayerStat()
        self.mapper = Mapper(90)


    def updatePlayerInfo(self, player_json, player_pos, house_pos):
        self.past_player = self.player
        self.player = Player(player_json["Health"], player_json["MaxHealth"], 
                    player_pos,
                    house_pos, player_json["Score"],
                    player_json["CarriedResources"], player_json["CarryingCapacity"])
        print("Controller: asking stillness for internal purpose")
        if not self.wasStill():
            print("Controller: updating last direction")
            self.lastDirection = self.player.Position - self.past_player.Position

    def resetBot(self):
        self.__init__()

    def getRandomGoal(self):
        randomDistance = np.random.randint(3,9)
        randomDirection = np.random.randint(0,4)
        return self.player.Position + convertIntToDirection(randomDirection) * randomDistance

    def moneyLeft(self):
        return self.player.Score - self.stats.ItemBoughtValue


    #### CONDITIONS
    def wasStill(self):
        print("Controller: wasStill?")
        return self.player.Position == self.past_player.Position

    def isNextToGoal(self):
        print("Controller: are we next to our goal?")
        return self.player.Position.getManDistance(self.goalPos) == 1

    def isNextMoveValid(self):
        print("Controller: isNextMoveValid?")
        return self.player.Position.getManDistance(self.nextMove) == 1

    def isThereAGoal(self):
        print("Controller: isThereAGoal?")
        return self.goalPos != Point(-1, -1)

    def isFull(self):
        print("Controller: isFull?")
        return self.player.CarriedRessources == self.player.CarryingCapacity

    def needsHealth(self):
        print("Controller: needsHealth?")
        return self.player.Health <= (self.player.MaxHealth / 3)
    
    def hasPotion(self):
        print("Controller: hasPotion?")
        return self.potions >= 1

    def canBuyPotion(self):
        print("Controller: canBuyPotion?")
        return self.moneyLeft() >= ItemPrices.HealthPotion

    def isGoalLoot(self):
        print("Controller: is Goal some loot?")
        for x,y in self.mapper.grid.loot:
            if Point(x,y) == self.goalPos:
                return True
        return False

    def isGoalHome(self):
        print("Controller: is home the goal?")
        if self.goalPos == self.player.HouseLocation:
            return True
        return False

    def isThereAPath(self):
        print("Controller: isThereAPath?")
        if self.path:
            return True
        return False


    #### ACTIONS

    def getNextMove(self):
        print("Controller: Get next move")
        if self.path:
            self.nextMove = self.path.pop()
            if self.nextMove.getManDistance(self.player.Position) != 1:
                self.mapper.createPath(self.player.Position, self.goalPos)
                self.path = self.mapper.getPath()
                self.nextMove = self.path.pop()
            return True
        return False

    def consumePotion(self):
        print("Controller: Consumed a potion")
        self.action.append(create_heal_action())
        self.potions -= 1

    def consumeNextMove(self):
        print("Controller: Consumed next move")
        self.action.append(create_move_action(self.nextMove))

    def attackLastDirection(self):
        print("Controller: Attacked last direction")
        self.action.append(create_attack_action(self.player.Position + 
        self.lastDirection))

    def mineGoal(self):
        print("Controller: Mined Goal")
        print("Ressources on player: ", self.player.CarriedRessources)
        self.action.append(create_collect_action(self.goalPos))

    def buyPotion(self):
        print("Controller: Bought potion")
        self.action.append(create_purchase_action(ItemTypes.HealthPotion))
        self.stats.ItemBoughtValue += ItemPrices.HealthPotion
        self.potions += 1

def convertIntToDirection(intDirection):
    direction = Point(0,0)
    if intDirection == 0:
        direction = Directions.North
    if intDirection == 1:
        direction = Directions.West
    if intDirection == 2:
        direction = Directions.South
    if intDirection == 3:
        direction = Directions.East
    return direction