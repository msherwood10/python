#checks for file in a directory
import os
#work_path should be the directory where the files are stored
error_code=0
work_path = "F:\MediaFire\Uploads"
if not os.listdir(work_path):
	#debugging
	print"directory is empty"
	error_code = 1
else:
	#fname should be a regex entry to match the sample file naming convention
	file_exists = os.path.isfile("README.md")
	if file_exists is True:
		with open("F:\Github\python\samplefilecheck.txt", "w") as textfile:
			textfile.write("File exists and was created at"+str(os.stat.st_ctime("README.md"))
#debugging
#if error_code=0:
#	print "File exists and was created at", os.stat.st_ctime
#else:
#	print "Error code",error_code

#print os.stat.st_ctime("README.md")
