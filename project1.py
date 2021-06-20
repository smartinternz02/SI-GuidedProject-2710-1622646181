import wiotp.sdk.device
import time
import random
import requests

myConfig = { 
    "identity": {
        "orgId": "r6dhnj",
        "typeId": "projectiot",
        "deviceId":"24680"
    },
    "auth": {
        "token": "987654321"
    }
}
location="16.999230,79.962770"
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print()
    if(m== "maxh" or m=="maxw"):
        print("bin is filled completely..the location of bin to collect waste in bin is",location)
        

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization":"o8nkJ74Uvl9B1muQwGehCKOgXzZWSRF0Y5pTLqEtxdiMPyH2VfmFh92jrnykNYZe4RAftO6c3vuaoXwI","message":"bin is filled go and collect it from the location","language":"english","route":"q","numbers":"9347844644"}

        headers = {
                    'cache-control': "no-cache"
                  }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
                
    print()

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    height=random.randint(0,50)
    weight=random.randint(0,20)
    myData={'d':{'name':'projectiot','height':height, 'weight':weight,"location":location}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
