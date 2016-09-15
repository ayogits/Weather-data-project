import json
from pandas.io.json import json_normalize

weather_file = 'weather_json_sample.json'
with open(weather_file) as fhand:
    data = json.load(fhand)
path = data['SiteRep']['DV']['Location']['Period'] # This is the path to the dates, times and weather info in a list format. Each element in list is a different day.
print path
result = json_normalize(path, 'Rep', ['value'])
print result

#day = path[0]['Rep'][0]['$'] # This gives weather info on the whole day
#print day