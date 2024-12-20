# DriveDynamics - See your driving telemetry

## SAFETY / LEGAL WARNING

DriveDynamics is designed for informational purposes only and should NEVER be used while operating a vehicle. By downloading and using this software, you agree to:

- Use DriveDynamics only when your vehicle is completely stopped and safely parked.
- Comply with all applicable traffic laws and regulations in your jurisdiction.
- Never interact with your device or this software while driving.

IMPORTANT: The developer of DriveDynamics is not responsible for any accidents, injuries, or damages resulting from the use or misuse of this software. If you are prone to distraction while driving, DO NOT use this program.
Your safety and the safety of others on the road are paramount. Distracted driving is dangerous and often illegal. If you cannot use this program safely and responsibly, please do not download or use it.

## About the Project

Have you ever wanted to see in-depth details about your driving? Perhaps you want to see your throttle inputs, or maybe you want to see how you modulate the brake pressure, in an objective way? Maybe, like me, you also think that this is just a pretty neat thing to see, even if you may not use it all the time.

If that sounds like something you'd like, you'll love this project! I used the pythonOBD library to read data from the obd sensors in your car, and then plot them in neat little graphs :). Sure, right now, there aren't that many different graphs to choose from, but as the project evolves, you'll be able to see almost anything you can see with your OBD Reader, in graphical form!

In the future, I will be working on a nice GUI to go with this application, so stay tuned for that.

In the meantime, happy driving! :D!

## Prerequisites

- For this to work, you must have a USB Connection in your car, to plug in your device.
- You must also have an OBD Reader so that the data from the sensors can be collected by the program (don't worry, all the data will stay on your device, so I or anyone else will have 0 access to it).

## Installation

1. ** Clone the Repository **

powershell
`git clone https://github.com/algx23/DriveDynamics.git`

2. ** Navigate to the cloned repo **

`cd DriveDynamics/`

3. ** Install Dependencies **

`pip install -r requirements.txt`

4. ** Connect to OBD Interface **

Ensure your car has a OBD Interface with eg an OBDii Reader in, and connect via a USB Port

5. ** Run main.py **

`py src/main.py`

## Feedback

If you have any ideas, or suggestions, or you find a bug in this project (likely :p), feel free to open an Issue! Any and all feedback is appreciated, just keep it constructive!

---

Thanks so much for using DriveDynamics!
