#! /usr/bin/env python


import yaml
from pprint import pprint


readyaml = open("yaml_example.yaml").read()

#pprint(readjson)

yaml_py = yaml.load(readyaml)
interface_name = yaml_py["ietf-interfaces:interface"]["name"]

pprint(interface_name)

yaml.dump(yaml_py)

