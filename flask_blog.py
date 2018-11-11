# -*- coding: utf-8 -*-
# @Author: 三木
# @Date:   2018-11-10 19:43:34
# @Last Modified by:   三木
# @Last Modified time: 2018-11-10 20:59:24
from app import app,db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}