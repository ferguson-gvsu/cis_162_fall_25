import os

enemies = []
filename = 'monsters.csv'
if not os.path.isfile(filename):
  print(f'Error! Could not find file: {filename}')
  exit(1)
file = open(filename, 'r')
header = file.readline()
for line in file:
  line = line.rstrip()
  # Skip empty lines
  if line == '':
    continue
  line_parts = line.split(',')
  if len(line_parts) != 4:
    print(f'Found an invalid line: {line}')
  else:
    name = line_parts[0]
    health = line_parts[1]
    attack = line_parts[2]
    defense = line_parts[3]
    enemy_dict = {
        'name':name,
        'health':health,
        'attack':attack,
        'defense':defense,
        }
    enemies.append(enemy_dict)
file.close()

for enemy in enemies:
  print(f"Name: {enemy['name']}, hp: {enemy['health']}, atk/def:{enemy['attack']}/{enemy['defense']}")
