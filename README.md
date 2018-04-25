# Make sure you change the "www.example.com" to "10.101.10.47" so your git commands work 

### Synopsis

This script will login to the INGRESSIVE shared Dropbox account and then download all files that are under the ```photoscript``` folder.  The script will also mimic the directory structure under the ```photoscript``` folder to the machine running the script.  
### Use Case

If you decide you want to share photos from an event, you would create a folder on the DropBox account under ```photoscript```.  Then upload your photos to that folder.  The next time the photoscript.py script runs, it will create the new directory and then download those files into that directory to be displayed on the INGRESSIVE-TV.  