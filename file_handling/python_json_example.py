import json

try:
    fh = open("demo.json", "r")
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(type(json_value["age"]))
finally:
    fh.close()