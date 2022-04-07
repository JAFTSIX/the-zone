from msilib.schema import Directory
from pathlib import Path
import shutil
import os
import glob
import paths

#camino='pp/rest'
#os.makedirs(camino,exist_ok=True)
#shutil.copytree('ENV/',camino)         

projectName= input('insert the name of the project: ')
projectNameFile=projectName+'.jpr'
location = glob.glob( paths.repository11G+'\\**\\'+projectNameFile, recursive = True)

location=location[0].replace(projectNameFile,'',1)
Directory=location.replace('C:\\Users\\Soin\\Documents\\Repository\\AIA11G','',1)
print(location) 


shutil.copytree(location,paths.Env+'\\'+projectName)
os.makedirs(paths.Env+Directory,exist_ok=True)
#print(os.path)
