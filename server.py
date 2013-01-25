import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
import sys

class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                   BaseHTTPServer.HTTPServer):
    pass

class MusicSiteHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	"""docstring for MusicSiteHandler"""
	def do_GET(self):
		text = "dsfasdfasdf"
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.send_header("Content-length", len(text))
		self.end_headers()
		self.wfile.write(text)


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server = ThreadingSimpleServer(('', port), MusicSiteHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"