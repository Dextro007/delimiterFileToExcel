from tkinter import *
import transform_path
import to_excel

def convert_command():
    #print(transform_path.transformPath(path_text.get()))
    path = transform_path.transformPath(path_text.get())
    l = (path.split('/')[-1]).split('.')
    l[-1] = 'xlsx'
    filename = '.'.join(l)
    dest_path = destination_text.get() + '\\' + filename
    to_excel.toexcel(delimiter_text.get(), path, dest_path)

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

destination_text = StringVar()
entry2 = Entry(window, textvariable= destination_text)
entry2.grid(row= 1, column= 1)

delimiter_text= StringVar()
entry3 = Entry(window, textvariable= delimiter_text)
entry3.grid(row= 2, column= 1)

close_button = Button(window, text= 'Close', width= 12, command= window.destroy)
close_button.grid(row= 4, column= 0)
#******************
convert_button = Button(window, text= 'Convert', width= 12, command= convert_command)
convert_button.grid(row= 4, column= 1)

#***********************
window.mainloop()
