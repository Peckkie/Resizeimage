import os 
import subprocess

path = '/home/gigi01/pics'

files_list = os.listdir(path)

for f in files_list:
	print(f)
	subprocess.call(['ffmpeg','-i',os.path.join(path,f),'-vf','scale=90:90',f])

