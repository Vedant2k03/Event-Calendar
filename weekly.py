import schedule
import time
from tkinter import *
from plyer import notification
from tkinter import messagebox

def week_rem():
    s_week=Tk()
    s_week.title("Reminder")
    s_week.geometry('700x330')
    #s_min.config(bg='lightsteelblue')

    Frame_s = Frame(s_week,bg='lightgreen' , borderwidth=10) 
    Frame_s.pack(side=TOP,fill=X)

    l = Label(Frame_s, text= "Schedule weekly reminder", font='comicsansns 20 bold', bg='lightgreen')
    l.pack()

    s_week_title = Label(s_week, text="Enter Title", font="poppins  15 ")
    s_week_title.place(x=10,y=70)

    s_week_sub = Label(s_week, text="Enter Subject", font="poppins 15 ")
    s_week_sub.place(x=10,y=120)

    sw_week = Label(s_week, text="Enter week day", font="poppins 15 ")
    sw_week.place(x=13,y=170)

    s_week_time = Label(s_week, text="Enter Time", font="poppins 15 ")
    s_week_time.place(x=13,y=220)

    s_title_entry = Entry(s_week, width='40',font="poppins 15 ")
    s_title_entry.place(x=200,y=70)

    s_sub_entry = Entry(s_week, width='40',font="poppins 15 ")
    s_sub_entry.place(x=200,y=120)

    s_week_entry = Entry(s_week, width='20',font="poppins 15 ")
    s_week_entry.place(x=200,y=170)

    s_time_entry = Entry(s_week, width='5',font="poppins 15 ")
    s_time_entry.place(x=200,y=220)

    s_time_format = Label(s_week,text="Hour:Minute (24 hr)",font="poppins 15 ")
    s_time_format.place(x=280,y=220)

    def a1():
        global a,b,c

        a = s_time_entry.get()
        b = s_title_entry.get()
        c = s_sub_entry.get()
        d = s_week_entry.get()

        if a=="" or b=="" or c=="" or d=="":
                messagebox.showerror("Alert", "All fields are required!")
        else:
                messagebox.showinfo("notifier set", "set notification ?")
                s_week.destroy()

                if d.lower()=='monday':
                    schedule.every().monday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)
                
                elif d.lower()=='tuesday':
                    schedule.every().tuesday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                elif d.lower()=='wednesday':
                    schedule.every().wednesday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                elif d.lower()=='thursday':
                    schedule.every().thursday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                elif d.lower()=='friday':
                    schedule.every().friday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                elif d.lower()=='saturday':
                    schedule.every().saturday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                elif d.lower()=='sunday':
                    schedule.every().sunday.at(a).do(notify)
                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                else:
                    messagebox.showerror("Alert", "Enter correct week day!")


    s_min_but = Button(s_week, width='10', text="Set",font=("poppins", 15, "bold"), command=a1, bg='lightsteelblue')
    s_min_but.pack(side=BOTTOM,pady=10)


    def notify():
            notification.notify(title=b,
                                    message=c,
                                    app_icon="D:\Python PBL\F Code\ico.ico",
                                    timeout=10)
            
    s_week.resizable(0,0)
    s_week.mainloop()