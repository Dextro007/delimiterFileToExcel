# All the 3rd party libraries
import os.path
from tkinter import *
from tkinter import filedialog
# local files 
import transform_path
import to_excel
# Completion popup
def popup(title, message):
    root = Tk()
    root.title(title)
    w = 400
    h = 300
    screenw = root.winfo_screenwidth()
    screenh = root.winfo_screenheight()

    x = (screenw - w)/2
    y = (screenh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    msg = message + '\n'
    lbl = Label(root, text = msg, width= 100, height=10)
    lbl.pack()
    ok = Button(root,text= 'OK', width= 10, command= root.destroy)
    ok.pack()
    root.mainloop()
# for converting csv to excel 
def convert_command():
    #print(transform_path.transformPath(path_text.get()))
    #path = transform_path.transformPath(path_text.get())
    path = path_text.get()
    l = (path.split('/')[-1]).split('.')
    l[-1] = 'xlsx'
    filename = '.'.join(l)
    dest_path = destination_text.get() + '/' + filename
    try:
        to_excel.toexcel(delimiter_text.get(), path, dest_path)
    except Exception as e:
        message = "Error: " + type(e)
        popup("Error", message)
    else:
        popup("Successful", "The file has been converted")


# for getting the file location & name
def get_file():
    ci_server = "//cw01.contiwan.com/root/Loc/rbgs/did02637"
    if(os.path.isdir(ci_server)):
        file = filedialog.askopenfilename(initialdir=ci_server ,title="Select File", filetypes=(("CSV File", "*.csv"), ("all files", "*.*")))
    else:
        file = filedialog.askopenfilename(initialdir = "D:/",title="Select File", filetypes=(("CSV File", "*.csv"), ("all files", "*.*")))
    entry1.insert(0,file)
    print(path_text.get())

def get_destination():
    dest = filedialog.askdirectory(initialdir = "D:/")
    entry2.insert(0,dest)

def help_command():
    popup("Help", "1. Choose the file\n 2. Choose the destination \n 3. Specify the delimiter \n 4. Press Convert Option\n for any query or suggestion\n mail to vivek.kumar@continental-corporation.com")
window = Tk()
window.title('D2E')
window.minsize(width=200, height=200)
label1 = Label(window, text= "File Path")
label1.grid(row= 0, column= 0)

label2 = Label(window, text= "Destination Path")
label2.grid(row = 1,column= 0)

label3 = Label(window, text= "Delimiter")
label3.grid(row= 2, column= 0)

path_text = StringVar()
entry1 = Entry(window, textvariable= path_text)
entry1.grid(row = 0, column = 1)
# to get the destination folder
destination_text = StringVar()
entry2 = Entry(window, textvariable= destination_text)
entry2.grid(row= 1, column= 1)
# To get the delimiter
delimiter_text= StringVar()
entry3 = Entry(window, textvariable= delimiter_text)
entry3.grid(row= 2, column= 1)

# for closing the file
close_button = Button(window, text= 'Close', width= 12, command= window.destroy)
close_button.grid(row= 5, column= 0)
#******************
convert_button = Button(window, text= 'Convert', width= 12, command= convert_command)
convert_button.grid(row= 5, column= 1)

#***********************
file_browse_button= Button(window, text= 'Browse', width= 10, command= get_file)
file_browse_button.grid(row = 0, column = 2)
# button get the destination directory
direct_browse = Button(window, text = "Select",width= 10, command= get_destination)
direct_browse.grid(row=1, column=2)
# help
help_button = Button(window, text= 'Help', width= 12, command= help_command)
help_button.grid(row= 5, column= 2)
window.mainloop()
