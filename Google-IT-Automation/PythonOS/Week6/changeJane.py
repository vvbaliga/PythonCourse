#!/usr/bin/env python3

import sys
import shutil
import subprocess

#/home/student-00-e1e7cd0ee1a8/data

files =$(grep " jane " ../data/list.txt | cut - d ' ' - f 3)

#os.rename('/home/student-00-e1e7cd0ee1a8/data/jane', '/home/student-00-e1e7cd0ee1a8/data/joe')

