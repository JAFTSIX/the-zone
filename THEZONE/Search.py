from ast import For
from configparser import DuplicateSectionError
import io
import re

#0 means that the file needs to be on the system
def search():
    print('starting the search for MDS dependencies')
    searchReplaceFile=io.open('.\\search&replace.txt','r')
    lines=searchReplaceFile.readlines()
    searchReplaceFile.close()
    mdslocations={}
    for line in lines:
        if line.rfind('<oramds:/apps>/AIAMetaData/AIAComponents')>-1:
            #copy everithing inside""
            line=re.findall(f'".*?"',line)[0]
            result=re.sub('"<oramds:/apps>','',line)[:-1]
            mdslocations[result]=0

    print(mdslocations)



search()    