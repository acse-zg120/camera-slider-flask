from flask import Flask, escape, request, redirect, render_template
#from os import path
import RPI.GPIO as GPIO
from time import sleep
from RpiMotorLib import RpiMotorLib

# from datetime import datetime
# import os.path
# import pigpio
# import time
# import json
# import logging

app = Flask(__name__)

# Disable logs except errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Define pins to A4988
GPIO_pins = (14,14,18)
dir_pin= 20
step_pin = 21

slider = request.form["slider"]
print(int(slider))

# pi = pigpio.pi()

#base_path = os.path(__file__).parent
# base_path = os.path.relpath(__file__)
# save_path = (base_path / "save.json").resolve()
save_path = os.path.relpath("./save.json")

gloriousRGBHex = "#FFFFFF"

hex_dict = {"color": ""}

########################################### Functions ########################################### 



######################################### End of Functions #########################################

# Functiom call
# Retrieves color hex from json file at launch
retrieveFromJSON()
rgbValue = convertHexToRGB(gloriousRGBHex)
enableGloriousRGB(rgbValue)

########################################### Flask Section ########################################### 
@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
    
    else:
        pass
    return render_template('index.html', RGBHex=RGBHex)
    # The first RGBHex is the value I'm using in the html and the second is the value declared above

# @app.route('/zihui')
# def zihui():
#     return ("Hi my name is Zihui")

if __name__ == '__main__':
    app.run(host= '192.168.43.137', port=5050, debug=True)
    #app.run(port=5001) - old line that is integrated to line above
    #Debug basically allows calling the python script to run as flask
    #It also allows webpage to be updated without ending and starting script

#export FLASK_APP=firstflask.py

####################################### End of Flask Section ######################################