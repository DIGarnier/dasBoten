from flask import Flask, request
from structs import *
import json
import numpy as np

from mapping import *
from implementation import *
from resources import *
from controller import *
from b3Tree import FullTree


app = Flask(__name__)


controller = Controller()
tree = b3.BehaviorTree()
tree.root = FullTree()
bb = b3.Blackboard()



def bot():
    """
    Main de votre bot.
    """
    global controller, tree , bb

    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map)
    p = map_json["Player"]
    #print("player:{}".format(p))
    pos_json = p["Position"]
    player_pos = Point(pos_json["X"],pos_json["Y"])

    house = p["HouseLocation"]
    house_pos = Point(house["X"], house["Y"])
    
    
    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)

    otherPlayers = []

    for players in map_json["OtherPlayers"]:
        player_info = players["Value"]
        p_pos = player_info["Position"]
        player_info = PlayerInfo(player_info["Health"],
                                player_info["MaxHealth"],
                                Point(p_pos["X"], p_pos["Y"]))

        otherPlayers.append(player_info)

    #########  TESTING  ########
    otherPs = [x.Position for x in otherPlayers]

    """ UPDATING """

    controller.updatePlayerInfo(p,player_pos,house_pos)
    controller.mapper.updateMap(deserialized_map, otherPs)

    """ Behavior Tree """
    tree.tick(controller, bb)


    print("playerPos:", player_pos, "ressourceCarrying:", controller.player.CarriedRessources, "Score:", controller.player.Score)
    print("house Pos:", house_pos ,"Health:", controller.player.Health, "Goal Pos:", controller.goalPos)
    print(controller.player.CarryingCapacity)
    decision = create_attack_action(player_pos)
    if controller.action:
        print("Sending one action to server")
        decision = controller.action.pop()
        print(decision)
    return decision


@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)