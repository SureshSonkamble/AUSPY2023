import requests
import json
try:
    url="http://online.pranaliinfotech.com/pigateway/api/UserLogin/Login?un=9922111000&pw=12345&apk_type=1"
    res=requests.get(url)
    data=res.json()
    for i in range(5):
        print(data['parentRow'][i]['SHOP_NAME'])
except:
    print("Error...")
