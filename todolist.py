
def tdl():
    

  import tkinter
  import tkinter.messagebox
  import pickle

  root = tkinter.Tk()
  root.title("TO DO LIST")

  def add_task():
        task = entry_task.get()
        if task != "":
           listbox_tasks.insert(tkinter.END, task)
           #We are inserting at the END so .end
           entry_task.delete(0, tkinter.END)
        else:
           tkinter.messagebox.showwarning(title="WARNING", message=" enter a task.")

  def delete_task():
       try:
           task_index = listbox_tasks.curselection()[0]
          #curselection = selection of current name or task
          #[0] because we can select multiple items, so 0 to only select first item
           listbox_tasks.delete(task_index)
       except:
          tkinter.messagebox.showwarning(title="WARNING!", message=" select a task.")
        #using try and except because we need to select an item first to delete it.Also stops the program from failing if there is an error. 
  
  def load_tasks():
    # we cannot loading before saving a task
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        #There is an error when we click on load task button as  there is no file present in the current directory, so here also we using try and except function
        #This method returns a specific character or a range of text.
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

  def save_tasks():
    #have to use pickle module [function dump]
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    #Give us task in a form of listtask
    pickle.dump(tasks, open("tasks.dat", "wb"))

#one more thing is remaining ,that is scroll option 
#createing a GUI 
  frame_tasks = tkinter.Frame(root)
  frame_tasks.pack()

  listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
  listbox_tasks.pack(side=tkinter.LEFT)

  scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
  scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

  listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
  scrollbar_tasks.config(command=listbox_tasks.yview)

  entry_task = tkinter.Entry(root, width=50)
  entry_task.pack()

  button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
  button_add_task.pack()

  button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
  button_delete_task.pack()

  button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
  button_load_tasks.pack()

  button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
  button_save_tasks.pack()


  root.mainloop()
    

 