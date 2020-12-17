#!/usr/bin/env python3
#script to check if the python path folder has an associated bin file for the filename provided by user, creates one if necessary

#currently checks files in current working directory

import os,sys

if len(sys.argv)<2:
    print('Usage: python mkbat.py [filename.py]')
    sys.exit()

path_dir = #where your scripts are
file_name = sys.argv[1]
bat_name = file_name.split('.')[0] + '.bat'
bat_path = os.path.join(path_dir,bat_name)
py_path = os.path.realpath(file_name)

ans = ''
print(bat_path)
if not os.path.exists(bat_path):
	ans = input(f'{bat_name} does not exist. Create {bat_name}? Y/N: ')
else:
	print(f'{bat_name} already exists')
	sys.exit()



if ans.lower() == 'y':
	new_bat = open(bat_path,'w')
	new_bat.write(f'@py.exe {py_path} %* \n@pause')
	new_bat.close()
	print(f'{bat_name} created in path file')
	sys.exit()




