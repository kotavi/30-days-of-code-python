import json


my_file = open('logs.jsonl', 'r')
new_file = open('updated_logs.jsonl', 'w')

for line in my_file.readlines():
    try:
        line = json.loads(line)
    except:
        continue
    if "index" in line:
        continue
    if "coordinates" in line["geo"]:
        if line["geo"]["coordinates"]["lat"] > 36:
            new_file.write(json.dumps(line))

# new_file = open('updated_logs.jsonl', 'w')
# data = my_file.readlines()
# rep = ',"_type":"log"'
# for line in data:
#     if rep in line:
#         line = line.replace(',"_type":"log"', '')
#     new_file.write(line)
my_file.close()
new_file.close()