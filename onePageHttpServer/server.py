import time
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

# Script is inspired by
# https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
# https://wiki.python.org/moin/BaseHttpServer
# http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/


def get_network_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    return s.getsockname()[0]


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Simple Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><h1>Congrats! A Simple Server is established</h1>", "utf-8"))
        self.wfile.write(bytes("<p>You can either test the connection or port forwarding</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    hostname = get_network_ip()
    port = int(input("Please input the port number: "))
    myServer = HTTPServer((hostname, port), MyServer)
    print("Server started ...")
    print("You can enter {}:{} on your browser to open the page".format(hostname, port))
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
    myServer.server_close()
    print("Service stopped")
