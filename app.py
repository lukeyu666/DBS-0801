#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template


# In[ ]:


import joblib


# In[ ]:


app = Flask(__name__)


# In[ ]:


@app.route("/", methods = ["GET","POST"])
def index():
    if request.methods == "POST":
        return(render_template("index.html",result1 = "OK", result2 = "OK"))
    else:
        return(render_template("index.html",result1 = "WAITTING", result2 = "WAITTING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




