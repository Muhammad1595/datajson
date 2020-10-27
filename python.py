import discord
from discord.ext import commands
import os
import random
import json
import requests
from os import getcwd

url = "https://github.com/someguy/brilliant/blob/master/somefile.txt"
directory = getcwd()
filename = directory + 'somefile.txt'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)
