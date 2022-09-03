from tkinter import *

def event():
    root=Tk()
    root.geometry('500x400')
    root.config(bg='lightsteelblue')

    ################################################################################################################################################################

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

    data.close()

    #############################################################################################################################################################################################

    starttime = Label(root, text='Enter Start Time: \n', bg='lightsteelblue', font='comicsansns 10')
    starttime.grid(row=0,column=0)
    stvalue=StringVar()
    stentry=Entry(root, textvariable=stvalue)
    stentry.grid(row=0, column=1)

    endtime = Label(root, text='Enter End Time:  \n', bg='lightsteelblue', font='comicsansns 10')
    endtime.grid(row=1,column=0)
    etvalue=StringVar()
    etentry=Entry(root, textvariable=etvalue)
    etentry.grid(row=1,column=1)

    event = Label(root, text='Enter Event:  \n', bg='lightsteelblue', font='comicsansns 10')
    event.grid(row=2,column=0)
    eventvalue=StringVar()
    evententry=Entry(root, textvariable=eventvalue)
    evententry.grid(row=2,column=1)

    location = Label(root, text='Enter Event Location:  \n', bg='lightsteelblue', font='comicsansns 10')
    location.grid(row=3,column=0)
    locationvalue=StringVar()
    locationentry=Entry(root, textvariable=locationvalue)
    locationentry.grid(row=3,column=1)

    date = Label(root, text='Enter Date: ', bg='lightsteelblue', font='comicsansns 10')
    date.grid(row=5,column=0)
    datevalue=StringVar()
    dateentry=Entry(root, textvariable=datevalue)
    dateentry.grid(row=5,column=1)

    date_format = Label(root, text='dd/mm/yyyy', bg='lightsteelblue')
    date_format.grid(row=5,column=2)

    ###################################################################################################################################################################

    event1value = IntVar()
    event1 = Checkbutton(text="Event 1", variable = event1value, bg='lightsteelblue')
    event1.grid(row=6,column=1)

    event2value = IntVar()
    event2 = Checkbutton(text="Event 2", variable = event2value, bg='lightsteelblue')
    event2.grid(row=7,column=1)

    event3value = IntVar()
    event3 = Checkbutton(text="Event 3", variable = event3value, bg='lightsteelblue')
    event3.grid(row=8,column=1)

    event4value = IntVar()
    event4 = Checkbutton(text="Event 4", variable = event4value, bg='lightsteelblue')
    event4.grid(row=9,column=1)

    event5value = IntVar()
    event5 = Checkbutton(text="Event 5", variable = event5value, bg='lightsteelblue')
    event5.grid(row=10,column=1)

    def get_vals():
        picked_date = datevalue.get().split('/')
        date_split = picked_date[0]
        k = int(date_split)*5

        if event1value.get()==1:
            st_list[k] = stvalue.get()
            et_list[k] = etvalue.get()
            evnt_list[k] = eventvalue.get()
            loc_list[k] = locationvalue.get()

        if event2value.get()==1:
            st_list[k+1] = stvalue.get()
            et_list[k+1] = etvalue.get()
            evnt_list[k+1] = eventvalue.get()
            loc_list[k+1] = locationvalue.get()

        if event3value.get()==1:
            st_list[k+2] = stvalue.get()
            et_list[k+2] = etvalue.get()
            evnt_list[k+2] = eventvalue.get()
            loc_list[k+2] = locationvalue.get() 

        if event4value.get()==1:
            st_list[k+3] = stvalue.get()
            et_list[k+3] = etvalue.get()
            evnt_list[k+3] = eventvalue.get()
            loc_list[k+3] = locationvalue.get()

        if event5value.get()==1:
            st_list[k+4] = stvalue.get()
            et_list[k+4] = etvalue.get()
            evnt_list[k+4] = eventvalue.get()
            loc_list[k+4] = locationvalue.get()

    ##########################################################################################################################################################

        savefile = open("data.txt",'w')
        for i in range (0,150):
            savefile.write(f"{st_list[i]}\n")
            savefile.write(f"{et_list[i]}\n")
            savefile.write(f"{evnt_list[i]}\n")
            savefile.write(f"{loc_list[i]}\n")

    #####################################################################################################################################################################

    Button(text='Save', command=get_vals).grid(row=4,column=1)
    Button(text='Exit', command=root.destroy).grid(row=11,column=1)

    root.mainloop()