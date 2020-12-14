#!/usr/bin/env python3
#lists py files in myscripts folder, checks to see if corresponding bat files exist for python files in PATH folder and creates them if necessary

import os

os.chdir('C:\\Users\\jm\\AppData\\Local\\Programs\\Python\\Python39\\Scripts')
files = os.listdir('C:\\Users\\jm\\Desktop\\projects\\myscripts')
fileNames = [file.split('.') for file in files]
target= os.listdir('C:\\Users\\jm\\AppData\\Local\\Programs\\Python\\Python39\\Scripts')

print(f'Files in project folder: {files}')



for name in fileNames:
	if name[1]=='py':
		#print(f'{name} is a python file')
		batName = name[0]+".bat"
		if not os.path.exists(batName):
			dog= 'dog'
			print(f'{batName} does NOT exist, creating bat')
			newBat = open(batName,'w')
			newBat.write(f'@py.exe C:\\Users\\jm\\Desktop\\projects\\myscripts\\{name[0]}.py %* \n@pause')
			newBat.close()






