is_inside = {}

file = open('keycard_log_difficult.txt', 'r')
for line in file:
    line = line.rstrip()
    line_parts = line.split()
    id = line_parts[0]
    action = line_parts[1]
    line_num = line_parts[2]
    if id not in is_inside:
        is_inside[id] = False
    if action == 'enter':
        if is_inside[id] == True:
            print(f'Duplicate detected! id: {id}, line_num: {line_num}')
        is_inside[id] = True
    elif action == 'exit':
        is_inside[id] = False
