import b3
from controller import *

###### WALKING CONDITIONS
class wasStillCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.wasStill():
            print("Conditions: was actually still!")
            return b3.SUCCESS
        print("Conditions: moved last turn")
        return b3.FAILURE

class isNextToGoalCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isNextToGoal():
            print("Conditions: is next to goal!")
            return b3.SUCCESS
        print("Conditions: is far from goal")
        return b3.FAILURE

class isNextMoveValidCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isNextMoveValid():
            print("Conditions: next move is valid!")
            return b3.SUCCESS
        print("Conditions: invalid move")
        return b3.FAILURE

class isThereAGoalCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isThereAGoal():
            print("Conditions: there is!")
            return b3.SUCCESS
        print("Conditions: no goal")
        return b3.FAILURE

class isThereAPathCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isThereAPath():
            print("Conditions: there is!")
            return b3.SUCCESS
        print("Conditions: no path")
        return b3.FAILURE

class isGoalHomeCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isGoalHome():
            print("Conditions: yes it is!")
            return b3.SUCCESS
        print("Conditions: it isn't")
        return b3.FAILURE

###### HEALTH CONDITIONS
class needsHealthCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.needsHealth():
            print("Conditions: needs health!")
            return b3.SUCCESS
        print("Conditions: does not need health")
        return b3.FAILURE

class hasPotionCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.hasPotion():
            print("Conditions: have a potion!")
            return b3.SUCCESS
        print("Conditions: have no potion")
        return b3.FAILURE

class canBuyPotionCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.canBuyPotion():
            print("Conditions: can buy potion!")
            return b3.SUCCESS
        print("Conditions: cannot buy potion")
        return b3.FAILURE

##### MINING CONDITIONS
class isFullCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isFull():
            print("Conditions: is Full")
            return b3.SUCCESS
        print("Conditions: is not Full")
        return b3.FAILURE

class isGoalLootCondition(b3.Condition):
    def tick(self, tick):
        if tick.target.isGoalLoot():
            print("Conditions: loot is still there!")
            return b3.SUCCESS
        print("Conditions: no loot")
        return b3.FAILURE



#### GLOBAL CONDITIONS
class isActionEmpty(b3.Condition):
    def tick(self, tick):
        if tick.target.action:
            print("Conditions: Action is not empty!")
            return b3.FAILURE
        print("Conditions: Action is empty")
        return b3.SUCCESS
