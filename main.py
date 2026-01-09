from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Stops the timer and resets the display."""
    global timer
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER LOGIC ------------------------------- # 

def start_timer():
    """Starts the countdown from 25 minutes."""
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ----------------------- # 

def count_down(count):
    """The brain of the timer: calculates math and updates the UI."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # This keeps the '00' formatting
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Focus Buddy")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Timer Display (Using a Red Box background instead of an image)
canvas = Canvas(width=200, height=224, bg=RED, highlightthickness=0)
timer_text = canvas.create_text(
    100, 112, text="25:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()