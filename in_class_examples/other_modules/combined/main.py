from tkinter import *
from tkinter import ttk
from advanced_web_request import fetch_griffons_games
import pyttsx3

root = Tk()
root.title("hockey?")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

game_data = 'No game data'

tts_engine = pyttsx3.init()

def fetch_data(*args):
    try:
      games = fetch_griffons_games()
      cur_row = 4
      for game in games:
        ttk.Label(mainframe, text=str(game['date'])).grid(column=1, row=cur_row)
        ttk.Label(mainframe, text=game['team']).grid(column=2, row=cur_row)
        ttk.Label(mainframe, text=game['result']).grid(column=3, row=cur_row)
        cur_row += 1
      global game_data
      game_data = games
        
    except ValueError:
        pass

def narrate(*args):
  global game_data
  if isinstance(game_data, str):
    tts_engine.say(game_data)
    tts_engine.runAndWait()
  else:
    for game in game_data:
      s = f"The Griffons played the {game['team']} in {game['date']}, result was: {game['result']}"
      tts_engine.say(s)
      tts_engine.runAndWait()


ttk.Label(mainframe, text="Click the buttons!").grid(column=1, row=1, sticky=W)

ttk.Button(mainframe, text="Fetch data", command=fetch_data).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Narrate", command=narrate).grid(column=3, row=3, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", fetch_data)

root.mainloop()
