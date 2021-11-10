import time
from datetime import date, datetime, timedelta

def gettime(dt):
    y, m, d = dt.split('-')
    return {'year': int(y), 'month': int(m), 'day': int(d)}

with open('input.csv') as f:
    lst =[]
    for line, val in enumerate(f.readlines()):
        if line == 0:
            lst.append(val)
        else:
            id, start, end = val.split(';')
            print(id)
            print(len(start.strip()))
            print(len(end.strip()))
            if start.strip() or start.strip():
                continue
            start = date(**(gettime(start)))
            end = date(**(gettime(end)))
            while start <= end:
                lst.append(';'.join([id, str(start), '\n']))
                start = start + timedelta(1)
    
    with open("output.csv", "w") as outfile: 
        outfile.writelines(lst)





