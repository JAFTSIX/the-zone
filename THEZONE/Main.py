import shutil
import os
import glob
import paths

#camino='pp/rest'
#os.makedirs(camino,exist_ok=True)
#shutil.copytree('ENV/',camino)         

text_files = glob.glob( "ENV\\**\\vipFile.txt", recursive = True)
print(text_files)
print(paths.repository11G) 

#print(os.path)