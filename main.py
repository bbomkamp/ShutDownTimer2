import tkinter
import tkinter.ttk as ttk
import threading
import os

# Window
window = tkinter.Tk()
window.title("ShutDown Timer")


# Frame
frame = tkinter.Frame(window)
frame.pack()

# Duration Frame
user_input_frame = tkinter.LabelFrame(frame, text="Duration")
user_input_frame.grid(row=0, column=0, padx=20, pady=20)

# Time Entry
time_entry = tkinter.Entry(user_input_frame)
time_entry.grid(row=0, column=0, padx=20, pady=20)

# Unit of Time
time_type = tkinter.StringVar()
time_type_combo = ttk.Combobox(user_input_frame, textvariable=time_type, values=["minutes", "hours", "seconds"])
time_type_combo.current(0)
time_type_combo.grid(row=0, column=1, padx=20, pady=20)


# Progress Frame
duration_frame = tkinter.LabelFrame(frame, text="Progress")
duration_frame.grid(row=1, column=0)

# Progress Circle
canvas = tkinter.Canvas(duration_frame, width=200, height=200,  highlightthickness=0)
canvas.pack()

# Time Remaining
remaining_time_label = tkinter.Label(duration_frame, text="", font=("TkDefaultFont", 14))
remaining_time_label.pack(pady=5)

# Buttons Frame
buttons_frame = tkinter.LabelFrame(frame)
buttons_frame.grid(row=2, column=0, padx=20, pady=20)

after_id = None

# Start Countdown
def start_countdown():
    global after_id
    start_button.config(state=tkinter.DISABLED)  # Disable the start button
    time = time_entry.get()
    time_type = time_type_combo.get()

    try:
        time = int(time)
        if time_type == "minutes":
            time *= 60
        elif time_type == "hours":
            time *= 3600
        if time <= 0:
            raise ValueError("Time must be greater than 0")

        # Schedule the first iteration of the countdown in a new thread
        t = threading.Thread(target=countdown, args=(time, time))
        t.start()
    except ValueError as e:
        stop_countdown()  # Stop the countdown
        tkinter.messagebox.showerror("Error", str(e))

# Start Button
start_button = tkinter.Button(buttons_frame, text="Start", command=start_countdown)
start_button.grid(row=0, column=0)

# Stop Countdown
def stop_countdown():
    global after_id
    start_button.config(state=tkinter.NORMAL)  # Enable the start button
    if after_id:
        window.after_cancel(after_id)
        after_id = None
        canvas.delete("all")
        remaining_time_label.config(text="")

# Cancel Button
cancel_button = tkinter.Button(buttons_frame, text="Cancel", command=stop_countdown)
cancel_button.grid(row=0, column=1)


# Function to update the countdown display
def countdown(remaining_time, total_time):
    global after_id
    remaining_time -= 1

    # Calculate the remaining hours, minutes and seconds
    hours = remaining_time // 3600
    seconds = remaining_time % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    # Update the remaining time label
    remaining_time_label.config(text="{} hours {} minutes {} seconds".format(hours, minutes, seconds))

    # Update the progress circle
    canvas.delete("all")
    canvas.create_arc(10, 10, 190, 190, start=90, extent=360*(remaining_time/total_time), fill="#16c5f5", width=2)

    # Check if the time has reached 0 and shut down the system
    if remaining_time <= 0:
        os.system("shutdown /s /t 1")
    else:
        # Schedule the next iteration of the countdown
        after_id = window.after(1000, countdown, remaining_time, total_time)





window.mainloop()
