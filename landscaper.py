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
    game["money"] += tool_2["profit"]
    
def cut_grass():
    i = input(f"Which tool do you want to use to cut the grass? {1} Primary Tool {2} Secondary Tool")
    i = int(i)
    if(i == 1):
        cut_grass_with_first()
        
    if(i == 2):
        cut_grass_with_second()
    
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
    
def buy_tool():
    i = input(f"Which tool do you want to upgrade? {1} Primary Tool {2} Secondary Tool")
    if(i == 1):
        tool_1 = tools[game["tool 1"]]
        print(f"You have upgraded tool 1 to {tool_1 + 1['name']}")
        buy_tool_1()
        return 0
    
    if(i == 2):
        tool_2 = tools[game["tool 2"]]
        buy_tool_2()
        print(f"You have upgraded tool 2 to {tool_2 + 1['name']}")
        return 0
    
def sell_tool_1():
    tool_1 = tools[game["tool 1"]]
    if(game["tool 1"] <= len(tools) -1):
        print("No tools to sell")
        
    half = tool_1["cost"]/2
    game["money"] =+ half
    game["tool 1"] -= 1
    
def sell_tool_2():
    tool_2 = tools[game["tool 2"]]
    if(game["tool 2"] <= len(tools) -1):
        print("No tools to sell")
        return 0
        
    half = tool_2["cost"]/2
    game["money"] =+ half
    game["tool 2"] -= 1
    
def win_check():
    if(game["tool 1"] == 4 & game["tool 2"] == 4 & game["money"] >= 1000):
        print("You've won the game!")
        return True
    return False

def reset():
    game["money"] = 0
    game["tool"] = 0
    
    
    
while(True):
    i = input(f" {1} Cut Grass {2} Buy Tool {3} Buy Primary Tool {4} Buy Secondary Tool {5} Sell Primary Tool {6} Sell Secondary Tool {7} Reset {8} Quit")
    i = int(i)
    if(i == 1):
        cut_grass()
        
    if(i == 2):
        buy_tool()
        
    if(i == 3):
        buy_tool_1()
        
    if(i == 4):
        buy_tool_2()

    if(i == 5):
        sell_tool_1()
        
    if(i == 6):
        sell_tool_2()
    
    if(i == 7):
        reset()
    
    if(i == 8):
        print("You quit the game")
        break
        
    if(win_check()):
        break
