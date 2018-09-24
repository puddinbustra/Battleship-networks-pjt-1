from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from urllib.parse import unquote, urlparse

#class battleship(cordinates)
#   def hit(cordinates):
#    method for determining if it was a hit, or if it was an exeption

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Respond to a GET request."""
           self.send_response(200)
           self.send_header("Content-type", "text/html")
           self.end_headers()
           self.wfile.write("<html><head><title>Title goes here.</title></head>")
           self.wfile.write("<body><p>This is a test.</p>")
           # If someone went to "http://something.somewhere.net/foo/bar/",
           # then s.path equals "/foo/bar/".
           self.wfile.write("<p>You accessed path: %s</p>" % s.path)
           self.wfile.write("</body></html>")

        # POST
        def do_POST(self):
            # Doesn't do anything with posted data
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            print(self.headers['content-type'])
            print(post_data)
            print(self.address_string())
            info = urlparse(self.path).query
            print(info)
            mylist = info.split("&")
            print(mylist)


            #url = unquote(o.params)
            #print(url)

            # we need code in here (probably run in an other class) that will take the
            # firing cordinates and determine if it was a hit, miss, or exeption
            # result = battleship.hit(post_data)
            # if result == hit:

            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(b'This is POST request. ')
            response.write(b'hit=1')
            self.wfile.write(response.getvalue())


def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 12345)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
