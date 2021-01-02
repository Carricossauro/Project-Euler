#!/usr/bin/python

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

temp = ini["added"]
ini["added"] = n
with open(pathDirectory + "/numberFiles.json", 'w') as jsonFile:
	json.dump(ini, jsonFile)

os.system("git add .")
os.system("git commit -m \"Problems " + str(temp+1) + "-" + str(n) + "\"")
os.system("git push origin master")

