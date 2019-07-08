#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json
from flask import render_template

app = Flask(__name__)



# 请您来修正Hello, word的拼写错误吧！
# 请在修改完成后，通过主菜单 Git/Commit ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到Factory ( http://factory.cloudtogo.cn/project/blueprint?id=last )，用同样的方法发布一个新实例即可看到修改后的效果。



# @app.route('/api/hello', methods=['GET'])
# def start():
#     return json.dumps({
#         'code': '0'
#     })
#
# @app.route('/api/test1', methods=['POST'])
# def apitest1():
#     jsonself = request.get_json()
#     username = jsonself['username']
#     password = jsonself['password']
#     print(username)
#     print(password)
#     return json.dumps({
#         'username': '%s' % (username)
#     })

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug=True)
