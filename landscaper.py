## Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0 },
    {"name": "scissors", "profit": 5, "cost": 5},
    {"name": "push lawnmower", "profit": 50, "cost": 25},
    {"name": "fancy lawnmower", "profit": 100, "cost": 250},
    {"name": "students", "profit": 250, "cost": 500}
]

def cut_grass():
    tool = tools[game["tool"]]
    print(f"You cut the grass with {tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You are using the {tool['name']} and have {game['money']}")
    
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
    
def win_check():
    if(game["tool"] == 4 & game["money"] >= 1000):
        print("You've won the game!")
        return True
    return False

def reset():
    game["money"] = 0
    game["tool"] = 0
    
    
    
while(True):
    i = input(f" {1} Cut Grass {2} Buy Tool {3} Check Stats {4} Reset")
    i = int(i)
    if(i == 1):
        cut_grass()
        
    if(i == 2):
        buy_tool()
        
    if(i == 3):
        check_stats()
        
    if(i == 4):
        reset()
        
    if(win_check()):
        break
