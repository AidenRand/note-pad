from tkinter import *
from tkinter import font
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

root = Tk()
root.title('Notepad')
root.geometry('500x500')

# Create text area
textBox = Text(root, height=50, width=100, wrap=WORD)
textBox.place(x=0, y=26)

def save_file():
    open_file = asksaveasfile(initialfile='Untitled.txt',
                      defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if open_file is None:
        return
    text = str(textBox.get(1.0, END))
    open_file.write(text)
    open_file.close()
    
def open_file():
    file = askopenfile(mode = 'r', filetypes=[('All Files', '*.*')])
    if file is not None:
        content = file.read()
    textBox.insert(INSERT, content)
# Save file button
saveBtn = Button(root, text='Save File', command=lambda:save_file())
saveBtn.place(x=0, y=0)

# Open file button
openBtn = Button(root, text='Open File', command=lambda:open_file())
openBtn.place(x=55, y=0)
root.mainloop()