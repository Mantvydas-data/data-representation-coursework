import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

def getCSOdata():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("CSO.json", "w") as fp:
        print(json.dumps(getCSOdata()), file=fp)