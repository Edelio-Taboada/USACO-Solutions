for each in range(int(input())):
    dicty = {"N": 0,
        "S":0,
        "E": 0,
        "W": 0
    }
    
    for i, dir in enumerate(input()):
        dicty[dir] = dicty[dir] + 1
    if dicty["N"] > dicty["S"]:
        if dicty["W"] > dicty["S"]:
            print("CC")
        else:
            print("CCW")
    else:
         if dicty["W"] > dicty["S"]:
            print("CCW")
        else:
            print("CC")
        
