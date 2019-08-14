#! /usr/bin/env python


import yaml
from pprint import pprint


readyaml = open("yaml_example.yaml").read()



yaml_py = yaml.load(readyaml,yaml.SafeLoader)
interface_name = yaml_py["ietf-interfaces:interface"]["name"]

#pprint(interface_name)

address = yaml_py["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"]

for addr in address:
	pprint(addr["ip"])

#yaml.dump(yaml_py)

