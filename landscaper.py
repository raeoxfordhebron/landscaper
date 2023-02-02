## Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0 }
]

def cut_grass():
    tool = tools[game["tool"]]
    print(f"You cut the grass with {tool['name']} and make {tool['profit']}")
    game["money"] += tool["profit"]