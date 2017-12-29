import simplejson as json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame,Series
import pandas as pd
import numpy as np


path = 'E:\\Project\\RecommendationForLib\\PythonForDataAnalysis\\usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
#print records[0]
#print records[0]['tz']
time_zones=[rec['tz'] for rec in records if 'tz' in rec]
#print time_zones[:10]
def get_couts(sequence):
    counts=defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts
counts=get_couts(time_zones)
#print counts['America/New_York']
#print 'Time zones %s ' % len(time_zones)
def top_counts(count_dict,n=5):
    value_key_pairs=[(count,tz)for tz,count in count_dict.items() ]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
#print top_counts(counts)

counts=Counter(time_zones)
#print counts.most_common(5)

frame=DataFrame(records)
#print frame['tz'][:5]
tz_counts=frame['tz'].value_counts()
#print tz_counts[:5]
clean_tz=frame['tz'].__finalize__('Missing')
clean_tz[clean_tz=='']='Unknown'
tz_counts=clean_tz.value_counts()
print tz_counts[:10]

tz_counts[:10].plot(kind='barh',rot=0)