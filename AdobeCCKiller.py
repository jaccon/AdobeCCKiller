import os
import json

with open('db.json') as json_file:
    data = json.load(json_file)
    for p in data['paths']:
        print('File: ' + p['path'])

        file = p['path'];
        
        if p['type'] == "file":
            cmd = "rm -rf"

        if p['type'] == "pid":
            cmd = "launchctl remove"

        execute = cmd + " " +file;
        print execute;
        os.system(execute)

        print('')