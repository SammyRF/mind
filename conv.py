import json
import pandas
import os

excel_writer = pandas.ExcelWriter('./test.xls')
for subdir, dirs, files in os.walk(r'./'):
    for filename in files:
        if filename.endswith('.log'):
            filepath = subdir + os.sep + filename
            with open(filepath) as f:
                lines = f.readlines()
                data = [json.loads(line) for line in lines]
                cols = list(json.loads(lines[0]).keys())
                pandas.DataFrame(data, columns=cols).to_excel(excel_writer, sheet_name=subdir[-8:0])
excel_writer.save()


