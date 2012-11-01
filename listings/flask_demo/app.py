import pylinux.pylinux as pylinux

from flask import Flask
import time

app = Flask(__name__)

@app.route("/uptime")
def uptime():
    return 'Raspberry Pi up for %s hours' % str(pylinux.uptime())

@app.route("/")
def index():

    return ''' <center><h1> Flask on Raspberry Pi </h1></center> \n
               Time now ''' + time.ctime()

           
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
