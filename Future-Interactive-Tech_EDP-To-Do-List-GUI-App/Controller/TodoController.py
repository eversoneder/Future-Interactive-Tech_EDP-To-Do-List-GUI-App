from tkinter import *

class TodoController:
    '''
    connect view interactions to model operations
    '''
    def __init__(self, model, view):
        '''
        save class instances and bind event listeners
        :param DatabaseModel model: database model instance
        :param TodoView view: gui view instance
        '''
        self.model = model
        self.view = view
        self.pendingTasks = []#store tuples: (taskId, itemName)
        self.doneTasks = []#store tuples: (taskId, itemName)
        self.bindEvents()
        self.refreshData()

    def bindEvents(self):
        '''
        attach button actions and keypress handlers
        '''
        self.view.btnAdd.config(command=self.handleAdd)
        self.view.btnRemove.config(command=self.handleRemovePending)
        self.view.btnMove.config(command=self.handleMarkDone)
        self.view.btnRestore.config(command=self.handleRestorePending)
        self.view.btnDelete.config(command=self.handleDeleteCompleted)
        self.view.txtInput.bind("<KeyPress>", self.handleKeyPress)

        #https://www.geeksforgeeks.org/python/how-to-bind-the-enter-key-to-a-tkinter-window/
        #hover effect
        #list to bind hover effects
        allBtns = [
            self.view.btnAdd, 
            self.view.btnRemove, 
            self.view.btnMove, 
            self.view.btnRestore, 
            self.view.btnDelete
        ]

        #loop through allBtns list and bind onButtonEnter & onButtonLeave to each one
        for button in allBtns:
            button.bind("<Enter>", self.onButtonEnter)
            button.bind("<Leave>", self.onButtonLeave)

    def onButtonEnter(self, event):
        '''
        change btn background color when mouse enters, according to the 2 hardcoded original colors (self.view.blueBtnBg & self.view.redBtnBg)
        '''
        #https://stackoverflow.com/questions/4299145/getting-the-widget-that-triggered-an-event?__cf_chl_tk=TTaqUec3nb5D6GroWAVqa6qu77F3rQkEtJ73kThwLLA-1786089418-1.0.1.1-rPhtwLdsXdqYEy4eUMJTwyAbUKAhRdV5OfMzM2eUIpc
        #event.widget = the exact button the mouse is currently hovering over
        hoveredBtn = event.widget
        
        # Check the button's current background color to see if it's a blue or red button
        if hoveredBtn["background"] == self.view.blueBtnBg:
            hoveredBtn.config(bg=self.view.blueBtnHoverBg)
            
        elif hoveredBtn["background"] == self.view.redBtnBg:
            hoveredBtn.config(bg=self.view.redBtnHoverBg)

    def onButtonLeave(self, event):
        '''
        restore btn background color when mouse leaves, according to the 2 hardcoded original colors (self.view.blueBtnHoverBg & self.view.redBtnHoverBg)
        '''
        hoveredBtn = event.widget
        
        if hoveredBtn["background"] == self.view.blueBtnHoverBg:
            hoveredBtn.config(bg=self.view.blueBtnBg)
            
        elif hoveredBtn["background"] == self.view.redBtnHoverBg:
            hoveredBtn.config(bg=self.view.redBtnBg)

    def refreshData(self):
        '''
        fetch all data from database and update listboxes with conditional ID display
        '''
        try:
            allRecords = self.model.fetchAllTasks()#goes to DatabaseModel.fetchAllTasks()
            
            self.pendingTasks = [] 
            self.doneTasks = []

            #count occurrences of each task name case insensitively
            nameCounts = {}
            for taskId, itemName, isDone in allRecords:
                lowerName = itemName.lower()#to check if names are equals ignoring case
                nameCounts[lowerName] = nameCounts.get(lowerName, 0) + 1
                
                if isDone == 0:
                    self.pendingTasks.append((taskId, itemName)) #to-do list
                else:
                    self.doneTasks.append((taskId, itemName))#completed list

            #clear existing listbox items
            self.view.lstPending.delete(0, END)
            self.view.lstDone.delete(0, END)

            #populate pending listbox
            for taskId, itemName in self.pendingTasks:
                if nameCounts[itemName.lower()] > 1:
                    displayText = f"{itemName} (ID: {taskId})"
                else:
                    displayText = itemName
                self.view.lstPending.insert(END, displayText)

            #populate completed listbox
            for taskId, itemName in self.doneTasks:
                if nameCounts[itemName.lower()] > 1:
                    displayText = f"{itemName} (ID: {taskId})"
                else:
                    displayText = itemName
                self.view.lstDone.insert(END, displayText)

        except Exception as e:
            print(f"Exception Error (TodoController.refreshData): {e}")

    def handleAdd(self):
        '''
        handle event when user click add button
        '''
        userInputText = self.view.getUserText()
        if len(userInputText) == 0:
            print("Please enter a name for the task first.")
            self.view.showMessage("Error", "Please enter a name for the task first.")
            return

        try:
            self.model.addTask(userInputText)
            print(f"'{userInputText}' added as new task item")
            self.view.clearUserText()
            self.refreshData()
        except Exception as e:
            self.view.showMessage("Database Error", f"Error saving task: {e}")

    def handleRemovePending(self):
        '''
        handle event when user removes item from pending (To-Do) list
        '''
        selectedIndex = self.view.lstPending.curselection()#get selected value
        if not selectedIndex:
            self.view.showMessage("Selection Error", "Please select an item from the To-Do list.")
            return

        itemPosition = selectedIndex[0]
        taskId = self.pendingTasks[itemPosition][0]#get id of selected item
        taskName = self.pendingTasks[itemPosition][1]#get name of selected item
        try:
            if self.model.deleteTask(taskId):#if deletion was successfull, will return true
                print(f"'{taskName}' id: {taskId} deleted")
                self.refreshData()
        except Exception as e:
            self.view.showMessage("Database Error", f"Error deleting task: {e}")

    def handleMarkDone(self):
        '''
        handle event when user moves item to completed list
        '''
        selectedIndex = self.view.lstPending.curselection()
        if not selectedIndex:
            self.view.showMessage("Selection Error", "Please select an item from the To-Do list")
            return

        itemPosition = selectedIndex[0]
        taskId = self.pendingTasks[itemPosition][0]
        taskName = self.pendingTasks[itemPosition][1]
        try:
            self.model.markAsDone(taskId)
            print(f"'{taskName}' id: {taskId} moved to Completed List")
            self.refreshData()
        except Exception as e:
            self.view.showMessage("Database Error", f"Error updating task: {e}")

    def handleRestorePending(self):
        '''
        handle event when user moves completed item back to pending (To-Do) list
        '''
        selectedIndex = self.view.lstDone.curselection()
        if not selectedIndex:
            self.view.showMessage("Selection Error", "Please select an item from the completed list.")
            return

        itemPosition = selectedIndex[0]
        taskId = self.doneTasks[itemPosition][0]
        taskName = self.doneTasks[itemPosition][1]
        try:
            self.model.markAsPending(taskId)
            print(f"'{taskName}' id: {taskId} moved back to To-Do List")
            self.refreshData()
        except Exception as e:
            self.view.showMessage("Database Error", f"Error restoring task: {e}")

    def handleDeleteCompleted(self):
        '''
        handle event when user deletes item from completed list
        '''
        selectedIndex = self.view.lstDone.curselection()
        if not selectedIndex:
            self.view.showMessage("Selection Error", "Please select an item from the completed list.")
            return

        itemPosition = selectedIndex[0]
        taskId = self.doneTasks[itemPosition][0]
        taskName = self.doneTasks[itemPosition][1]
        try:
            if self.model.deleteTask(taskId):
                print(f"'{taskName}' id: {taskId} deleted")
                self.refreshData()
        except Exception as e:
            self.view.showMessage("Database Error", f"Error deleting completed task: {e}")

    def handleKeyPress(self, event):
        '''
        handle event when enter key pressed in input field
        :param Event event: keypress event details
        '''
        if event.keysym == "Return":
            self.handleAdd()