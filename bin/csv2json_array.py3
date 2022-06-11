#!/usr/bin/env python3

import csv
import json
import sys

reader = csv.reader(sys.stdin)
data=[]
for row in reader:
	data.append(row)

sys.stdout.write(json.dumps(
	data,
	skipkeys=True,
	ensure_ascii=False,
	check_circular=False,
	allow_nan=True,
	cls=None,
	indent=None,
	separators=(',', ':'),
	default=None,
	sort_keys=False))
