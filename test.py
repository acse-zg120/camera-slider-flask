# from flask import Flask
# import RPI.GPIO as GPIO
# from time import sleep
# from RpiMotorLib import RpiMotorLib
# from os import os

# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'RPI')

# # Define pins to A4988
# GPIO_pins = (14,14,18)      # Microstep Resolution MS1 to MS3 -> GPIO Pin
# dir_pin= 20                 # Driection -> GPIO Pin
# step_pin = 21               # Step -> GPIO Pin

# app = Flask(__name__)

# slider = request.form["slider"]
# print(int(slider))


# # def hello():
# #     return 'Hello World'

# @app.route('/', methods=['POST', 'GET'])


# def home():

#     if request.method == 'POST':
#         return("Hello world")

#     else:
#        pass

# if __name__ == '__main__':
#     app.run(host= '192.168.43.137', port=5050, debug=True)




from flask import Flask, render_template_string, request 
from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

app = Flask(__name__)

#HTML Code 

TPL = '''
<html>
     <img src="https://iotdesignpro.com/sites/default/files/Iot%20Design%20Pro%20Logo_0.png" alt="">
    <head><title>Web Page Controlled Stepper</title></head>
    <body>
    <h2> Web Page to Control Stepper</h2>
        <form method="POST" action="test">
            <h5> Use the slider to rotate Stepper Clockwise & Counter-Clockwise  </h5>
            <p>Slider   <input type="range" min="1" max="20" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>


'''
 
@app.route("/")
def home():

    return render_template_string(TPL)
 
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    print(int(slider))
  
    if (int(slider)>10):
       mymotortest.motor_go(True, "Full" , 600,int(slider)*.0004, False, .05)
       print("Rotating Clockwise")
    
    if (int(slider)<10):
       mymotortest.motor_go(False, "Full" , 600,int(slider)*.001, False, .05)
       print("Rotating Anti-Clockwise")

    
    return render_template_string(TPL)
 
#Yomi added a comment
# Run the app on the local development server
if __name__ == "__main__":
    app.run(host= '192.168.43.137', port=5050, debug=True)