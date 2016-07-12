import requests as r
import json
import datetime

class MicrosoftHealth:
  token = ''
  def __init__(self, token):
    self.token = 'Bearer ' + token

  def getProfile(self):
    request = r.get('https://api.microsofthealth.net/v1/me/Profile?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn

  def getSteps(self):
    request = r.get('https://api.microsofthealth.net/v1/me/Summaries/daily?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn

  def getActivities(self):
    request = r.get('https://api.microsofthealth.net/v1/me/Activities?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn
