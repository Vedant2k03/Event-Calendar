#Import Python modules
from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from plyer import notification
import schedule 
import time

#User defined modules
import remainder as r
import daily 
import weekly as w
import snooze 
import todolist as tdl
import event

########################################################################################################################################
#Basic Geometry and Background
root = Tk()
root.title('Calendar app')
root.geometry("1300x600")
root.config(bg='lightsteelblue')

##################################################################################################################################################

data = open('data.txt','r')
all_data = data.read()
data_list = all_data.split("\n")
st_list=[]
et_list=[]
evnt_list=[]
loc_list=[]

for n in range (0,600):
    if n%4==0:
        st_list.append(data_list[int(n)])
        
for n in range (0,600):
    if (n-1)%4==0:
        et_list.append(data_list[int(n)])

for n in range (0,600):
    if (n-2)%4==0:
        evnt_list.append(data_list[int(n)])

for n in range (0,600):
    if (n-3)%4==0:
        loc_list.append(data_list[int(n)])        

##################################################################################################################################################

f3 = Frame(root, bg='cornflowerblue', borderwidth=6, relief=GROOVE)
f3.pack(side=RIGHT, fill=Y)

l3 = Label(f3, text="Today's Events:", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 25 bold')
l3.pack()

def events_display():
    date_split = cal.get_date().split("/")
    k = int(date_split[1])*5

    event_l1 = Label(f3, text = f"{st_list[k]} - {et_list[k]} \n{evnt_list[k]} \nLocation: {loc_list[k]}", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 15 bold')
    event_l1.pack(pady=10)
    if st_list[k]=='0' :
        event_l1.destroy()  
    
    event_l2 = Label(f3, text = f"{st_list[k+1]} - {et_list[k+1]} \n{evnt_list[k+1]} \nLocation: {loc_list[k+1]}", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 15 bold')
    event_l2.pack(pady=10)
    if st_list[k+1]=='0' :
        event_l2.destroy()    

    event_l3 = Label(f3, text = f"{st_list[k+2]} - {et_list[k+2]} \n{evnt_list[k+2]} \nLocation: {loc_list[k+2]}", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 15 bold')
    event_l3.pack(pady=10)
    if st_list[k+2]=='0' :
        event_l3.destroy()   

    event_l4 = Label(f3, text = f"{st_list[k+3]} - {et_list[k+3]} \n{evnt_list[k+3]} \nLocation: {loc_list[k+3]}", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 15 bold')
    event_l4.pack(pady=10)
    if st_list[k+3]=='0' :
        event_l4.destroy()  

    event_l5 = Label(f3, text = f"{st_list[k+4]} - {et_list[k+4]} \n{evnt_list[k+4]} \nLocation: {loc_list[k+4]}", bg='cornflowerblue', padx=25, pady=25, font='comicsansns 15 bold')
    event_l5.pack(pady=10)
    if st_list[k+4]=='0' :
        event_l5.destroy()  


############################################################################################################################################################

f2 = Frame(root, bg='mediumslateblue', borderwidth=6, relief=GROOVE)
f2.pack(side=TOP, fill=X)

l2 = Label(f2, text='Event Schedular - Schedule your Day!', bg='mediumslateblue', padx=25, pady=25, font='comicsansns 25 bold')
l2.pack()

#####################################################################################################################################
#Default Calendar view
cal = Calendar(root, selectmode='day', year=2022, day=2, month=7)
cal.pack(pady=15)

##################################################################################################################################################
#Selected Date and Function Display
def grab_date():
    my_label.config(text="Selected date is " + cal.get_date(), font='comicsansns 15 bold')
    options()
    events_display()
    my_button.destroy()

my_button = Button(root, text="Get Date", font='comicsansns 10 ', command = grab_date)
my_button.pack(pady=15)

my_label = Label(root, text="", bg='lightsteelblue')
my_label.pack(pady=15)

####################################################################################################################################################
#Function Calling 
button_frame = Frame(root, bg='lightsteelblue', borderwidth=4, relief=FLAT)
button_frame.pack(pady=15)

def options():
    evnt = Button(button_frame, text="Add Event", font='comicsansns 10', command=destroyandcall)
    evnt.pack(side=LEFT, padx=15)

    reminder = Menubutton(button_frame, text="Add Reminder", font='comicsansns 10')

    re = Menu(reminder, tearoff=0)
    re.add_command(label ='Set Reminder', command = temp1)
    re.add_command(label ='Snooze', command = temp)
    re.add_command(label ='Daily reminder', command = temp2)
    re.add_command(label ='Weekly reminder', command = temp3)
    reminder["menu"] = re

    reminder.pack(side=LEFT, padx=15)

    task = Button(button_frame, text="Add Task", font='comicsansns 10', command= tdl.tdl)
    task.pack(side=LEFT, padx=15)

    #edit = Button(button_frame, text="Edit Schedule", font='comicsansns 10')
    #edit.pack(side=LEFT, padx=15)

def temp():
    root.destroy()
    snooze.min_rem()
def temp1():
    root.destroy()
    r.t()
def temp2():
    root.destroy()
    daily.daily_rem()
def temp3():
    root.destroy()
    w.week_rem()

####################################################################################################################################################   
#Event Function

def destroyandcall():
    root.destroy()
    event.event()

root.mainloop()