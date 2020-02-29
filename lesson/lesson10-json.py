import json 

# f = open("sample.json", "r")

# data = json.load(f)

# print(data)

# f.close()

with open("sample.json", "w") as f:
  data = json.dumps({"北海道":100,"熊本":80,"石川":100,"長野":90})
  print(data)
