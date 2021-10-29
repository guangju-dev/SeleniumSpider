# -- coding: utf-8 --
from flask import Flask
from SeleniumSearch import finddoi
app = Flask(__name__)
username = ""
password = ""
brower_location = "http://sso.hnlat.com/"
website = ""
#简单的Hello World
@app.route("/")
def hello_word():
    return "Hello Word"
#收到客户端的请求并解析其url获得搜索关键词,也就是search_id
@app.route("/doi/<search_id>")
def search(search_id):
    doi_text = finddoi(username, password,brower_location, search_id,website)
    return doi_text
if __name__ == '__main__':
    app.run()