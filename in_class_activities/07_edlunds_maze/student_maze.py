# Feel free to change these parameters!

random_seed = 4 # 0 means to generate a new maze each time
hard_mode = False # Setting hard_mode to True adds some extra information to work with
harder_mode = False # Randomly generate the up and down cues, hard_mode must also be True
num_columns = 8 # Number of walkable columns
num_rows = 6 # Number of vertical tiles in each column

#######################################
# IGNORE EVERYTHING UNTIL NEXT BANNER #
######################################

import random

class MazeActivity:
  def __init__(self, seed=0, cols=6, rows=8):
    self.seed = seed
    self.cols = cols
    self.rows = rows
    self.width_tiles = self.cols * 2 + 1
    self.height_tiles = self.rows + 2
    self.maze = []
    self.connector_y_coords = []
    self.generate_maze()
    self.pos = [1,1]
    self.num_moves = 0
    
  def generate_maze(self):
    self.up_char = '^'
    self.down_char = 'v'
    if harder_mode:
      self.up_char = random.choice('abcdefghijklmnopqrstuvwxyz')
      self.down_char = random.choice('abcdefghijklmnopqrstuvwxyz')
      while self.down_char == self.up_char:
        self.down_char = random.choice('abcdefghijklmnopqrstuvwxyz')
    if self.seed != 0:
      random.seed(self.seed)
    self.maze = []
    # Top border
    for x in range(self.width_tiles):
      self.maze.append('#')
    # Create the basic columns
    for row in range(self.rows):
      for col in range(self.width_tiles):
        if col & 1 == 1: 
          self.maze.append(' ')
        else:
          self.maze.append('#')
    # Bottom border
    for x in range(self.width_tiles):
      self.maze.append('#')
    # Add the connectors
    for col in range(self.cols-1):
      gap_y = 1 + random.randint(0, self.rows-1)
      if col != 0 and hard_mode:
        prev_y = self.connector_y_coords[-1]
        while gap_y == prev_y:
          gap_y = 1 + random.randint(0, self.rows-1)
        prev_idx = prev_y * self.width_tiles + ((col-1) * 2 + 2)
        char = self.down_char
        if prev_y > gap_y:
          char = self.up_char
        self.maze[prev_idx] = char
      self.connector_y_coords.append(gap_y)
      index = gap_y * self.width_tiles + (col * 2 + 2)
      self.maze[index] = ' '

  def draw(self):
    for row in range(self.height_tiles):
      line = ''
      for col in range(self.width_tiles):
        char = self.maze[row * self.width_tiles + col]
        if col == self.pos[0] and row == self.pos[1]:
          char = '@'
        line += char
      print(line)
    print('') # Add an extra blank line

  def sense(self, new_pos):
    return self.maze[new_pos[1] * self.width_tiles + new_pos[0]]

  def check_move(self, new_pos):
    return self.sense(new_pos) != '#'

  def check_finished(self):
    return self.pos[0] == self.width_tiles - 2

  def finish(self):
    print(f"Congrats! You finished the maze in {self.num_moves} moves!")

  def move(self, new_pos):
    self.num_moves += 1
    if self.check_move(new_pos):
      self.pos = new_pos
      if self.check_finished():
        self.finish()
    else:
      print('Hit a wall :(')

  def move_up(self):
    self.move([self.pos[0], self.pos[1] - 1])
  
  def move_down(self):
    self.move([self.pos[0], self.pos[1] + 1])
    
  def move_left(self):
    self.move([self.pos[0] - 1, self.pos[1]])
    
  def move_right(self):
    self.move([self.pos[0] + 1, self.pos[1]])
    
  def sense_up(self):
    return self.sense([self.pos[0], self.pos[1] - 1])
  
  def sense_down(self):
    return self.sense([self.pos[0], self.pos[1] + 1])
  
  def sense_left(self):
    return self.sense([self.pos[0] - 1, self.pos[1]])
  
  def sense_right(self):
    return self.sense([self.pos[0] + 1, self.pos[1]])
  
  def sense_current(self):
    return self.sense(self.pos)

activity = MazeActivity(random_seed, num_columns, num_rows)

def move_up():
  global activity
  activity.move_up()

def move_down():
  global activity
  activity.move_down()

def move_left():
  global activity
  activity.move_left()

def move_right():
  global activity
  activity.move_right()

def sense_up():
  global activity
  return activity.sense_up()

def sense_down():
  global activity
  return activity.sense_down()

def sense_left():
  global activity
  return activity.sense_left()

def sense_right():
  global activity
  return activity.sense_right()

def sense_current():
  global activity
  return activity.sense_current()

def draw():
  global activity
  activity.draw()

def check_finished():
  global activity
  return activity.check_finished()

################################
# IGNORE EVERYTHING ABOVE HERE #
################################

# Your task is to write code that will solve ANY maze that we generate. 
# You can write any code you need to below these comments.
# A brief description of each function you have access to is given below.

# Functions: 
# draw(): print the current state of the board. **without calling this you won't see anything!**
# move_up(), move_down(), move_right(), and move_left(): move you one tile each in the given direction
# sense_up(), sense_down(), sense_right(), sense_left(), and sense_current() will return the CHARACTER in that position, relative to the agent
#     When not in hard mode, the possible characters are " " (floor) and "#" wall
#     When in hard mode, you ALSO have "^" and "v", which indicate that the next hole is either above ("^") or below ("v") this one. 
#         If the next hole is directly across, you will receive a " " still.
# check_finished(): returns True if you have reached the right side of the maze, False otherwise


# Your code goes here!
# Right now it just draws the beginning state of the maze.
draw()


