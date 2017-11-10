import json

with open('timeline.json') as f:
    data = json.loads(f.read())

with open('readable.json','w') as f:
    f.write(json.dumps(data,indent=2,sort_keys=True))
