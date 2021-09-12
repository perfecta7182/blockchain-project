import json
import os
files = []
base_path = 'C:/Users/77079/Desktop/pyblock/flask/json11'
for i in os.listdir(base_path):
    if i.endswith('.json'):
        full_path = '%s/%s' % (base_path, i)
        files.append(open(full_path, 'r', encoding='utf-8').read())

    for single_file in files:
        print(single_file)








