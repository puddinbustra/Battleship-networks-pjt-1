from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from urllib.parse import unquote, urlparse
import sys
import csv

#global var (I'd rather have this accessed from the class below, but dont know how to make that happen)
global_cord = "x=4"

#class update_board()  (we need to get this into a class so that it can be called
#                       multiple times)

#formats own_board.txt into a html doc that can be passed in do_GET
contents = open("own_board.txt","r")
with open("own_board.html", "w") as e:
    e.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />')
    for lines in contents.readlines():
        e.write( lines + "<br />" )

#formats opponent_board.txt into a html doc that can be passed in do_GET
contents = open("opponent_board.txt","r")
with open("opponent_board.html", "w") as e:
    e.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />')
    for lines in contents.readlines():
        e.write( lines + "<br />" )


#creates array of board (this needs to be a class so that we can
#read in a board, update this one with it, and then easily access cordinates
#to see if there was a hit or not)
#if there is a hit, our own_board.txt needs to be updated to show that it was hit
#array_own_board = ['0'] * 10

#class split_board
file = open('own_board.txt')
board = []
for line in file.readlines():
    line = line.strip()
    y = [value for value in list(line)]
    board.append( y )
file.close()
print(board)

class UpdateBoard:

    def __init__ (self):
        self.x = 'working'

    def write_board(self):

        with open("onw_board.txt", "w") as output:
            output.write(str(board))

        # with open('own_board.txt', 'w') as f:
        #     writer = csv.writer(f, delimiter='')
        #     #(f, delimiter=',')
        #     writer.writerows(board)  #considering my_list is a list of lists.



class Battleship:
    #method for determining if it was a hit, or if it was an exeption
    #(probably needs to import both the board and the cordinates)
    #(needs to return hit, type, sunk, been_hit)

    def __init__ (self, cordinates):
        self.cordinates = cordinates

    def hit(self):
        hit = 0
        type = "A"
        sunk = 0
        been_hit = 0
        #cordinats to the left, right, top, bottom
        check_cord_l = "N"
        check_cord_r = "N"
        check_cord_b = "N"
        check_cord_t = "N"
        x_cord = self.cordinates[0]
        y_cord = self.cordinates[1]
        print(x_cord)
        print(y_cord)

        if (
            board[x_cord][y_cord] == "C" or board[x_cord][y_cord] == "B"
            or board[x_cord][y_cord] == "R" or board[x_cord][y_cord] == "S"
            or board[x_cord][y_cord] == "D"
          ):
           hit = 1
           type = board[x_cord][y_cord]
           board[x_cord][y_cord] = "x"

           #check to see if it is sunk on the x axis
           if x_cord == 0:
               check_cord_r = board[x_cord+1][y_cord]

           elif x_cord == 9:
               check_cord_l = board[x_cord-1][y_cord]

           else:
               check_cord_l = board[x_cord-1][y_cord]
               check_cord_r = board[x_cord+1][y_cord]



           if y_cord == 0:
               check_cord_b = board[x_cord][y_cord-1]

           elif y_cord == 9:
               check_cord_t = board[x_cord][y_cord+1]

           else:
               check_cord_b = board[x_cord][y_cord-1]
               check_cord_t = board[x_cord][y_cord+1]

           while True:
                   check_cord_l != type
                   check_cord_r != type
                   check_cord_b != type
                   check_cord_t != type
                   sunk = 1

        elif board[x_cord][y_cord] == "x":
           been_hit == 1

        return(hit, type, sunk, been_hit)


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

        # function to reply to HTTP GET calls
        def do_GET(self):
            print(urlparse(self.path))

                #url path to get to own_board
            if urlparse(self.path).path == "/own_board.html":
                f = open('own_board.html', 'rb')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><head><title>BattleShip</title></head>")
                self.wfile.write(b"<body><p>Your BattleShip Board</p>")
                self.wfile.write(f.read())
                f.close()
                self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, 'utf-8'))
                self.wfile.write(b"</body></html>")

                #url path to get to opponent_board
            elif urlparse(self.path).path == "/opponent_board.html":
                f = open('opponent_board.html', 'rb')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><head><title>BattleShip</title></head>")
                self.wfile.write(b"<body><p>Opponent BattleShip Board</p>")
                self.wfile.write(f.read())
                f.close()
                self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, 'utf-8'))
                self.wfile.write(b"</body></html>")

                #url without a path
            else:
                f = open('opponent_board.html', 'rb')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><head><title>BattleShip</title></head>")
                self.wfile.write(b"<body><p>Standard BattleShip Board</p>")
                self.wfile.write(f.read())
                f.close()
                self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, 'utf-8'))
                self.wfile.write(b"</body></html>")


        print("working")

    #        f = open('battleship.html', 'rb')
            # self.send_response(200)
            # self.send_header("Content-type", "text/html")
            # self.end_headers()
            # self.wfile.write(b"<html><head><title>BattleShip</title></head>")
            # self.wfile.write(b"<body><p>Your BattleShip Board</p>")
            # self.wfile.write(f.read())
            # f.close()
            # # If someone went to "http://something.somewhere.net/foo/bar/",
            # # then s.path equals "/foo/bar/".
            # self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, 'utf-8'))
            # self.wfile.write(b"</body></html>")

        # POST
        def do_POST(self):
            # Doesn't do anything with posted data
            hit = 0
            type = "N"
            sunk = 0
            been_hit = 0

            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            print(self.headers['content-type'])
            print(post_data)
            print(self.address_string())
            info = urlparse(self.path).query
            print(info)
            x_cord = int(info[2])
            y_cord = int(info[5])
            mylist = [x_cord, y_cord]
            print(mylist)
            battleship = Battleship(mylist)
            hit, type, sunk, been_hit = battleship.hit()
            newBoard = UpdateBoard()
            newBoard.write_board()
            #url = unquote(o.params)
            #print(url)

            # we need code in here (probably run in an other class) that will take the
            # firing cordinates and determine if it was a hit, miss, or exeption
            # result = battleship.hit(post_data)
            # if result == hit:

            if isinstance(x_cord, int) != True or isinstance(y_cord, int) != True:
                self.send_response(400)
                self.end_headers()
                response = BytesIO()
                response.write(b'This is POST request. ')
                response.write(b'Coordinants were out of Bounds')
                self.wfile.write(response.getvalue())


            elif x_cord > 9 or y_cord > 9:
                self.send_response(404)
                self.end_headers()
                response = BytesIO()
                response.write(b'This is POST request. ')
                response.write(b'Coordinants were out of Bounds')
                self.wfile.write(response.getvalue())

            elif been_hit == 1:
                self.send_response(410)
                self.end_headers()
                response = BytesIO()
                response.write(b'This is POST request. ')
                response.write(b'This has been hit already')
                self.wfile.write(response.getvalue())

            else:
                self.send_response(200)
                self.end_headers()
                response = BytesIO()
                response.write(b'hit=%d ' % hit)
                response.write(b'type=%s ' % bytes(type,'utf-8'))
                response.write(b'sunk=%d ' % sunk)
                response.write(b'been_hit=%d ' % been_hit)
                self.wfile.write(response.getvalue())


def run():
  print('starting server...')

  # Server settings
  server_address = ('127.0.0.1', 12345)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
