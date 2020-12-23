#!/bin/python3

import os
import json
from os import path


pathDirectory = "/home/carricossauro/Documents/project-euler"

i = 1
while path.exists(pathDirectory + "/p" + str(i) + ".py"):
	i+=1
n = i-1

with open(pathDirectory + "/numberFiles.json") as jsonFile:
	ini = json.load(jsonFile)

os.system("git add .")
os.system("git commit -m \"Problems " + str(n) + "-" + str(ini["added"]) + "\"")
os.system("git push origin master")

ini["added"] = n
with open(pathDirectory + "/numberFiles.json") as jsonFile:
	json.dump(ini, jsonfile)