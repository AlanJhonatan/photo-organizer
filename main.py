import os
import json
from os.path import isfile, join

files = []
dirs = []
_structure = {}

for (dirpath, dirnames, filenames) in os.walk('.'):
  #print(f'dirpath: {dirpath}, dirnames: {dirnames}, filenames: {filenames}')
  
  # add '/' at end of dirnames
  for idx, d in enumerate(dirnames):
    d += '/'
    dirnames[idx] = d
  if len(dirpath) != 1:
    dirpath = dirpath[2:]

  _structure[dirpath] = dirnames + filenames

with open('data.json', 'w+', encoding='utf-8') as f:
  json.dump(_structure, f, ensure_ascii=False, indent=4)
  f.close()