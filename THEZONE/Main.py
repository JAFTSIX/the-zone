from msilib.schema import Directory
from pathlib import Path
import shutil
import os
import glob
import paths

projectName= input('insert the name of the project: ')
projectNameFile=projectName+'.jpr'
location = glob.glob( paths.repository11G+'\\**\\'+projectNameFile, recursive = True)

location=location[0].replace(projectNameFile,'',1)
Directory=location.replace('C:\\Users\\Soin\\Documents\\Repository\\AIA11G','',1)
print(location) 


shutil.copytree(location,paths.Env+'\\'+projectName)
os.makedirs(paths.Env+Directory,exist_ok=True)
#print(os.path)
input('now go and fill the search&replace txt i am waiting')