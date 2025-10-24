mascots = {}
mascots['gvsu'] = 'lakers'
mascots['msu'] = 'spartans'
mascots['ferris'] = 'bulldogs'

print(mascots)
mascots.pop('ferris')
#del mascots['ferris']
print(mascots)

print('gvsu' in mascots)
print('lakers' == mascots['gvsu'])

print(mascots)
if 'gvsu' not in mascots:
    mascots['gvsu'] = 'LAKERS'
print(mascots)

print(len(mascots))

for key in mascots:
    print(key)
    print(mascots[key])

print(mascots.items())
for k,v in mascots.items():
    print(f"Key:{k}, Value:{v}")

print(mascots.keys())