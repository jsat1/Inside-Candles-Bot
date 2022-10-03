import requests
import json
import os

url = "https://api.twitter.com/2/tweets"

consumer_key = os.environ['api_key']
access_token = os.environ['access_token']
headers = {
  'Authorization': f'OAuth oauth_consumer_key={consumer_key},oauth_token={access_token},oauth_signature_method="HMAC-SHA1",oauth_timestamp="1664722905",oauth_nonce="pls6CnNDIvr",oauth_version="1.0",oauth_signature="QAPeTPhfT5mE1yu2bZ6Gh%2BzTDIQ%3D"',
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A164748160617485457; guest_id_ads=v1%3A164748160617485457; guest_id_marketing=v1%3A164748160617485457; personalization_id="v1_PFHqkQhmwp141oUu4hPm9w=="'
}

def sendTweet(tweetText, mediaID):
    payload = json.dumps({
        "text": tweetText, 
        "media": {
            "media_ids": [mediaID]
        }
    })

    response = requests.request("POST", url, headers=headers, data=payload)
