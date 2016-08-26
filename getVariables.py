from ec_socket import getXml
from xmlExtract import extractDataFromXML
from scipy.io import savemat
import sys

#Gets the xml from ExpCtr and saves the variables as .mat
#Takes a file full path as argument that is used to save the .mat file at.
def getVariables(varFilePath):

    #Port and Ip for server that host expRunner
    port = 8093
    ip = '134.100.104.14'
    
    #Get the xml file from the exprunner as one long string using getXml()
    fileString = getXml(port, ip)
    #Extract data from the control-file.
    dataList = extractDataFromXML(fileString)
    #dataList[0] contains variables, dataList[1] timing and dataList[2] events. 
    vars = dataList[0]
    #save the data into a .mat-File.
    savemat(varFilePath, vars)

#----------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    getVariables(sys.argv[1])
    sys.exit(0)

