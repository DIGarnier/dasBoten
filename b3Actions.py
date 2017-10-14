import b3
from controller import *
from mapping import *



class ConsumePotion(b3.Action):
    def tick(self, tick):
        target = tick.target
        if not target.action:
            print("Action: Want to consume potion")
            target.consumePotion()
        return b3.SUCCESS

class ConsumeNextMove(b3.Action):
    def tick(self, tick):
        target = tick.target
        if not target.action and target.nextMove:
            print("Action: Want to consume next move")
            target.consumeNextMove()
        return b3.SUCCESS        


class GetNextMove(b3.Action):
    def tick(self, tick):
        target = tick.target
        if target.getNextMove():
            print("Action: got next move!")
            return b3.SUCCESS
        print("Action: didnt get next move")
        return b3.FAILURE

class SetGoalToShop(b3.Action):
    def tick(self, tick):
        target = tick.target
        goal = findClosestObjects(target.player.Position, 
        target.mapper.grid.shops)
        if not goal:
            print("Action: didnt find any shops")
            return b3.FAILURE
        else:
            print("Action: set goal to nearest shop")
            target.goalPos = goal[0]
            target.goal = Goals.GoShop
            return b3.SUCCESS

class SetGoalToRessource(b3.Action):
    def tick(self, tick):
        target = tick.target
        goal = findClosestObjects(target.player.Position, 
        target.mapper.grid.loot)
        if not goal:
            print("Action: didnt find any loot")
            return b3.FAILURE
        else:
            print("Action: set goal to nearest loot")
            target.goalPos = goal[0]
            target.goal = Goals.GoMine
            return b3.SUCCESS

class SetGoalToHome(b3.Action):
    def tick(self, tick):
        target = tick.target
        target.goalPos = target.player.HouseLocation
        target.goal = Goals.GoEmpty
        print("Action: set goal to home")
        return b3.SUCCESS 

class RemoveGoal(b3.Action):
    def tick(self, tick):
        tick.target.goalPos = Point(-1,-1)
        tick.target.goal = Goals.DoNothing
        print("Action: remove goal")
        return b3.SUCCESS

class CreatePath(b3.Action):
    def tick(self, tick):
        target = tick.target
        bias = Point(0, 0)
        if target.goal == Goals.GoMine or target.goal == Goals.GoShop:
            i = np.random.randint(0,4)
            bias = convertIntToDirection(i)

        target.mapper.createPath(target.player.Position, target.goalPos + bias)
        target.path = target.mapper.getPath()
        print("Action: create path")
        return b3.SUCCESS

class AttackLastDirection(b3.Action):
    def tick(self, tick):
        target = tick.target
        if not target.action:
            print("Action: attacking last direction")
            target.attackLastDirection()
            return b3.SUCCESS

class MineGoal(b3.Action):
    def tick(self, tick):
        target = tick.target
        if not target.action:
            print("Action: mining goal")
            target.mineGoal()
            return b3.SUCCESS

class BuyPotion(b3.Action):
    def tick(self, tick):
        target = tick.target
        if not target.action:
            print("Action: buying potion")
            target.buyPotion()
            return b3.SUCCESS
   