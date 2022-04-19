"""
    Learn how to use tkinter
        > Canvas
        > PhotoImage
        > tkinter.TK().after ( equivalent to set timeout / interval )
        > tkinter.TK().after_cancel ( canceling the interval )

    The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.
    It uses a timer to break work into intervals, typically 25 minutes in length, separated by short breaks.

    When start counter begin
        1st 25 minute work, then 5 minute break,
        2nd 25 minute work, 5 minute break,
        3rd 25 minute work, 5 minute break,
        4th 25 minute work, 5 minute break,
        and last 20 minute work
"""
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

is_in_timer = False
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global is_in_timer
    global reps

    is_in_timer = False
    minutes = 0
    second = 0
    reps = 0
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{second:02d}")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def trigger_start():
    global is_in_timer

    if is_in_timer:
        print(f"still in timer with sequence : {reps}")
        return

    is_in_timer = True
    start_timer()


def start_timer():
    global reps
    global is_in_timer

    reps += 1
    if reps % 2 == 1 and reps < 8:
        countdown(WORK_MIN * 60)
        title.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        countdown(SHORT_BREAK_MIN * 60)
        title.config(text="Short Break", fg=PINK)
    elif reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        title.config(text="Long Break", fg=RED)
    else:
        reps = 0
        is_in_timer = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = int(count / 60)
    second = int(count % 60)

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{second:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor((reps / 2))):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.grid(row=0, column=0, columnspan=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#countdown(5)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)
start_button.config(command=trigger_start)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)
reset_button.config(command=reset_timer)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
