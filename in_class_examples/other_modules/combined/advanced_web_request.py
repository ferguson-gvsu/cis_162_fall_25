from bs4 import BeautifulSoup
import urllib.request
import datetime

def fetch_griffons_games():
  response = urllib.request.urlopen('https://griffinshockey.com/schedule/results')
  #response = urllib.request.urlopen('http://gvsu.edu')
  raw_html = response.read()
  html_str = raw_html.decode()

  #soup = BeautifulSoup(html_str)
  soup = BeautifulSoup(html_str, 'lxml')
  games = soup.find_all('div', class_='c-game-listing--results')
  result_list = []
  for game in games:
    date_str = game.find_all('span', class_='o-timestamp')[0]['data-time']
    year,month,day = date_str[:10].split('-')
    date = datetime.date(int(year), int(month), int(day))
    team_div = game.find_all('div', class_='c-game-listing__team')[0]
    team_name = str(team_div.find_all('span')[1].string).strip()
    result = str(game.find_all('span', class_='c-game-listing__score')[0].string).strip()
    game_data = {}
    game_data['team'] = team_name
    game_data['date'] = date
    game_data['result'] = result
    result_list.append(game_data)
  return result_list

if __name__ == '__main__':
  games = fetch_griffons_games()
  for game in games:
    print(f"{game['date']} {game['team']}; {game['result']}")
