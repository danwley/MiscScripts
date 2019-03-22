# THE FOLLOWING CODE DOES NOT PROTECT AGAINST FILENAMES THAT CANNOT BE LIST-SORTED
# Scripting this process to rename only around 10 files has clearly not saved time, although exposure to the os library and the command line has made it worthwhile

import os

directory = "2P6 Communications" # engineering topic target
old_files, new_files = [], []

for file in os.listdir(directory):
	if file[0]=='L': new_files.append(file) # updated notes have format: "Lecture_n"
	else: old_files.append(file) # unfilled notes

new_files.sort(); old_files.sort() # ensure corresponding numbering

for i in range(len(new_files)):
	try:
		os.remove(directory+"/"+old_files[i]) # avoid same name error
		os.rename(directory+"/"+new_files[i], directory+"/"+old_files[i]) # update filenames
	except PermissionError:
		print("Unable to rename %s: Old/new file being used by another process" %new_files[i])