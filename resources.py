
from actions import *
from implementation import *
from mapping import *

def followPath(path):
    pos = convertTuplePoint(path.pop())
    return create_move_action(pos)
