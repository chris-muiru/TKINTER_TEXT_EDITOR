import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
Window=tk.Tk()
Window.title("Simple file editor")
Window.rowconfigure(0,minsize=500,weight=1)
Window.columnconfigure(1,minsize=500,weight=1)
def openFile():
    #askopenfilename represent the filepath
    filepath=askopenfilename(filetypes=[("python files","*.py")])
    MainText.delete(1.0,tk.END)
    with open(filepath,"r") as myfile:
        content=myfile.read()
        MainText.insert(tk.END,content)
    Window.title(f"simple file editor-{filepath}")
    
def saveAs(): 
    filepath=asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
    print(filepath)
    with open(filepath,"w") as file:
        words=MainText.get("1.0",tk.END)
        file.write(words)

Frame=tk.Frame(master=Window)
Frame.grid(row=0,column=0,sticky="ns")
MainText=tk.Text(master=Window,borderwidth=2)
MainText.grid(row=0,column=1,sticky="nsew")
btnOpen=tk.Button(master=Frame,text="Open",command=openFile)
btnSave=tk.Button(master=Frame,text="Save",command=saveAs)
btnOpen.grid(row=0,column=0,pady=5,sticky="e")
btnSave.grid(row=1,column=0,sticky="e")

Window.mainloop()