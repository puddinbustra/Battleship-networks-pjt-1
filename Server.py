'''
Created on Sep 20, 2018

@author: andrewdixon, Hugh O'Neill
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
s.listen(1)
print( "socket is listening")

#Set up the game
    #Upload your board, and your copy of opponent's board

ships = 17
while ships > 0:

# Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    #Receive the pair of ints
    xcor,ycor = conn.recv(64)
    update(xcor,ycor)

# Close the connection with the client
c.close()

def update(xcor, ycor):
    #Access document (need a get?)
    #O represents a miss, but previously shot. x represents a previous hit
    if board[ycor,xcor] == 'x' or board[ycor,xcor] == 'o':
        #Send http error message to client
    elif board[ycor,xcor] == ' ':
        #may need to http post this
        board[ycor,xcor] = 'o'
        c.send("miss")
    #If hit
    else:
        #May need http post
        board[ycor][xcor] = 'x'
        ships -= 1
        c.send("hit")
    #Note that if we just update the local text file, it will have to be uploaded each time
     


