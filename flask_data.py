#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h1>hello world</h1>" #h1은 큰 글씨

