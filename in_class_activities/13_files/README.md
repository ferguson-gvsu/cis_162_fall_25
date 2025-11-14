# Option A

`game.py` holds a working game where you must click the target 5 times. 
Your score is how long it takes you to click all 5 (lower score is better). 

We want to track your highscore _across_ different plays of the game. 
A file, `highscore.txt` is provided. 

Modify `game.py` to load the highscore from `highscore.txt` AND update `highscore.txt` if the player gets a new highscore. 

Bonus task: Track the top 3 highscores instead!

# Option B

We are tracking keycard accesses into the building. 
The file, `keycard_log.txt` provides like so:
```
id, action, line_num
```
Where `id` is the keycard id, `action` is either `enter` or `exit` and `line_num` just tracks what line we're on. 

We have a problem! Someone's keycard has been duplicated. 
Can you write a script to parse the file and figure out which keycard was duped?
