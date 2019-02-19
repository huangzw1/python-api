#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json

app = Flask(__name__)
@app.route('/api/hello', methods=['GET'])


# 请您来修正Hello, word的拼写错误吧！
# 请在修改完成后，通过主菜单 Git/Commit ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到Factory ( http://factory.cloudtogo.cn/project/blueprint?id=last )，用同样的方法发布一个新实例即可看到修改后的效果。




def start():
    return json.dumps({
        'code': '0'
    })

if __name__ == '__main__':
    app.run()
