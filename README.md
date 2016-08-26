# VarValueAcquirer
Asks the ExpRunner for the variable values and shows the value of a specific variable. GUI is written in MatLab, socket 
communication, Xml parsing and pre processig is written in python.

All the variable names are converted to lower case. So you nee to type the as such in the edit field. Problems could arise if the names contain special characters MatLab cannot deal with. If that happeneds replace them in getVariables.py


Installation:
Put the files in a folder of your choice, just put all in one. Change in ec_socket.py the ip and the port of the expRunner host. The files must be in your MatLab working directory. 
