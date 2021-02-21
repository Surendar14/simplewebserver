from http.server import HTTPServer, BaseHTTPRequestHandler

Content = """
<!doctype html>
<html>
<head>
<title>my webserver</title>
</head>
<body>
<h1>MULTIPLICATION TABLES OF 11</h1>
11×0=0<br>
11×1=11<br>
11×2=22<br>
11×3=33<br>
11×4=44<br>
11×5=55<br>
11×6=66<br>
11×7=77<br>
11×8=88<br>
11×9=99<br>
11×10=110<br>
</body>
</html>
"""


class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request recived")

        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()

     # to send the responce
        self.wfile.write(Content.encode())

 # to create server address
server_address = ('', 80)

# to listen at the specified port
httpd = HTTPServer(server_address, myhandler)
print("MY WEBSERVER IS RUNNING...")
httpd.serve_forever()
