## Game State
game = {"tool 1": 0, "tool 2": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0 },
    {"name": "scissors", "profit": 5, "cost": 5},
    {"name": "push lawnmower", "profit": 50, "cost": 25},
    {"name": "fancy lawnmower", "profit": 100, "cost": 250},
    {"name": "students", "profit": 250, "cost": 500}
]

def cut_grass_with_first():
    tool_1 = tools[game["tool 1"]]
    print(f"You cut the grass with {tool_1['name']} and make {tool_1['profit']}")
    game["money"] += tool_1["profit"]
    
def cut_grass_with_second():
    tool_2 = tools[game["tool 2"]]
    print(f"You cut the grass with {tool_2['name']} and make {tool_2['profit']}")
    
def buy_tool_1():
    tool_1 = tools[game["tool 1"]]
    if(game["tool 1"] >= len(tools) -1):
        print("No more upgrades")
        return 0
    
    next_tool = tools[game["tool 1"] +1]
    if(next_tool == None):
        print("There are no more tools")
        return 0
    
    if(game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool 1"] += 1

def buy_tool_2():
    tool_1 = tools[game["tool 2"]]
    if(game["tool 2"] >= len(tools) -1):
        print("No more upgrades")
        return 0
    
    next_tool = tools[game["tool 2"] +1]
    if(next_tool == None):
        print("There are no more tools")
        return 0
    
    if(game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool 2"] += 1
    
def win_check():
    if(game["tool 1"] == 4 & game["tool 2"] == 4 & game["money"] >= 1000):
        print("You've won the game!")
        return True
    return False

def reset():
    game["money"] = 0
    game["tool"] = 0
    
    
    
while(True):
    i = input(f" {1} Cut Grass with Primary Tool {2} Cut Grass with Secondary Tool {3} Buy Primary Tool {4} Buy Secondary Tool {5} Reset {6} Quit")
    i = int(i)
    if(i == 1):
        cut_grass_with_first()
        
    if(i == 2):
        cut_grass_with_second()
        
    if(i == 3):
        buy_tool_1()
        
    if(i == 4):
        buy_tool_2()

    if(i == 5):
        tool_1 = 0
    
    if(i == 6):
        print("You quit the game")
        break
        
    if(win_check()):
        break
