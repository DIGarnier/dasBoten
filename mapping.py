from structs import *
from implementation import *


class Mapper():
    def __init__(self, size):
        self.grid = GridWithWeights(size, size)
        self.grid.weights = fillWeights(size)
        self.path = []
        self.cost = []

    def updateMap(self, deserialized_map, otherPs):
        self.grid.walls = pointsToTuples(findThings(deserialized_map, [TileContent.Lava, TileContent.Shop, TileContent.Resource]))
        self.grid.shops.extend(pointsToTuples(findThings(deserialized_map, TileContent.Shop)))
        self.grid.loot =pointsToTuples(findThings(deserialized_map, TileContent.Resource))
        self.grid.otherPlayers = otherPs
        self.grid.make_unique()

    def createPath(self, start, goal):
        startT = (start.X, start.Y)
        goalT  = (goal.X, goal.Y)
        came_from, cost_so_far = a_star_search(self.grid, startT, goalT)
        self.path = reconstruct_path(came_from,start=startT,goal=goalT)
        self.cost = cost_so_far

    def getPath(self):
        path = (list(reversed(self.path))[:-2])
        return tuplesToPoints(path)

    def draw(self,option = 1):
        if option:
            draw_grid(self.grid, width=1, path=self.path, start=self.path[0], goal=self.path[-1])
        else:
            draw_grid(self.grid, width=1, number=self.cost, start=self.path[0],goal=self.path[-1])




def findClosestObjects(position, objects):
    if objects:
        if isinstance(objects[0], tuple):
            objects = tuplesToPoints(objects)
        distances = [obj.getDistance(position) for obj in objects]

        if distances:
            distances[0] -= 0.0005

        sortedObjects = [x for _,x in sorted(zip(distances,objects))]

        return sortedObjects
    return []




def whatIsInXDirection(deserialized_map, player_pos, direction):
    xP, yP = player_pos.X, player_pos.Y
    deltaX = xP if xP < 10 else 10
    deltaY = yP if yP < 10 else 10
    pointOfInterest = Point(deltaX, deltaY) + direction
    return deserialized_map[pointOfInterest.X][pointOfInterest.Y].Content
        
            

    

def findThings(dMap, content):
    if not isinstance(content,list):
        content = [content]

    tilesFound = []
    for tiles in dMap:
        for tile in tiles:  
            if tile.Content in content: 
                tilesFound.append(tile)

    return tilesFound


def pointsToTuples(points):
    if not isinstance(points,list):
        points = [points]
    tupleList = [(point.X, point.Y) for point in points]

    return tupleList

def tuplesToPoints(tuples):
    if not isinstance(tuples,list):
        tuples = [tuples]
    pointList = [Point(tupl[0], tupl[1]) for tupl in tuples]
    
    return pointList


def fillWeights(size):
    weights = {}
    for y in range(size):
        for x in range(size):
            weights[(x,y)] = 1

    return weights
