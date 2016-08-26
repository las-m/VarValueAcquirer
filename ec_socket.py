import socket
import sys
import struct
#Use time for performance testing of the module
import time

#This function acquires and returns the xml file from the experiment runner
def getXml(port, ip):

    #Convert the port to integer type
    port = int(port)
    #The socket server sends the xml if a client sends "GETNEXT" to it
    old_message = "GETNEXT"
    #Actually the string needs to be processed a bit. First store it in a list
    old_message = list(old_message)
    #Initialize the variable I actually send to the server
    message = list()

    #I need "GETNEXT" as unicode code (numeric) 
    for x in old_message:
        message.append(ord(x))
    message.append(10)

    #Construct the socket object
    s = socket.socket()

    #Try to connect the socket using ip address and port passed to the function
    #If it fails throw an exception
    try:
        s.connect((ip, port))
    except:
        e = sys.exc_info()[0]
        print(e)

    #Convert the numeric representation (as list) of "GETNEXT"
    #to the bytes type and send these bytes
    s.send(bytes(message))

    #Initialize variables for storage of the answer 
    total_data=[];
    data='';
    #We need to make sure that the whole data is transmitted but the delay in the
    #Multiscope can't be too long. Therefore define a short timeout variable and
    #get the current time
    timeout = 0.0001
    begin=time.time()

    #beginReq = begin
    while 1:

        #If the data transmission timed out quit the loop
        if time.time()-begin > timeout:
            break

        #try to receive data. If it is succesfull add the received data to the
        #array containing the complete data. If there is no data wait and then
        #try again. If receiving the data fails try again immediately 
        try:
            data = s.recv(8192)
            if data:
                total_data.append(data)
                begin = time.time()
            else:
                time.sleep(0.0000001)
        except:
            pass
    #endReq = time.time() 

    #Close the socket when the data is complete
    s.close

    #duration = beginReq - endReq
    #print('Data revceiving:', duration)
    
    #Make a list of strings, where each string correspongs to a component of
    #the totaldata array.
    stringList = []
    for x in total_data:
        stringList.append(str(x,"ISO-8859-1"))

    #Join the strings. Now the data contained in the xml file can be
    #returned as one string
    return''.join(stringList)
