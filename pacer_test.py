import requests
import json
import hashlib# client_code, client_secret from App.  Code captured from URL.
clientid = 'pacer_6cb249f1a99d462a99af70e48a72611a'
clientsecret = '8d75412e5b6e45908b2570d4e13f8574'
codefromurl = '8d4c093ca4299ba89dbfd2f7e6ac98c4c5ca4c159571' # This is valid only once.# Generate Encoded Signature
client_secret_oauth = clientsecret + "pacer_oauth"
print(client_secret_oauth)
appSecretHash = hashlib.md5(client_secret_oauth.encode('utf-8')).hexdigest()
print(appSecretHash)
apphash_client_id = appSecretHash + clientid
print(apphash_client_id)
encodedSignature = hashlib.md5(apphash_client_id.encode('utf-8')).hexdigest()
print(encodedSignature)# Get Access Token
url = 'http://openapi.mypacer.com/oauth2/access_token'
headers = {'Authorization': encodedSignature, 
           'content-type': 'application/json'}
body = {
    "client_id": clientid,
    "code": codefromurl,
    "grant_type": "authorization_code"
    }
r = requests.post(url, data=json.dumps(body), headers=headers)
json_data = json.loads(r.text)
print(json.dumps(json_data, indent=4, sort_keys=True))
access_token = json_data['data']['access_token']
refresh_token = json_data['data']['refresh_token']
user_id = json_data['data']['user_id']
print("Access token is: ", access_token)
print("Refresh token is: ", refresh_token)
print("User ID is: ", user_id)


authSign = "Bearer " + access_token
headers = {"Authorization": authSign,
          'content-type': 'application/json'}
url = 'http://openapi.mypacer.com/users/' + user_id
r = requests.get(url, headers=headers)
print(r.text)

authSign = "Bearer " + access_token
headers = {"Authorization": authSign,
          'content-type': 'application/json'}
url = 'http://openapi.mypacer.com/users/' + user_id + '/activities/daily.json?start_date=2021-07-01&end_date=2021-07-02&accept_manual_input=true'
print(url)
r = requests.get(url, headers=headers)
json_data = json.loads(r.text)
print(json.dumps(json_data, indent=4, sort_keys=True))


