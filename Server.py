'''
Created on Sep 20, 2018

@author: andrewdixon
'''
#Server 

# first of all import the socket library
import socket

# next create a socket object, with parameters ip and connection type (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print( "socket binded to %s" %(port) )

# put the socket into listening mode
s.listen(5)
print( "socket is listening")

# a forever loop until we interrupt it or
# an error occurs
ships = 17
while ships > 0:

# Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr )

    #Receive the data
    data = conn.recv(64)

    # send a thank you message to the client.
    c.send('Thank you for connecting')

# Close the connection with the client
#
c.close()

def update(xcor, ycor):
    #Access document (need a get?)
    #change xcor and ycor so that they're read in properly
    xcor -= 1
    ycor = len(board[])- ycor
    #O represents a miss, but previously shot. x represents a previous hit
    if board[ycor,xcor] == 'x' or board[ycor,xcor] == 'o':
        #Print error
    elif board[ycor,xcor] == ' ':
        #may need to http post this
        board[ycor,xcor] = 'o'
        #return miss
    #If hit
    else:
        #May need http post
        board[ycor][xcor] = 'x'
        ships -= 1
        #return hit
    
    #Get 
    #Probably an http post to your side's board
    return 


