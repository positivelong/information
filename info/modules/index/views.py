from flask import render_template

from info import redis_store
from . import index_blu

@index_blu.route('/')
def index():
    # 向redis中保存一个值 name long
    # redis_store.set("name", "long")
    return render_template('news/../../static/news/html/../../templates/news/index.html')
