'''
Created on Sep 20, 2018

@author: andrewdixon, Hugh O'Neill
'''
# Import socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# Get the coords, and send them to the server
coords = input("What coordinants would you like? eg '3,4': ")
# change xcor and ycor so that they're read in properly
xcor,ycor = int(coords[0]),int(coords[2])
xcor -= 1
# At least if it's a text file, I think this is how it works
# We can replace len(board) with the default number if it's inconvenient
ycor = len(oppboard[])- ycor
s.send(xcor,ycor)

# receive if it was a hit. Then update your copy of opp board
data = s.recv(64)
update(data)

# close the connection
s.close()

def update(status)
    #Update your copy of the opponent's board, may need the http messages
    if(status == "hit"):
        oppboard[ycor,xcor] = 'x'
    elif(status == "miss"):
        oppboard[ycor,xcor] = 'o'
    #If you have to deal with an error when it's returned, then deal with that here
    else:
        print("Error")



