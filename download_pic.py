import urllib
import simplejson as json
import io
import cStringIO
import time
import os
from pprint import pprint

resource = 'https://media.golfdigest.com/photos/585054bdba03cefc46ca21c1/master/w_768/2017-01-Pine-Valley-GC-hole-11.jpg'
urllib.urlretrieve(resource, './test1.jpg')

with open('data.json') as f:
    data = json.load(f)

smallData = data['items']

counter = 1

for i in smallData:
    resource = i['link']
    filepath = './images/golf'+ str(counter) + '.jpg'
    urllib.urlretrieve(resource, filepath)
    counter = counter + 1
