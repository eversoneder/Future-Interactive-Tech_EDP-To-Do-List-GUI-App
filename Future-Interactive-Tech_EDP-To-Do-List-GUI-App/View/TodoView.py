from tkinter import *
from tkinter import messagebox
import os

class TodoView:
    '''
    gui interface layout and controls matching wireframe design
    '''

    def __init__(self):
        '''
        constructor, setup main window settings and initialize layout
        '''
        self.root = Tk()
        self.root.title("Future Interactive Technologies - Task Manager")
        self.root.geometry("860x460")
        self.root.minsize(860, 460)
        self.root.config(background="#253342")
        self.buildGUI()

    def buildGUI(self):
        '''
        create outer frames, labels, listboxes, arrow and btns
        '''

        #colors to be used
        bgColor = "#253342"
        frameBgColor = "#1E2A38"
        hbackground = "#3A4D61"

        textColor = "#FFFFFF"

        self.blueBtnBg = "#1B8CD8"
        self.blueBtnHoverBg = "#57C1FF"
        self.blueBtnClicked = "#1572B2"

        self.redBtnBg = "#D9534F"
        self.redBtnHoverBg = "#FF7570"
        self.redBtnClicked = "#B53B37"
        
        

        currentDir = os.path.dirname(os.path.abspath(__file__))#get view folder
        projectRoot = os.path.dirname(currentDir)#get root folder path

        #main window outer container frame
        mainFrame = Frame(self.root, background=bgColor)
        mainFrame.pack(fill=BOTH, expand=True, padx=15, pady=15)

        #################### LEFT PANEL: logo frame & cat frame ####################
        frameLeft = Frame(mainFrame, background=bgColor, width=220)
        frameLeft.pack(side=LEFT, fill=Y, padx=(0, 15))
        frameLeft.pack_propagate(False)

        #################### top left frame (within frameLeft): logo frame ####################
        self.frameLogo = Frame(frameLeft, background=frameBgColor, highlightbackground=hbackground, highlightthickness=1, height=170)
        self.frameLogo.pack(fill=BOTH, pady=(0, 10), expand=True)#pady=(0, 10) = space betwween images

        logoImg = os.path.join(projectRoot, "Assets", "Images", "Future-Interactive-Technologies-Logo.png") #get logo image
        #logoImg = os.path.join(projectRoot, "Assets", "Images", "Future-Interactive-Technologies-Logo1.png") #get logo image
        #logoImg = os.path.join(projectRoot, "Assets", "Images", "Future-Interactive-Technologies-Logob.png") #get logo image
        self.logoImg = PhotoImage(file=logoImg) 
        lblLogoPlaceholder = Label(self.frameLogo, image=self.logoImg, fg="#A0B0C0", background=frameBgColor)
        lblLogoPlaceholder.pack(expand=True)

        #################### bottom left frame (within frameLeft): cat frame ####################
        self.frameCat = Frame(frameLeft, background="#000000", highlightbackground="#3A4D61", highlightthickness=1)
        self.frameCat.pack(fill=X)
        

        # cryingCat = os.path.join(projectRoot, "Assets", "Images", "crying-cat.png") #get crying-cat image
        # self.cryingCat = PhotoImage(file=cryingCat) 
        # lblCatPlaceholder = Label(self.frameCat, image=self.cryingCat, fg="#000000", background="#000000")
        # lblCatPlaceholder.pack(side="left", anchor="s")

        developedByES = os.path.join(projectRoot, "Assets", "Images", "Developed-by-es.png") #get crying-cat image
        self.developedByES = PhotoImage(file=developedByES) 
        lblCatPlaceholder = Label(self.frameCat, image=self.developedByES, fg=frameBgColor, background=frameBgColor)
        lblCatPlaceholder.pack(side="left", anchor="s")

        #################### FrameRight is the base frame for the frameAddTask frame alone ####################
        frameRight = Frame(mainFrame, background=bgColor)
        frameRight.pack(side=TOP, fill=BOTH, expand=True)

        #################### top right: frameAddTask holds all the add task items like the lblInput, txtInput and btnAdd ####################
        frameAddTask = Frame(frameRight, background=bgColor)
        frameAddTask.pack(fill=X, pady=(0, 15))

        lblInput = Label(frameAddTask, text="Add New Task:", font=("Arial", 12, "bold"), fg=textColor, background=bgColor)
        lblInput.pack(side=LEFT, padx=(0, 10))

        self.txtInput = Entry(frameAddTask, font=("Arial", 11), borderwidth=0)
        self.txtInput.pack(side=LEFT, fill=X, expand=True, padx=(0, 10), ipady=4)

        #https://www.geeksforgeeks.org/python/python-creating-a-button-in-tkinter/
        #fg=textColor text color
        #activeforeground=textColor when a btn is clicked, maintain the text color
        #background=blueBtnBg btn backround color
        #activebackground=blueBtnClicked darker blue color for when btn is clicked
        #borderwidth=0 no border
        #padx=15, pady=4 btn paddings
        self.btnAdd = Button(frameAddTask, text="Add Task", font=("Arial", 10, "bold"), background=self.blueBtnBg, fg=textColor, activebackground=self.blueBtnClicked, activeforeground=textColor, borderwidth=0, highlightbackground="#57C1FF", padx=15, pady=4, cursor="hand2")
        self.btnAdd.pack(side=LEFT)

        #################### middle content frame (to-do, arrow, completed) ####################
        frameLists = Frame(frameRight, background=bgColor)
        frameLists.pack(fill=BOTH, expand=True)


        #################### to-do task list frame ####################
        toDoFrame = Frame(frameLists, background=bgColor)
        toDoFrame.pack(side=LEFT, fill=BOTH, expand=True)

        lblToDo = Label(toDoFrame, text="To-Do Task List:", font=("Arial", 11, "bold"), fg=textColor, background=bgColor, anchor="w")
        lblToDo.pack(fill=X, pady=(0, 5))

        ToDoBoxFrame = Frame(toDoFrame, background=bgColor)
        ToDoBoxFrame.pack(fill=BOTH, expand=True, pady=(0, 10))

        #https://tkdocs.com/shipman/relief.html
        #https://tkdocs.com/shipman/listbox.html relief="flat" (flat 2d style so that borderwidth doesn't appear as it is 
        #default set to "sunken" and borderwidth gives some space away from wall), activestyle="none" (remove underline on focused item)
        self.lstPending = Listbox(ToDoBoxFrame, font=("Arial", 10), borderwidth =3, relief="flat", activestyle="none")
        self.lstPending.pack(side=LEFT, fill=BOTH, expand=True)#responsive

        scrollPending = Scrollbar(ToDoBoxFrame, orient=VERTICAL, command=self.lstPending.yview)#scrollbar to to-do list
        scrollPending.pack(side=RIGHT, fill=Y)
        self.lstPending.config(yscrollcommand=scrollPending.set)

        #################### to-do frame btns ####################
        framePendingBtns = Frame(toDoFrame, background=bgColor)
        framePendingBtns.pack(fill=X)

        #dont need padx bc it will be stretched by expand=True
        self.btnMove = Button(framePendingBtns, text="Complete Task", font=("Arial", 9, "bold"), background=self.blueBtnBg, fg=textColor, activebackground=self.blueBtnClicked, activeforeground=textColor, borderwidth=0, pady=6, cursor="hand2")
        self.btnMove.pack(side=LEFT, fill=X, expand=True)

        self.btnRemove = Button(framePendingBtns, text="Delete Task", font=("Arial", 9, "bold"), background=self.redBtnBg, fg=textColor, activebackground=self.redBtnClicked, activeforeground=textColor, borderwidth=0, pady=6, cursor="hand2")
        self.btnRemove.pack(side=LEFT, fill=X, expand=True, padx=(5, 0))


        #################### middle arrow frame ####################
        arrowFrame = Frame(frameLists, background=bgColor, width=40)
        arrowFrame.pack(side=LEFT, fill=Y, padx=10)

        arrowPath = os.path.join(projectRoot, "Assets", "Images", "arrow.png") #get center blue arrow image
        self.arrowImg = PhotoImage(file=arrowPath) 
        lblArrow = Label(arrowFrame, image=self.arrowImg, background=bgColor)
        lblArrow.pack(expand=True)

        #################### completed tasks list frame ####################
        frameCompleted = Frame(frameLists, background=bgColor)
        frameCompleted.pack(side=LEFT, fill=BOTH, expand=True)

        lblCompleted = Label(frameCompleted, text="Completed Tasks List:", font=("Arial", 11, "bold"), fg=textColor, background=bgColor, anchor="w")
        lblCompleted.pack(fill=X, pady=(0, 5))

        frameDoneBox = Frame(frameCompleted, background=bgColor)
        frameDoneBox.pack(fill=BOTH, expand=True, pady=(0, 10))

        self.lstDone = Listbox(frameDoneBox, font=("Arial", 10), background="#FFFFFF", fg="#000000", selectbackground="#1B8CD8", selectforeground=textColor, borderwidth=1, relief=SOLID, activestyle="none")
        self.lstDone.pack(side=LEFT, fill=BOTH, expand=True)

        scrollDone = Scrollbar(frameDoneBox, orient=VERTICAL, command=self.lstDone.yview)#scrollbar to done list
        scrollDone.pack(side=RIGHT, fill=Y)
        self.lstDone.config(yscrollcommand=scrollDone.set)

        #################### completed frame btns ####################
        frameDoneBtns = Frame(frameCompleted, background=bgColor)
        frameDoneBtns.pack(fill=X)

        self.btnRestore = Button(frameDoneBtns, text="Move to To-Do", font=("Arial", 9, "bold"), background=self.blueBtnBg, fg=textColor, activebackground=self.blueBtnClicked, activeforeground=textColor, borderwidth=0, pady=6, cursor="hand2")
        self.btnRestore.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))

        self.btnDelete = Button(frameDoneBtns, text="Delete Completed", font=("Arial", 9, "bold"), background=self.redBtnBg, fg=textColor, activebackground=self.redBtnClicked, activeforeground=textColor, borderwidth=0, pady=6, cursor="hand2")
        self.btnDelete.pack(side=LEFT, fill=X, expand=True, padx=(5, 0))

    def getUserText(self):
        '''
        read text typed in input box
        '''
        return self.txtInput.get().strip()

    def clearUserText(self):
        '''
        clear text input box
        '''
        self.txtInput.delete(0, END)

    def showMessage(self, titleText, messageText, isError=True):
        '''
        show pop up message box
        :param str titleText: title for pop up box
        :param str messageText: details of pop up box
        :param bool isError: flag for error vs info message
        '''
        if isError:
            messagebox.showerror(titleText, messageText)
        else:
            messagebox.showinfo(titleText, messageText)