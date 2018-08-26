#! /usr/bin/env python


import xmltodict
from pprint import pprint


readxml = open("xml_example.xml").read()

pprint(readxml)

xml_dict = xmltodict.parse(readxml)
interface_name = xml_dict["interface"]["name"]

pprint(interface_name)

xml_dict = xmltodict.unparse(readxml)