'''
Created on Sep 20, 2018

@author: andrewdixon
'''
# Import socket module

import requests

# Get the coords, and send them to the server
coords = input("What coordinants would you like? eg '3,4': ")
# change xcor and ycor so that they're read in properly
xcor,ycor = int(coords[0]),int(coords[2])
xcor -= 1
# At least if it's a text file, I think this is how it works
# We can replace len(board) with the default number if it's inconvenient
ycor -= 1

params = "x=" + str(xcor) + "y=" + str(ycor)

data = params
#params = "x=5&y=7"

r = requests.post('http://127.0.0.1:12345/', data, params = params)
print(r.status_code)
print(r.raise_for_status())
print(r.url)
print(r.text)

ahit = r.text[4]
atype = r.text[11]
#Update the oppboard.txt
file = open ('opponent_board.txt','r')
mstring = ""
for y in range(len(board)):
    for x in range(len(board)):
        if(y == ycor and x == xcor):
            if(ahit==1):
                mstring += atype
            if(ahit == 0)L
                mstring = '0'
        else:
            mstring += board[y][x]
            
    mstring += '\n'
file.close()
with open("opponent_board.txt", "w") as output:
    output.write(str(board))
