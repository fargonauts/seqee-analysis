import pandas
import datetime

from pprint import pprint
from collections import defaultdict

def read_date(date):
    #i.e. 2007September10PM030257
    if date.endswith('_2'):
        date = date[:-2]
    return datetime.datetime.strptime(date,'%Y%B%d%p%I%M%S')

def convert(data):
    longdata = defaultdict(list)
    for date, problems in data.items():
        for problem, section in problems.items():
            for k, v in section.items():
                longdata[k].append(v)
            longdata['problem'].append(problem)

            longdata['date'].append(read_date(date))
    return pandas.DataFrame(longdata)
