#move files into corresponding folder depending on file type
#make a list of common file extensions
#lowercases everything for streamlining
#moves all files in parent folder to corresponding sub folder if file type matches a listed extension
#forced overwrite if file already in destination directory
#TO ADD: functionality to create folders, user input parent folder, prompt user to overwrite if file already exists
import os, shutil

images = ['tif', 'tiff', 'gif', 'png', 'jpg', 'jpeg', 'raw']
audio = ['mp3', 'flac', 'wav','wma']
video = ['mp4', 'mov', 'wmv', 'flv', 'avi']
text = ['doc', 'docx', 'pdf', 'txt', 'odt']
programs = ['exe']
file_types = {'images':images, 'audio': audio, 'video': video, 'text':text}

os.chdir('testfolder')
cwd = os.getcwd()
files = os.listdir('...testfolder')
fileNames = [x.lower() for x in files]

print(f'Files in test folder: {fileNames}')

#uses dictionary where each key is the folder type, values are a list of filename extensions for that type
for file_type in file_types.keys():
	for extensions in file_types[file_type]:
		for name in fileNames:
			if name.endswith(extensions):
				print(f'Moving \'{name}\' to {file_type} folder')
				shutil.move(os.path.join(cwd,name),os.path.join(cwd,file_type,name))


			



