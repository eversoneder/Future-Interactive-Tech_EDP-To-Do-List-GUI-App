# Future-Interactive-Tech EDP To-Do List GUI App

Desktop task management client featuring relational database persistence, event-driven user interactions, and an elastic dark-mode UI.

![FIT Task Management Application Preview](Assets/Images/todo-app-preview.gif)

## Introduction
The FIT Task Management Application provides an interactive workflow for managing pending tasks and tracking completed items. Designed around the **Event-Driven Programming (EDP)** paradigm, the application processes real-time user inputs, mouse hovers, and keyboard presses to update the interface dynamically.

To keep the codebase maintainable and decoupled, the project strictly follows the **Model-View-Controller (MVC)** architectural pattern. Data access, visual layouts, and event orchestration live in separate modules, making the application straightforward to debug and scale.

## Tech Stack
* **Language & Framework:** Python 3.x with `tkinter` (Standard GUI library)
* **Architecture Pattern:** Model-View-Controller (MVC)
* **Database Management System:** MySQL Server 8.0+
* **Database Driver:** `mysql-connector-python`
* **UI & Layouts:** Tkinter Frames, Listboxes, Scrollbars, and `<KeyPress>`, `<Enter>`, and `<Leave>` Event Bindings

## Directory Structure
```text
Future-Interactive-Tech_EDP-To-Do-List-GUI-App/
│
├── Controller/
│   └── TodoController.py               <-- Handles user events, hover triggers, and view-model coordination
│
├── Model/
│   └── DatabaseModel.py                <-- Manages MySQL connections and SQL query execution
│
├── View/
│   └── TodoView.py                     <-- Builds Tkinter GUI panels, widgets, and color schemes
│
├── Assets/
│   └── Images/
│       ├── arrow.png                   <-- Directional workflow arrow
│       ├── Future-Interactive-Technologies-Logo.png <-- Branding header graphic
│       └── Developed-by-es.png         <-- Developer attribution image
│
└── Future_Interactive_Tech_EDP_To_Do_List_GUI_App.py <-- Primary entry point script
```

## Database Schema Setup
The application connects to a local MySQL database instance. Execute the following script in MySQL Workbench or your command-line SQL client to create the schema and task table:

```sql
CREATE DATABASE IF NOT EXISTS `future_interactive_technologies` 
/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ 
/*!80016 DEFAULT ENCRYPTION='N' */;

USE `future_interactive_technologies`;

CREATE TABLE IF NOT EXISTS `entry` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `itemName` VARCHAR(45) DEFAULT NULL,
  `done` TINYINT DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

> [!NOTE]
> Make sure to update the database connection password inside `Model/DatabaseModel.py` to match your local MySQL configuration.

## Key Features
* **Strict MVC Separation:** Visual presentation (**View**), database logic (**Model**), and event handling (**Controller**) are completely isolated into dedicated layers.
* **Relational Data Integrity:** Queries target unique primary keys (`id`) directly. If entries share identical names, the UI dynamically appends `(ID: {id})` labels to ensure the correct record is updated or deleted.
* **Interactive Event-Driven UI:** Mouse hover listeners (`<Enter>` and `<Leave>`) dynamically brighten button colors (`#1B8CD8` to `#57C1FF` for blue, `#D9534F` to `#FF7570` for red) using `event.widget`. Keyboard bindings support submitting tasks directly via the **Enter** key.
* **Elastic Dashboard Layout:** Uses **Tkinter** geometry settings (`expand=True`, `fill=BOTH`) with a minimum window boundary (`860x460`) so the layout scales cleanly when resized.
* **Defensive Error Handling:** Integrated `tkinter.messagebox` modal alerts notify users of empty text submissions or missing listbox selections without crashing the app.

## Prerequisites
* Python 3.x installed on your system.
* MySQL Server 8.0+ running locally.

## Installation & Running

### 1. Clone the repository
```bash
git clone https://github.com/eversoneder/Future-Interactive-Tech_EDP-To-Do-List-GUI-App.git
cd Future-Interactive-Tech_EDP-To-Do-List-GUI-App
```

### 2. Install dependencies
```bash
pip install mysql-connector-python
```

### 3. Setup the database
Run the SQL creation script provided in the [Database Schema Setup](#database-schema-setup) section inside your MySQL client to generate the database and table structures.

### 4. Configure credentials
Open `Model/DatabaseModel.py` and update the connection details (around line 31) with your local MySQL password:

```python
self.hostName = 'localhost'
self.userName = 'root'
self.password = 'YOUR_MYSQL_PASSWORD'
self.databaseName = 'future_interactive_technologies'
```

### 5. Launch the application
Run the primary entry script from the project root:
```bash
python Future_Interactive_Tech_EDP_To_Do_List_GUI_App.py
```

## Contributors
* **Everson Spinola** - [everson_spinola@hotmail.com](mailto:everson_spinola@hotmail.com)

## Contact
For any queries or support, please contact me at [everson_spinola@hotmail.com](mailto:everson_spinola@hotmail.com).
