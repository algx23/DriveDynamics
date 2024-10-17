# DriveDynamics - See your driving telemetry 

## About the Project

Have you ever wanted to see in depth details about your driving? Perhaps you want to see your throttle inputs, or maybe you want to see how you modulate the brake pressure, in an objective way? Maybe, like me, you also think that this is just a pretty neat thing to see, even if you may not use it all the time.

If that sounds like something you'd like, you'll love this project! I used the pythonOBD library to rad data from the obd sensors in your car, and then plot them in neat litte graphs :). Sure, right now, there aren't that many different graphs to choose from, but as the project evolves, you'll be able to see almost anything you can see with your OBD Reader, in graphical form!

In the future, I will be working on a nice GUI to go with this application, so stay tuned for that.

In the meantime, happy driving! :D!


## Prerequisites

- For this to work, you must have a USB Connection in your car, to plug in your device.
- You must also have an OBD Reader so that the data from the sensors can be collected by the program (don't worry, all the data will stay on your device, so I or anyone else will have 0 access to it).

## Installation

1. ** Clone the Repository **

'''powershell
git clone https://github.com/algx23/DriveDynamics.git


2. ** Navigate to the cloned repo **

cd DriveDynamics/

3. ** Install Dependencies **

pip install -r requirements.txt

4. ** Connect to OBD Interface **

Ensure your car has a OBD Interface with eg an OBDii Reader in, and connect via a USB Port

5. ** Run main.py **

py src/main.py

## Feedback

If you have any ideas, or suggestions, or you find a bug in this project (likely :p), feel free to open an Issue! Any and all feedback is appreciated, just keep it constructive! 

---

Thanks so much for using DynamicDrive!

