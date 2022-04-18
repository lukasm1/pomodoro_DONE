import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps=0
checkmarks=""
cd_timer=""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps, checkmarks
    canvas.itemconfig(timer_txt, text=f"00:00")
    timer.config(text="Timer", fg=GREEN)
    reps=0
    checkmarks=""
    window.after_cancel(cd_timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps==9:
        pass
    elif reps % 2 !=0:
        timer.config(text="Work")
        count_down(work_sec)
    elif reps%8:
        timer.config(text="Break", fg=RED)
        count_down(short_break_sec)
    else:
        timer.config(text="Break", fg=PINK)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, checkmarks, cd_timer
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count>0:
        cd_timer=window.after(1000, count_down, count-1)
    else:
        if reps % 2 != 0:
            checkmarks += "✔"
            checkmark.config(text = checkmarks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.minsize(width=200, height=200)
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_txt=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer=Label(text="Timer", fg=GREEN, font=("Arial", 50, "normal"), bg=YELLOW)
timer.grid(column=1, row=0)

start=Button(text="Start", bg="white", highlightthickness=0, borderwidth=0, command=start_timer)
start.grid(column=0, row=2)

reset=Button(text="Reset", bg="white", highlightthickness=0, borderwidth=0, command=reset)
reset.grid(column=2, row=2)

checkmark=Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark.grid(column=1, row=3)

window.mainloop()