import http.server
import socketserver

PORT = int(input("input port number: "))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server is runing! http://127.0.0.1:",PORT,"\nPress Ctrl+C to stop the server.")
    httpd.serve_forever()