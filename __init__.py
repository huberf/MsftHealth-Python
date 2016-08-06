import requests as r
import json
import datetime
import time
import formatdate

class MicrosoftHealth:
  token = ''
  refreshToken = ''
  clientId = ''
  clientSecret = ''
  redirectUri = ''
  persistent = False
  lastToken = 0

  def __init__(self, token):
    self.token = 'Bearer ' + token

  def __init__(self, refreshToken, clientId, clientSecret, redirectUri):
    self.refreshToken = refreshToken
    self.clientId = clientId
    self.clientSecret = clientSecret
    self.redirectUri = redirectUri
    self.persistent = True

  def getToken(self):
    accessUrl ='https://login.live.com/oauth20_token.srf?client_id={client_id}&redirect_uri={redirect_uri}&client_secret={client_secret}&refresh_token={refresh_token}&grant_type=refresh_token'
    accessUrl = accessUrl.replace('{client_id}', self.clientId)
    accessUrl = accessUrl.replace('{redirect_uri}', self.redirectUri)
    accessUrl = accessUrl.replace('{client_secret}', self.clientSecret)
    accessUrl = accessUrl.replace('{refresh_token}', self.refreshToken)
    response = r.get(accessUrl)
    data = json.loads(response.text)
    return 'Bearer ' + data['access_token']

  def verifyToken(self):
    if(time.time() - self.lastToken > 3400):
      self.token = self.getToken()
      self.lastToken = time.time()

  def getRefreshToken(self, clientId, clientSecret, offlineCode):
    data = {'client_id': clientId,
        'redirect_uri': redirectUri,
        'client_secret': clientSecret,
        'code': offlineCode,
        'grant_type': 'authorization_code'}
    accessUrl = 'https://login.live.com/oauth20_token.srf'
    response = r.post(accessUrl, data=data, headers={'content-type':'application/x-www-form-urlencoded'})
    return response.text

  def getProfile(self):
    self.verifyToken()
    request = r.get('https://api.microsofthealth.net/v1/me/Profile?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn

  def getSummary(self):
    self.verifyToken()
    start = datetime.datetime.now()
    formatter = formatdate.FormatDate()
    endDate = formatter.format(start.year, start.month, start.day, start.hour, start.minute)
    #startDate = formatter.format(start.year, start.month - 1, start.day, start.hour, start.minute)
    startDate = formatter.format(2016, 1, 1, 0, 0)
    request = r.get('https://api.microsofthealth.net/v1/me/Summaries/hourly?startTime=' + startDate + '&endTime=' + endDate, headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn

  def getActivities(self):
    self.verifyToken()
    request = r.get('https://api.microsofthealth.net/v1/me/Activities?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn

  def getDevices(self):
    self.verifyToken()
    request = r.get('https://api.microsofthealth.net/v1/me/Devices?', headers={'Authorization': self.token})
    toReturn = json.loads(request.text)
    return toReturn
