#! /usr/bin/env python


import json
from pprint import pprint


readjson = open("json_example.json").read()

#pprint(readjson)

json_py = json.loads(readjson)
interface_name = json_py["ietf-interfaces:interface"]["name"]

pprint(interface_name)

json.dumps(json_py)