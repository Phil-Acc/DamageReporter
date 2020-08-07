import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
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
          "Garbage\nBag": 40,
          "Card-\nboard": 23
        },
      "url1": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture2.png",
      "url2": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture1.png",
      "url3": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture0.png",
      "url4": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps2.png",
      "url5": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps1.png",
      "url6": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps0.png",
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
          "Garbage\nBag": 40,
          "Card-\nboard": 23
        },
      "url1": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture3.png",
      "url2": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture2.png",
      "url3": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/picture1.png",
      "url4": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps3.png",
      "url5": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps2.png",
      "url6": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/maps1.png",
      "bardiagram": "https://raw.githubusercontent.com/Phil-Acc/DamageReporter/master/bardiagram.png"
    }  
    
with open('data.json', 'w') as outfile:
    json.dump(jsondata, outfile)
    
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#2a2a2a'
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7.61,3))
fig.patch.set_facecolor('#2a2a2a')
ax.bar(list(jsondata["tickets_by_cat"].keys()), list(jsondata["tickets_by_cat"].values()))
ax.set_ylabel("Active Cases")
ax.set_facecolor('#2a2a2a')
plt.tight_layout()
plt.savefig("bardiagram.png", dpi=300, facecolor='#2a2a2a')

'''
steps = 8
total = [0]
active = [0]
solved = [0]
for i in range(steps):
    solved.append(solved[-1]+numpy.max([int(numpy.random.normal(450/steps, 30)),0]))
    active.append(active[-1]+int(numpy.random.normal(180/steps, 50)))
    total.append(solved[-1]+active[-1])


plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#2a2a2a'
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7.61,3))
fig.patch.set_facecolor('#2a2a2a')
ax.plot(total, label="Total Cases")
ax.plot(active, label="Active Cases")
ax.plot(solved, label="Solved Cases")
ax.set_ylabel("Cases")
ax.set_xlabel("Time (weeks)")
ax.set_facecolor('#2a2a2a')
plt.tight_layout()
plt.legend(facecolor='#2a2a2a')
plt.savefig("timetrace.png", dpi=300, facecolor='#2a2a2a')
plt.show()
'''