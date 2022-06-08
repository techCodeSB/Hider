import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror, showinfo


class Hide:
    mainfile = None
    secondfile = None
    option = "text"
    key = b"userdata="
    savefile = None

    def __init__(self, r):
        self.root = r
    
    def ui(self):
        self.selectMainButton = Button(
            self.root,
            text="Select main file like image or video",
            command=self.openmainfile,
            width=62,
            height=2,
            relief="groove"
        )
        self.selectMainButton.pack(pady=20)
        # mainfile button is close-----------------------------

        self.div = Frame(self.root)
        self.text = Button(
            self.div,
            text="using text",
            height=2,
            width=30,
            relief='groove',
            command=self.usingText
        )
        self.text.grid(row=0, column=0)
        self.otherfile = Button(
            self.div,
            text="using other file",
            height=2,
            width=30,
            relief='groove',
            command=self.usingOther
        )
        self.otherfile.grid(row=0, column=1)
        self.div.pack()
        # selection button is close------------------------------

        self.usertext = Text(
            self.root,
            width=55,
            height=15,
        )
        self.usertext.pack(pady=20)
        # userttext is close------------------------------------

        self.selectSecondfile = Button(
            self.root,
            text="Select second file",
            command=self.openseconfile,
            width=62,
            height=2,
            relief="groove",
            state=DISABLED
        )
        self.selectSecondfile.pack()
        # second button is close--------------------------------

        self.bind = Button(
            self.root,
            text="BIND",
            width=62,
            height=2,
            relief="groove",
            command=self.bind
        )
        self.bind.pack(pady=20)
        # bind button is close----------------------------------
            

    def openmainfile(self):
        Hide.mainfile = askopenfile(defaultextension=".jpg", mode='ab+', filetypes=[("Image", "*.jpg"),("image", "*.jpeg"), ('Video', '*.mp4'), ('All File', '*.*')])
    
    def openseconfile(self):
        Hide.secondfile = askopenfile(defaultextension=".jpg", mode='ab+', filetypes=[("Image", "*.jpg"),("image", "*.jpeg"), ('Video', '*.mp4'), ('All File', '*.*')])
    # openfile functions close.................................................

    def usingText(self):
        self.usertext.config(bg="white", state=NORMAL)
        self.selectSecondfile.config(state=DISABLED)
        Hide.option = "text"

    def usingOther(self):
        self.usertext.config(bg="lightgrey", state=DISABLED)
        self.selectSecondfile.config(state=NORMAL)
        Hide.option = "file"
    # selection button functions close............................................


    def bind(self):
        if not Hide.mainfile == None:
            if Hide.option == 'text':# for text file bind-------------------
                self.usertextdata = self.usertext.get(0.1, END).strip()
                Hide.mainfile.seek(0)
                self.mainDataRead = Hide.mainfile.read()
                if not self.usertextdata == "":
                    if Hide.key in self.mainDataRead:
                        self.updateTextBind()
                    else:
                        Hide.mainfile.write(Hide.key)
                        Hide.mainfile.write(self.usertextdata.encode())
                        showinfo(title="Hider", message="Successfully bind data....")
                        self.reArrange()
                else:
                    showerror(title="Hider error", message="Enter your text")

            if Hide.option == "file":# for other file bind---------------------------------------
                if not Hide.secondfile == None:
                    Hide.secondfile.seek(0)
                    self.secondFileData = Hide.secondfile.read()
                    Hide.mainfile.seek(0)
                    self.mainDataRead = Hide.mainfile.read()
                    
                    if Hide.key in self.mainDataRead:
                        self.updateFileBind()
                    else:
                        Hide.mainfile.write(Hide.key)
                        Hide.mainfile.write(self.secondFileData)
                        showinfo(title="Hider", message="Successfully bind data....")
                        self.reArrange()
                else:
                    showerror(title="Hider error", message="Choose second file!!")
        else:
            showerror(title="Hider error", message='Select main file')


    def updateTextBind(self):  
        self.mainSplitData = self.mainDataRead.split(Hide.key)
        Hide.mainfile.seek(0)
        Hide.mainfile.truncate()
        try:
            Hide.mainfile.write(self.mainSplitData[0])
            Hide.mainfile.write(Hide.key)
            Hide.mainfile.write(self.usertextdata.encode())
            showinfo(title="Hider", message="Successfully bind data....")
            self.reArrange()
        except:
            showerror(title="Hider error", message="File no bind!!!")
    

    def updateFileBind(self):
        # main file work
        self.mainSplitData = self.mainDataRead.split(Hide.key)
        Hide.secondfile.seek(0)
        self.finalSecondFileData = Hide.secondfile.read()
        Hide.mainfile.seek(0)
        Hide.mainfile.truncate()
        try:
            Hide.mainfile.write(self.mainSplitData[0])                
            Hide.mainfile.write(Hide.key)
            Hide.mainfile.write(self.finalSecondFileData)
            showinfo(title="Hider", message="Successfully bind data....")
            self.reArrange()
        except:
            showerror(title="Hider error", message="File no bind!!!")
    
    def reArrange(self):
        Hide.mainfile = None
        Hide.secondfile = None
        self.usertext.delete(0.1, END)

# ========================== EXTARACT CLASS IS START HERE =====================
class Extract:    
    extractFile = None
    extractOption = None
    key = b"userdata="
    savefile = "Enter file with extension..."

    def __init__(self, r):
        self.root = r
    
    def ui(self):
        self.extractFile = Button(
            self.root,
            text="Select file",
            command=self.openExtractFile,
            width=62,
            height=2,
            relief="groove"
        )
        self.extractFile.pack(pady=20)
        # extract mainfile button is close-----------------------------

        self.div = Frame(self.root)
        self.text = Button(
            self.div,
            text="Text",
            height=2,
            width=30,
            relief='groove',
            command=self.extractTextButton
        )
        self.text.grid(row=0, column=0)
        self.otherfile = Button(
            self.div,
            text="File",
            height=2,
            width=30,
            relief='groove',
            command=self.extractFileButton
        )
        self.otherfile.grid(row=0, column=1)
        self.div.pack()
        # selection button is close------------------------------

        self.extracttext = Text(
            self.root,
            width=55,
            height=15,
        )
        self.extracttext.pack(pady=20)
        # userttext is close------------------------------------

        self.extract = Button(
            self.root,
            text="Extract",
            width=62,
            height=2,
            relief="groove",
            command=self.extract
        )
        self.extract.pack(pady=20)
        # extract button is close----------------------------------

 
    def openExtractFile(self):
        Extract.extractFile = askopenfile(defaultextension=".jpg", mode='rb', filetypes=[("Image", "*.jpg"),("image", "*.jpeg"), ('Video', '*.mp4'), ('All File', '*.*')])

    def extractTextButton(self):
        Extract.extractOption = 'text'
    
    def extractFileButton(self):
        Extract.extractOption = 'file'
        # ---------------------create dialog window to input output file name-----------
        self.dialog = Toplevel(root)
        self.dialog.geometry("520x200")
        self.dialog.title("Extract file details")
        self.dialog.resizable(False, False)
        # self.dialog.iconbitmap(f"{os.getcwd()}\project\hider\logo.ico")
        self.dialog.transient(root)

        self.text = Label(self.dialog,text="") # this label for spacing purpos only
        self.text.pack(pady=10)

        self.filename = Entry(
            self.dialog,
            width=55,
            relief='groove',
            fg='grey'
        )
        self.filename.pack(pady=10, ipady=10)
        self.filename.insert(0,"Enter file with extension...")
        self.filename.bind("<Button-1>", self.entryButton)
        
        self.save = Button(
            self.dialog,
            text="Save",
            relief='groove',
            height=2,
            width=15,
            command=self.dialogButton
        )
        self.save.pack()
        self.dialog.mainloop() #.........extract dialog box end here............
    
    def dialogButton(self):
        self.val = self.filename.get()
        if not self.val == "Enter file with extension..." and not self.val == "":
            Extract.savefile = self.val
            self.dialog.destroy()# quit the dial box after clicking save button
        else:
            showerror(title="fill the input", message="Enter the file name")

    def entryButton(self, e=""):
        self.filename.delete(0, END)
        self.filename.config(fg='black')

    def extract(self):
        if not Extract.extractFile == None:
            self.readExtractFile = Extract.extractFile.read()
            self.splitExtratFile = self.readExtractFile.split(Extract.key)
            if Extract.extractOption == 'text':
                self.extracttext.delete(0.1, END)
                self.extracttext.insert(0.1, self.splitExtratFile[1].decode())

                Extract.extractFile = None
                Extract.extractOption = None
            
            elif Extract.extractOption == 'file':
                if not Extract.savefile == 'Enter file with extension...' and not Extract.savefile == "":   
                    try:
                        if not os.path.isdir('output'):
                            os.mkdir('output')
                        with open(f"output/{Extract.savefile}", 'wb') as handle:
                            handle.write(self.splitExtratFile[1])
                            self.save = os.getcwd()
                            showinfo(title="file save", message=f"file save in {self.save}\output\{Extract.savefile}")

                            self.reArrange()
                    except:
                        showerror(title="Save error", message="file not save")
                        self.reArrange()
                else:
                    showerror(title="Hider error", message="Enter the file name")
                    self.reArrange()

            else:
                showerror(title="Hider error", message='Select option TEXT OR FILE')
        else:
            showerror(title="Hider error", message="Choose the extract file")
    
    def reArrange(self):
        Extract.extractFile = None
        Extract.extractOption = None
        Extract.savefile = "Enter file with extension..."


root = Tk()
root.title("Hider by - Sourav Bishai")
root.geometry("600x580")
# root.resizable(False, False)

# root.iconbitmap(f"{os.getcwd()}\project\hider\logo.ico")
# i = PhotoImage(file='logo.png')
# root.iconphoto(root, i)


tab = ttk.Notebook(root)# notebook for creating tab
hideFrame = ttk.Frame(tab)# hide tab................
hide = Hide(hideFrame)
hide.ui()
tab.add(hideFrame, text="BIND")

extractFrame = ttk.Frame(tab)# extract tab..............
extract = Extract(extractFrame)
extract.ui()
tab.add(extractFrame, text="EXTRACT")
tab.pack(fill=BOTH, expand=True)# pack the tab ttk.Notebook()

# status bar start---------------------------------
status = Frame(
    root,
    bg='blue',
    height=30,
)
copyright = Label(status, text="Copyright © 2022 Sourav | Production", bg="blue", fg="white")
copyright.pack()
status.pack(side=BOTTOM, fill=BOTH)

root.mainloop()
