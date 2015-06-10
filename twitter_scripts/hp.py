import requests
import json

key = ""
with open('api_key.txt','r') as f:
    apikey = f.readline().strip()


# General routine for calling IDOL on Demand services
def postrequests(callingurl,function,data={},files={}):
  
  # Put API Key into URL
  data["apikey"]=apikey

  # Insert particular IOD service into URL
  callurl=callingurl.format(function)

  # Call IoD and return results
  success=True
  try:
      r=requests.post(callurl,data=data,files=files,timeout=5)
      returned_status_code=r.status_code
      returned_json=r.json() 
      if r.status_code != 200:
          success=False
   
  # Trap timeouts - fairly common
  except requests.exceptions.Timeout as e:
      success=False
      returned_status_code=-1
      returned_json='Timeout'
   
  return success, returned_status_code, returned_json

def hp_sentiment(text):
  url="http://api.idolondemand.com/1/api/sync/{}/v1"
  success, status_code, results = postrequests(url,'analyzesentiment',{'text':text})

  if success:
    SentimentResult_string=json.dumps(results)
    aggregatelist=results["aggregate"]
    return 2**aggregatelist["score"]
  else:
    return 1