import os
import zipfile
import shutil
import json

def convert(tar_file):
    print(tar_file)
    temp = './temp'
    zipfile.ZipFile(tar_file).extractall(temp)
    logs = []
    for subdir, _, files in os.walk(temp):
        for filename in files:
            if filename.endswith('.log'):
                name = subdir[-10:]
                filepath = subdir + os.sep + filename
                with open(filepath) as f:
                    for line in f.readlines():
                        logs.append('{"file":"' + name + '",' + line[1:])
    shutil.rmtree(temp)

    with open("result.json", "w") as outfile: 
        json.dump(json.loads('[' + ','.join(logs) + ']'), outfile, indent=4)

if __name__ == '__main__':
    for _, _, files in os.walk('./'):
        for filename in files:
            if filename.endswith('.tar'):
                convert(filename)
    

