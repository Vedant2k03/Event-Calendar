import schedule
import time
from tkinter import *
from plyer import notification
from tkinter import messagebox

def daily_rem():
        s_daily=Tk()
        s_daily.title("Reminder")
        s_daily.geometry('700x300')
        #s_min.config(bg='lightsteelblue')

        Frame_s = Frame(s_daily,bg='lightgreen' , borderwidth=10, relief= GROOVE) 
        Frame_s.pack(side=TOP,fill=X)

        l = Label(Frame_s, text= "Schedule daily reminder", font='comicsansns 20 bold', bg='lightgreen')
        l.pack()

        s_daily_title = Label(s_daily, text="Enter Title", font="poppins  15 ")
        s_daily_title.place(x=10,y=70)

        s_daily_sub = Label(s_daily, text="Enter Subject", font="poppins 15 ")
        s_daily_sub.place(x=10,y=120)

        s_daily_time = Label(s_daily, text="Enter daily repeat", font="poppins 15 ")
        s_daily_time.place(x=13,y=170)

        s_title_entry = Entry(s_daily, width='40',font="poppins 15 ")
        s_title_entry.place(x=200,y=70)

        s_sub_entry = Entry(s_daily, width='40',font="poppins 15 ")
        s_sub_entry.place(x=200,y=120)

        s_time_entry = Entry(s_daily, width='5',font="poppins 15 ")
        s_time_entry.place(x=200,y=170)

        s_time_format = Label(s_daily,text="Hour:Minute (24 hr)",font="poppins 15 ")
        s_time_format.place(x=280,y=170)

        def a1():
                global a,b,c

                a = s_time_entry.get()
                b = s_title_entry.get()
                c = s_sub_entry.get()

                if a=="" or b=="" or c=="":
                        messagebox.showerror("Alert", "All fields are required!")
                else:
                        messagebox.showinfo("notifier set", "set notification ?")
                        s_daily.destroy()
                        schedule.every().day.at(a).do(notify)
                        while True:
                                schedule.run_pending()
                                time.sleep(1)

        s_min_but = Button(s_daily, width='10', text="Set",font=("poppins", 15, "bold"), command=a1, bg='lightsteelblue')
        s_min_but.pack(side=BOTTOM,pady=10)


        def notify():
                notification.notify(title=b,
                                        message=c,
                                        app_icon="D:\Python PBL\F Code\ico.ico",
                                        timeout=10)
                
        s_daily.resizable(0,0)
        s_daily.mainloop()