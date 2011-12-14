#!/usr/bin/env python

import re
import sys


for line in sys.stdin:
   val = line.strip()
   a = val.split('\t');
   topicid = a[0];
   print "%s\t%s" % (topicid, 1)


