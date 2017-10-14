import b3
from b3Conditions import *
from b3Actions import *
from b3SubTrees import *


class CheckHealthAndTryToHeal(b3.Priority):
    def __init__(self):
        healOrBuyHeal = b3.Priority([CheckPotionAndConsumeSEQ(),
                                     CheckBuyPotionGoBuySEQ()])
        childSeq = b3.Sequence([needsHealthCondition(), healOrBuyHeal])
        childList = [childSeq, b3.Succeeder()]
        super().__init__(childList)

class GoEmptyLootHome(b3.Sequence):
    def __init__(self):
        childList = [isFullCondition(),
                    SetGoalToHome(),
                    WalkToGoalSEQ(),
                    SetGoalToHome()]
        super().__init__(childList)

class FullTree(b3.Sequence):
    def __init__(self):
        healthMineAndHome = [isActionEmpty(), CheckHealthAndTryToHeal(), GoMineSEQ(), GoEmptyLootHome()]
        super().__init__(healthMineAndHome)

