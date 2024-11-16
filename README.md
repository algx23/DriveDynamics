# DriveDynamics - See your driving telemetry 

## SAFETY / LEGAL WARNING
As of the current version of this program, it will require your laptop to be open while driving.By downloading DriveDynamics, you agree to follow all road traffic safety laws in your country, state or "gemeinde", and this includes not putting your focus on your device(s_) while driving.

I am not responsible for any damages that may come about if you choose to take your focus off the road to look at the program while driving.

Safety is paramount in all situations, and if this product is likely to, or you yourself are prone to being easily distracted while driving and using something like this, then I HIGHLY SUGGESTyou to not download and use this program - for both your own safety and the safety of all other road users, pedestrians, and anyone in your community around you



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
```git clone https://github.com/algx23/DriveDynamics.git```


2. ** Navigate to the cloned repo **

```cd DriveDynamics/```

3. ** Install Dependencies **

```pip install -r requirements.txt```

4. ** Connect to OBD Interface **

Ensure your car has a OBD Interface with eg an OBDii Reader in, and connect via a USB Port

5. ** Run main.py **

```py src/main.py```

## Feedback

If you have any ideas, or suggestions, or you find a bug in this project (likely :p), feel free to open an Issue! Any and all feedback is appreciated, just keep it constructive! 

---

Thanks so much for using DriveDynamics!

