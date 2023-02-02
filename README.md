# ShutDown Timer
A GUI tool that can be used to set a timer to shut down the system.

![image](https://user-images.githubusercontent.com/37642026/216204784-f1ef5a95-93d5-4947-91a8-9300e5a752c4.png)


## Requirements
- Python 3
- Tkinter
- tkinter.ttk
- os
- threading

## How to Use
1. Enter the time you want the timer to run for.
2. Choose the unit of time (minutes, hours, or seconds).
3. Click the "Start" button to start the countdown.
4. The progress of the countdown will be displayed in a circle and the time remaining will be displayed in hours, minutes, and seconds.
5. Click the "Cancel" button to stop the countdown.

## Features
- Ability to choose between minutes, hours, or seconds as the unit of time.
- A visual representation of the progress of the countdown in the form of a circle.
- A display of the time remaining in hours, minutes, and seconds.

## Notes
- The system will be shut down once the timer reaches 0.
- The "Start" button will be disabled while the timer is running and re-enabled when the timer is cancelled.
