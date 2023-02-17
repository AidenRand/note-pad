from tkinter import *
from tkinter import font
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

root = Tk()
root.title('Notepad')
root.geometry('500x500')

def save_file():
    f = asksaveasfile(initialfile='Untitled.txt',
                      defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    
def open_file():
    file = askopenfile(mode = 'r', filetypes=[('All Files', '*.*')])
# Save file button
saveBtn = Button(root, text='Save File', command=lambda:save_file())
saveBtn.place(x=0, y=0)

# Open file button
openBtn = Button(root, text='Open File', command=lambda:open_file())
openBtn.place(x=55, y=0)
root.mainloop()

# Create text area
textBox = Entry(root, width=100)
textBox.place(x=10, y=20)