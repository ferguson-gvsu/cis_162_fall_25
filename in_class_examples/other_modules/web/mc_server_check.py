import urllib.request
import json

try:
  #with open('secret_ip.txt', 'r') as fp:
  with open('popular_ip.txt', 'r') as fp:
    ip = fp.readline().strip()
except:
  print('Error reading ip file! Stopping!')
  exit(1)

full_address = f'https://api.mcsrvstat.us/3/{ip}'
response = urllib.request.urlopen(full_address)
response_bytes = response.read()
response_str = response_bytes.decode()

response_json = json.loads(response_str)
is_online = response_json['online']
print(f'Is the server online? {is_online}')
if is_online:
  cur_players = int(response_json['players']["online"])
  print(f"Current players online: {cur_players}")
