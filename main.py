from flask import Flask, render_template, request
from time import sleep
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")



@app.route("/post", methods=['GET','POST'])
def poster():
    if request.method == "POST":

        #   Collect JSON data sent by POSTer method every 50ms. It saves 
        #   strings into 4 variables which varies from -100 to 100
         
        content = request.json
        motorX = json.dumps(content['motorX'])      
        motorY = json.dumps(content['motorY'])
        servo1 = json.dumps(content['servoX'])
        servo2 = json.dumps(content['servoY'])

        #   Optional/debug, print variables

        print("steering X : ", motorX)
        print("steering Y : ", motorY)
        print("speed X    : ", servo1)
        print("speed Y    : ", servo2)           

        return "ok"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')