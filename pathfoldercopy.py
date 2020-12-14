#!/usr/bin/env python3
import os, shutil

os.chdir('C:\\Users\\jm\\Desktop\\projects\\myscripts')
currentFolder = os.listdir('C:\\Users\\jm\\Desktop\\projects\\myscripts')
target = 'C:\\Users\\jm\\AppData\\Local\\Programs\\Python\\Python39\\Scripts'
targetFolder = os.listdir(target)

for script in currentFolder:
	if script not in targetFolder:
		print(f'{script} is NOT in target, copying file...' )
		shutil.copy(script, target)


	

