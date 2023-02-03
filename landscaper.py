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
    print(f"You cut the grass with {tool_2['name']}")
    
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
    i = input(f" {1} Cut Grass {2} Buy Tool {3} Check Stats {4} Reset {5} Quit")
    i = int(i)
    if(i == 1):
        cut_grass()
        
    if(i == 2):
        buy_tool()
        
    if(i == 3):
        check_stats()
        
    if(i == 4):
        reset()
    
    if(i == 5):
        print("You quit the game")
        break
        
    if(win_check()):
        break
