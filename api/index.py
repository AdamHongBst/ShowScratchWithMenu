from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(302)  # 设置重定向状态码 302
        self.send_header('Location', '/ShowScratchWithMenu.html')  # 设置重定向的目标路径
        self.end_headers()
        return
