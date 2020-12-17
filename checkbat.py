#!/usr/bin/env python3
#lists py files in myscripts folder, checks to see if corresponding bat files exist for python files in PATH folder and creates them if necessary

import os

os.chdir({path folder})
files = os.listdir({script folder})
#NEED TO CHANGE FILE SPLIT TO ACCOUNT FOR MULTIPLE DOTS USE REGEX
fileNames = [file.split('.') for file in files]
target= os.listdir({stuff})

print(f'Files in project folder: {files}')



for name in fileNames:
	if name[1]=='py':
		#print(f'{name} is a python file')
		batName = name[0]+".bat"
		if not os.path.exists(batName):
			dog= 'dog'
			print(f'{batName} does NOT exist, creating bat')
			newBat = open(batName,'w')
			newBat.write(f'@py.exe {destinationfolder}{name[0]}.py %* \n@pause')
			newBat.close()






