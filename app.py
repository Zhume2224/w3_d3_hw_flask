from flask import Flask,url_for
app=Flask (__name__)
from controllers import controller

if __name__=='__main__':
    app.run(debug=True)
