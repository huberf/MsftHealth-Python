import requests as r

request = r.get('https://api.microsofthealth.net/v1/me/Profile?', headers={'Authorization': token});

print request.text
