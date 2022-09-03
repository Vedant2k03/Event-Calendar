import schedule
import time
from tkinter import *
from plyer import notification
from tkinter import messagebox

def min_rem():
        s_min=Tk()
        s_min.title("Reminder")
        s_min.geometry('700x300')
        #s_min.config(bg='lightsteelblue')

        Frame_s = Frame(s_min,bg='lightgreen' , borderwidth=10) 
        Frame_s.pack(side=TOP,fill=X)

        l = Label(Frame_s, text= "Snooze reminder", font='comicsansns 20 bold', bg='lightgreen')
        l.pack()

        s_min_title = Label(s_min, text="Enter Title", font="poppins  15 ")
        s_min_title.place(x=10,y=70)

        s_min_sub = Label(s_min, text="Enter Subject", font="poppins 15 ")
        s_min_sub.place(x=10,y=120)

        s_min_time = Label(s_min, text="Enter time repeat", font="poppins 15 ")
        s_min_time.place(x=10,y=170)

        s_title_entry = Entry(s_min, width='40',font="poppins 15 ")
        s_title_entry.place(x=200,y=70)

        s_sub_entry = Entry(s_min, width='40',font="poppins 15 ")
        s_sub_entry.place(x=200,y=120)

        s_time_entry = Entry(s_min, width='10',font="poppins 15 ")
        s_time_entry.place(x=200,y=170)

        min_label = Label(s_min, text="min", font="poppins 15")
        min_label.place(x=295, y=170)

        def a1():
                global a,b,c
                a = int(s_time_entry.get())
                b = s_title_entry.get()
                c = s_sub_entry.get()

                if a=="" or b=="" or c=="":
                        messagebox.showerror("Alert", "All fields are required!")
                else:
                        messagebox.showinfo("notifier set", "set notification ?")
                        s_min.destroy()
                        schedule.every(a).minutes.do(notify)
                        while True:
                                schedule.run_pending()
                                time.sleep(1)

        s_min_but = Button(s_min, width='10', text="Set",font=("poppins", 15, "bold"), command=a1, bg='lightsteelblue')
        s_min_but.pack(side=BOTTOM,pady=10)


        def notify():
                notification.notify(title=b,
                                        message=c,
                                        app_icon="D:\Python PBL\F Code\ico.ico",
                                        timeout=10)
                

        s_min.resizable(0,0)
        s_min.mainloop()