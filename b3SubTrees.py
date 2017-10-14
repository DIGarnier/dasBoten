import b3
from b3Conditions import *
from b3Actions import *


#### HEALTH
class CheckPotionAndConsumeSEQ(b3.Sequence):
    def __init__(self):
        childList = [hasPotionCondition(),
                    ConsumePotion()]
        super().__init__(childList)

class CheckBuyPotionGoBuySEQ(b3.Sequence):
    def __init__(self):
        childList = [canBuyPotionCondition(),
                     SetGoalToShop(),
                     WalkToGoalSEQ(),
                     BuyPotion(),
                     ConsumePotion()]
        super().__init__(childList)

#### WALKING
class CheckStillnessAttackWallSEL(b3.Priority):
    def __init__(self):
        repeatTwiceAttack = b3.Repeater(AttackLastDirection(), 2)
        childSeq = b3.Sequence([wasStillCondition(), repeatTwiceAttack])
        childList = [childSeq, b3.Succeeder()]
        super().__init__(childList)

class GetCheckConsumeNextMoveSEQ(b3.Priority):
    def __init__(self):
        childSeq = b3.Sequence([GetNextMove(),
                                isNextMoveValidCondition(),
                                ConsumeNextMove()])
        childList = [childSeq, b3.Succeeder()]
        super().__init__(childList)

class CheckMove(b3.Sequence):
    def __init__(self):
        isFarFromGoal = b3.Inverter(isNextToGoalCondition())
        isGoalHomeOrNoPath = b3.Priority([isGoalHomeCondition(), isFarFromGoal])
        childList = [isGoalHomeOrNoPath,
                     GetCheckConsumeNextMoveSEQ()]
        super().__init__(childList)


class CheckPathOrCreatePath(b3.Priority):
    def __init__(self):
        isThereNoPath = b3.Inverter(isThereAPathCondition())
        ifNoPathCreateIt = b3.Sequence([isThereNoPath,
                                        CreatePath()])
        childList = [ifNoPathCreateIt, b3.Succeeder()]
        super().__init__(childList)

class WalkToGoalSEQ(b3.Sequence):
    def __init__(self):
        childList = [isThereAGoalCondition(),
                    CheckPathOrCreatePath(),
                    CheckMove(),
                    RemoveGoal()]
        self.id = 1
        super().__init__(childList)

#### MINING

class MineTillFullOrNoLoot(b3.Priority):
    def __init__(self):
        isNotFull = b3.Inverter(isFullCondition())
        childSequence = b3.Sequence([isNotFull,
                        isGoalLootCondition(),
                        isNextToGoalCondition(),
                        MineGoal()])
        childList = [childSequence,  b3.Succeeder()]
        super().__init__(childList)

class CheckIfNearLootOrWalkThere(b3.Priority):
    def __init__(self):
        isFarFromGoal = b3.Inverter(isNextToGoalCondition())
        childSequence = b3.Sequence([isFarFromGoal,
                        WalkToGoalSEQ(),
                        SetGoalToRessource()])
        childList = [childSequence,  b3.Succeeder()]
        super().__init__(childList)

class CheckIfGoalOrSetRessource(b3.Priority):
    def __init__(self):
        isThereNoGoal = b3.Inverter(isThereAGoalCondition())
        childSequence = b3.Sequence([isThereNoGoal,
                        SetGoalToRessource()])
        childList = [childSequence,  b3.Succeeder()]
        super().__init__(childList)

class GoMineSEQ(b3.Sequence):
    def __init__(self):
        childList = [CheckIfGoalOrSetRessource(),
                    CheckIfNearLootOrWalkThere(),
                    MineTillFullOrNoLoot()]
        super().__init__(childList)


        
