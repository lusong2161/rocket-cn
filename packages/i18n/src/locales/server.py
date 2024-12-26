#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class TranslationServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def end_headers(self):
        # 添加必要的CORS头
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept')
        self.send_header('Access-Control-Max-Age', '86400')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/translation_verify.html'
        elif self.path.endswith('.json'):
            self.send_header('Content-Type', 'application/json; charset=utf-8')
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    print('启动翻译验证服务器...')
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, TranslationServer)
    print('服务器运行在 http://0.0.0.0:8000/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n关闭服务器...')
        httpd.server_close()
