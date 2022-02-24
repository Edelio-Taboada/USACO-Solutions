dict = {"Tiger": 1,
        "Rabbit": 2,
        "Dragon": 3,
        "Snake": 4,
        "Horse": 5,
        "Goat": 6,
        "Monkey": 7,
        "Rooster": 8,
        "Dog": 9,
        "Pig": 10,
        "Rat": 11,
        "Ox": 12}
dist = {"Bessie": 0}
year = {"Bessie": "Ox"}
for every in range(int(input())):
    lin = input().split()
    year[lin[0]] = lin[4]
    if lin[3] == "previous":
        if dict[lin[4]] == dict[year[lin[7]]]:
            dist[lin[0]] = dist[lin[7]] - 12
        elif dict[lin[4]] > dict[year[lin[7]]]:
            dist[lin[0]] = dist[lin[7]] - dict[year[lin[7]]] - (12 - dict[lin[4]])
        else:
            dist[lin[0]] = dist[lin[7]] - (dict[year[lin[7]]] - dict[lin[4]])
    else:
        if dict[lin[4]] == dict[year[lin[7]]]:
            dist[lin[0]] = 12 + dist[lin[7]]
        elif dict[lin[4]] > dict[year[lin[7]]]:
            dist[lin[0]] = dist[lin[7]] + (dict[lin[4]] - dict[year[lin[7]]])
        else:
            dist[lin[0]] = dist[lin[7]] + (12 - dict[year[lin[7]]] + dict[lin[4]])
print(abs(dist["Elsie"]))
