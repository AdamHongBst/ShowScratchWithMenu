from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(302)  # 302状态码表示临时重定向
            self.send_header("Location", "/ShowScratchWithMenu.html")  # 设置跳转的目标URL
            self.end_headers()
        else:
            self.send_response(404)  # 返回404状态码表示页面不存在
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

