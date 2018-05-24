#!/usr/local/bin/python3

import json

config_file = "pyfunc.json"
funcs = json.loads(open(config_file).read())

for key, value in funcs.items():
    print("Function ", key)
    exec(value["body"])

h = 2335.8
for Psta in (740, 750, 760,770):
    print("psl:", Psta, h, psl(Psta, h))

print("\n")
for t in (-40, -20, 0, 10, 20, 30, 40):
    for rh in (1, 25, 50, 75, 99):
        print("dewpoint:", t, rh, dewpoint(t=t, rh=rh))
    print("\n")
