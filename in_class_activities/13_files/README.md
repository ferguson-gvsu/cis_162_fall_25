# Option A

`game.py` holds a working game where you must click the target 5 times. 
Your score is how long it takes you to click all 5 (lower score is better). 

We want to track your highscore _across_ different plays of the game. 
A file, `highscore.txt` is provided. 

Tasks: 
1. Modify `game.py` to load the highscore from `highscore.txt`
2. Update `highscore.txt` if the player gets a new highscore. 

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

Tasks:
1. Figure out the logic of how we'd detect a duplicate keycard
2. Check with me to verify your logic is sound
3. Write code to load in `keycard_log.txt` and read it line-by-line
4. Modify your code to detect the duplicate keycard

Note:
`keycard_log_simple.txt` is provided for an easier example to work through. 
`keycard_log_difficult.txt` is a challenging instance to test your code on.
