import numpy
import matplotlib.pyplot as plt
import json

timeframe = "new"

if timeframe=="old":
    jsondata = {
      "total_tickets": 173,
      "tickets_by_cat": 
        {
          "D00": 13,
          "D01": 19,
          "D10": 22,
          "D11": 1,
          "D20": 5,
          "D40": 28,
          "D43": 14,
          "D44": 8,
          "Garbage Bag": 40,
          "Cardboard": 23
        },
      "url1": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture2.png",
      "url2": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture1.png",
      "url3": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture0.png",
      "url4": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map2.png",
      "url5": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map1.png",
      "url6": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map0.png",
      "bardiagram": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/bardiagram.png"
    }

else:
    jsondata = {
      "total_tickets": 176,
      "tickets_by_cat": 
        {
          "D00": 13,
          "D01": 19,
          "D10": 23,
          "D11": 1,
          "D20": 6,
          "D40": 28,
          "D43": 15,
          "D44": 8,
          "Garbage Bag": 40,
          "Cardboard": 23
        },
      "url1": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture3.png",
      "url2": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture2.png",
      "url3": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture1.png",
      "url4": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map3.png",
      "url5": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map2.png",
      "url6": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/map1.png",
      "bardiagram": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/bardiagram.png"
    }  
    
with open('data.json', 'w') as outfile:
    json.dump(jsondata, outfile)
    
plt.barh(list(jsondata["tickets_by_cat"].keys()), list(jsondata["tickets_by_cat"].values()))
plt.xlabel("Active Cases")
plt.tight_layout()
plt.savefig("bardiagram.png", dpi=300)