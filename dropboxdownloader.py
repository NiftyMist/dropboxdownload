import dropbox
import os

# API Token
dbx = dropbox.Dropbox('') # add Dropbox API token here

# List for storing Folder and Photo names
folders = []
photos = []

# Store names of Folders
for entry in  dbx.files_list_folder('/ingest').entries:
		if "." not in entry.name:
			folders.append(entry.name)
		#dbx.files_download_to_file(entry.name, "/ingest/"+entry.name, rev=None)
		#print(dbx.files_download(entry))

# Create local directory for download
for i in folders:
	if not os.path.exists(i):
		os.makedirs(i)

# Downlaod everthing within each folder
num = 0
count = 0
for i in folders:
	foldername = folders[num]
	dir = '/ingest/'+foldername
	
	for entry in dbx.files_list_folder(dir).entries:
		photos.append(entry.name)
	for i in photos:
		destination = folders[num]+"/"+photos[count]
		target = "/ingest/"+folders[num]+"/"+photos[count]
		#print(destination+"\n"+"\t"+target)
		dbx.files_download_to_file(destination, target, rev=None)
		count = count+1
	num = num+1
