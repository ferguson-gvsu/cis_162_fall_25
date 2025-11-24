import urllib.request

response = urllib.request.urlopen('http://gvsu.edu')
raw_html = response.read()
html_str = raw_html.decode()
print(html_str)
