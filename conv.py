import json
import pandas
import os
import zipfile
import sys
import shutil

def convert(tar_file):
    print(tar_file)
    temp = './temp'
    excel_file = '/data/' + tar_file[:-4] + '.xls'
    zipfile.ZipFile(tar_file).extractall(temp)
    excel_writer = pandas.ExcelWriter(excel_file)
    for subdir, _, files in os.walk(temp):
        for filename in files:
            if filename.endswith('.log'):
                filepath = subdir + os.sep + filename
                with open(filepath) as f:
                    lines = f.readlines()
                    data = [json.loads(line) for line in lines]
                    cols = list(json.loads(lines[0]).keys())
                    pandas.DataFrame(data, columns=cols).to_excel(excel_writer, sheet_name=subdir[-8:])
    excel_writer.save()
    shutil.rmtree(temp)

if __name__ == '__main__':
    for _, _, files in os.walk('./'):
        for filename in files:
            if filename.endswith('.tar'):
                convert(filename)

