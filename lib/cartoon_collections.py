import pdb

def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print(f"{index +1}. {dwarf}")
    pass

def summon_captain_planet(calls):
    return [f"{call.title()}!" for call in calls]

def long_planeteer_calls(calls):
    long_calls = [call for call in calls if len(call) > 4]
    return len(long_calls) > 0

def find_the_cheese(possible_cheeses):
    cheeses = set(["cheddar", "gouda", "camembert"])
    equality = cheeses.intersection(set(possible_cheeses))
    # pdb.set_trace()
    return equality.pop() if len(equality) > 0 else None

# def find_the_cheese(foods):
    
#     for food in foods:
#         if food in CHEESES:
#             return food

#     return None
