from ec_socket import getXml
from xmlExtract import extractDataFromXML
from scipy.io import savemat
import sys

#Gets the xml from ExpCtr and saves them as .mat
def getVariables(varFilePath):

    #Port and Ip for server that host expRunner
    port = 8093
    ip = '134.100.104.14'
    
    #Get the xml file from the exprunner as one long string using getXml()
    #with the ip and the port passed from the multiscope config file
    fileString = getXml(port, ip)
    #Extract data from the control-file.
    dataList = extractDataFromXML(fileString)
    #begin = time.time()    #in der Liste kommen erst Variablen, dann Timing, dann Events
    vars = dataList[0]
    #save the data into a .mat-File.
    savemat(varFilePath, vars)

#----------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    getVariables(sys.argv[1])
    sys.exit(0)

