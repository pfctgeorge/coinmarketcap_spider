#!/usr/bin/env python

import json
r = open("./coins.json").read()
for img in json.loads(r):
    smallSrc = 'wget %s' % img['imgSrc']
    print(smallSrc)
