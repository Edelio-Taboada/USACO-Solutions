
for each in range(int(input())):
    currentPos = [0,0]
    currentDir = ""
    turnTracker = 0
    for direction in input():
        if direction != currentDir:
            if currentDir == "N" and direction == "E":
                turnTracker += 1
            elif currentDir == "N" and direction == "W":
                turnTracker -= 1
            elif currentDir == "S" and direction == "E":
                turnTracker -= 1
            elif currentDir == "S" and direction == "W":
                turnTracker += 1
            elif currentDir == "E" and direction == "N":
                turnTracker -= 1
            elif currentDir == "E" and direction == "S":
                turnTracker += 1
            elif currentDir == "W" and direction == "N":
                turnTracker += 1
            elif currentDir == "W" and direction == "S":
                turnTracker -= 1
        currentDir = direction
    if turnTracker > 0:
        print("CW")
    elif turnTracker < 0:
        print("CCW")
    else:
        print("huh?")
