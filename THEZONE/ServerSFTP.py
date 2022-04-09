import pysftp

sftpHost='speapl305'
sftpPort='22'
sftpusername='oracle'
sftpPassword='pHe6aJeB'

cnOpts=pysftp.CnOpts()
cnOpts.hostkeys=None



def isOnTheServer(mdslocations):
    snake=pysftp.Connection(host=sftpHost,password=sftpPassword,cnopts=cnOpts,username=sftpusername,port=22) 
    WsdlPath='/SOA/Oracle/AIA/comms_home/source/soainfra/apps'
    
    for  location in mdslocations :
       #print(WsdlPath+location)
       mdslocations[location]=snake.exists(remotepath=WsdlPath+location) 
       #print(snake.exists(remotepath=WsdlPath+location))
    
    snake.close()
    return mdslocations

