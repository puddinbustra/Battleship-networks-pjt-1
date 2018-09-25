'''
Created on Sep 20, 2018

@author: andrewdixon
'''
# Import socket module

import requests

# Get the coords, and send them to the server
coords = input("What coordinants would you like? eg '3,4' in the form y,x: ")
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

ahit = int(r.text[4])
atype = r.text[11]
#Update the oppboard.txt
file = open ('opponent_board.txt','r')

board = []
for line in file.readlines():
    line = line.strip()
    y = [value for value in list(line)]
    board.append( y )

if ahit == 0:
    board[ycor][xcor] = '0'
else:
    board[ycor][xcor] = '1'

print(xcor)
print(ycor)

mstring = ""
for y in range(len(board)):
    for x in range(len(board)):
        mstring += board[y][x]
    mstring += '\n'
board = mstring
print(board)


#This updates the text file.
with open("opponent_board.txt", "w") as output:
    output.write(mstring)
    output.close()

#This updates the html file.
contents = open("opponent_board.txt","r")
with open("opponent_board.html", "w") as e:
    e.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />')
    for lines in contents.readlines():
        e.write( lines + "<br />" )
