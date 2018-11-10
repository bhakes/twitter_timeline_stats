# -*- coding: utf-8 -*-
# This is an golf course img scrapper that goes to the web and
# gets sweet images of golf course from around the world

import urllib2
import simplejson as json
import io
import cStringIO

searchTerm = "pine-valley-golf-club"
searchID = 'XXXXX'
api_key = 'XXXXX'
startIndex = 0
searchUrl = "https://www.googleapis.com/customsearch/v1?key=" + api_key + "&q=" + searchTerm + "&imgsz=medium"+ "&searchType=image" + "&cx=" + searchID
contents = urllib2.urlopen(searchUrl).read()
parsed = json.loads(contents)
with io.open('data.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False))
