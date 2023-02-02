## Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0 },
    {"name": "scissors", "profit": 5, "cost": 5},
    {"name": "lawnmower", "profit": 50, "cost": 25}
]

def cut_grass():
    tool = tools[game["tool"]]
    print(f"You cut the grass with {tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]
    
def buy_tool():
    tool = tools[game["tool"]]
    if(game["tool"] >= len(tools) -1):
        print("No more upgrades")
        return 0
    
    next_tool = tools[game["tool"] +1]
    if(next_tool == None):
        print("There are no more tools")
        return 0
    
    if(game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
    
while(True):
    i = input(f" {1} Cut Grass")
