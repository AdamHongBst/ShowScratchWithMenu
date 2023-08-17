from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    # 使用 redirect 函数重定向到根目录下的 ShowScratchWithMenu.html 文件
    return redirect(url_for('static', filename='ShowScratchWithMenu.html'))

if __name__ == "__main__":
    app.run()
