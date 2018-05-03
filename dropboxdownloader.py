import dropbox
import os
# API Token
dbx = dropbox.Dropbox('') # Add Dropboc Token String here
# List for storing Folder and Photo names
folders = []
photos = []
# Store names of Folders
for entry in  dbx.files_list_folder('/ingest').entries:
		if "." not in entry.name:
			folders.append(entry.name)
# Create local directory for download
for i in folders:
	if not os.path.exists(i):
		os.makedirs(i)
# Downlaod everthing within each folder
num = 0 # count for folders list
count = 0 # count for photos list
photo = 0 # counting the number of downloaded photos
cwd = os.getcwd() # Gets the current working directory
for i in folders:
	foldername = folders[num]
	# Store names of Photos within current Folder
	dir = '/ingest/'+foldername
	for entry in dbx.files_list_folder(dir).entries:
		photos.append(entry.name)
	# Determine which Photos to download by checking if the absolute path already exists locally
	for i in photos:
		destination = cwd+"/"+folders[num]+"/"+photos[count]
		target = "/ingest/"+folders[num]+"/"+photos[count]
		downloaded = os.path.exists(destination)
		if downloaded == True:
			count = count+1 # move on to next item in photos list
			continue
		elif downloaded == False:
			dbx.files_download_to_file(destination, target, rev=None)
			photo = photo+1 # adds 1 to the count of photos downloaded
			count = count+1 # move on to next item in photos list
	num = num+1 # move on to next item in folders list
print("Downloaded "+str(photo)+" New Photos")
