import requests
import json

response = requests.get("https://nrv-cloud.herokuapp.com/music")
data = response.json()
datas = data.get('data')
for info in datas:
	url = info.get('preview')
	r = requests.get(url, allow_redirects=True)
	open(u'{}.mp3'.format(info.get('artist')), 'wb').write(r.content)
