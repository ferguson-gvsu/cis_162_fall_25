import copy

class MazeActivity:
  def __init__(self):
    self.maze = [
    '#############',
    '......#.....#',
    '#.###.###.#.#',
    '#.........#.#',
    '###.#######.#',
    '#.......#...#',
    '#.###.#.###.#',
    '#...#.#.....#',
    '###.#.###.#.#',
    '#.#.....#.#.#',
    '#.#######.#.#',
    '#.........#..',
    '#############'
    ]
    self.pos = [1,0]
    self.goal = [11, 12]
    self.facing = 1 # N, E, S, W
    self.moves = 0
    self.turns = 0
    self.move_calls = 0
    self.always_draw = True

  def get_symbol(self):
    symbol_list = '^>v<'
    if self.facing >= len(symbol_list):
      print('Error!')
      quit()
    return symbol_list[self.facing]

  def draw(self):
    for line_idx in range(len(self.maze)):
      if line_idx == self.pos[0]:
        col = self.pos[1]
        print(self.maze[line_idx][:col] + self.get_symbol() + self.maze[line_idx][col + 1:])
      else:
        print(self.maze[line_idx])
    print()

  def move(self, steps = 1):
    self.move_calls += 1
    for step_idx in range(steps):
      self.moves += 1
      new_pos = [self.pos[0], self.pos[1]]
      if self.facing == 0:
        new_pos[0] -= 1
      elif self.facing == 1:
        new_pos[1] += 1
      elif self.facing == 2:
        new_pos[0] += 1
      elif self.facing == 3:
        new_pos[1] -= 1
      if self.maze[new_pos[0]][new_pos[1]] == '#':
        print('Hit a wall! Stopping!')
        break
      else:
        self.pos = new_pos
    if self.always_draw:
      self.draw()
    if self.pos[0] == self.goal[0] and self.pos[1] == self.goal[1]:
      print('=== FINISHED ===')
      print(f'Moves: {self.moves}')
      print(f'Turns: {self.turns}')
      print(f'Function calls (move): {self.move_calls}')

  def turn(self, dir):
    self.turns += 1
    dir = dir.lower()
    if dir == 'r':
      self.facing += 1
    if dir == 'l':
      self.facing -= 1
    self.facing = (self.facing + 4) % 4
    if self.always_draw:
      self.draw()


activity = MazeActivity()

def move(steps = 1):
  global activity
  activity.move(steps)

def turn():
  global activity
  activity.turn()

def start():
  global activity
  activity.draw()
