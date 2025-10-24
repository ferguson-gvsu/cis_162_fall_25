players = {"james" : 23, "hughes" : 32}
print(players)
#players.pop("hughes")
del players["hughes"]
print(players)

players["steve"] = 12
players["alice"] = 0
print(players)
print(len(players))

for i in range(100):
    if "zeke" not in players:
        players["zeke"] = 100
        print('HIT!')
print(players)

for name in players:
    print(name)
    jersey_num = players[name]
    print(jersey_num)

print(players.items())

for k, v in players.items():
    print(f"Key is {k}, value is {v}")

found_key = False
key = ""
for k, v in players.items():
    if v == 23:
        found_key = True
        key = k
        break

print(key)
players.pop(key)
print(players)