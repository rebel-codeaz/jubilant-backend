#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

comments = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        print(self.headers)
        len_msg = int(self.headers.get('Content-length',0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(len_msg).decode()

        # 3. Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]
        # print(parse_qs(data))   #{'message': ['heya']}
        # print(parse_qs(data)["message"])    #['heya']
        # print(parse_qs(data)["message"][0]) #heya
        message = message.replace("<", "&lt;")
        comments.append(message)
        # Send the "message" field back as the response.
        self.send_response(303)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Location', '/')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
       
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        prev = form.format("\n".join(comments))
        self.wfile.write(prev.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    print("message board server started at port 8000")
    httpd.serve_forever()
