import mysql.connector
from tkinter import messagebox

'''
MySQL Workbench create statements for Schema and Entry table:

CREATE DATABASE `future_interactive_technologies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

use future_interactive_technologies;

CREATE TABLE `entry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `itemName` varchar(45) DEFAULT NULL,
  `done` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

NOTE: My MySQL password might not match with yours, change it on line 31 please.
'''

class DatabaseModel:
    '''
    database logic and queries
    '''
    def __init__(self):
        '''
        store the db connection info
        '''
        self.hostName = 'localhost'
        self.userName = 'root'
        self.password = 'root'
        self.databaseName = 'future_interactive_technologies'

    def getConnection(self):
        '''
        db connection using constructor values
        '''
        return mysql.connector.connect(
            host=self.hostName,
            user=self.userName,
            password=self.password,
            database=self.databaseName
        )

    
    def fetchAllTasks(self):
        '''
        db SELECT query to get all items
        '''
        try:
            with self.getConnection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM entry")
                    return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error connecting (DatabaseModel.fetchAllTasks): {e}")
            messagebox.showerror("Database Error", f"Could not load data:\n\nMake sure your Database Password is correctly set at DatabaseModel.py Line 31.\n\n{e}")

    def addTask(self, itemName):
        '''
        insert query to add new task into the db
        :param str itemName: the item to be inserted into db
        '''
        with self.getConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO entry (itemName, done) VALUES (%s, %s)", (itemName, 0))
                conn.commit()

    def markAsDone(self, taskId):
        '''
        update query to set item done status to 1 using unique id
        :param int taskId: unique database primary key id
        '''
        with self.getConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE entry SET done = 1 WHERE id = %s", (taskId,))
                conn.commit()

    def markAsPending(self, taskId):
        '''
        update query to set item done status back to 0 using unique id
        :param int taskId: unique database primary key id
        '''
        with self.getConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE entry SET done = 0 WHERE id = %s", (taskId,))
                conn.commit()

    def deleteTask(self, taskId):
        '''
        delete query to remove item from db using unique id
        :param int taskId: unique database primary key id
        '''
        with self.getConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM entry WHERE id = %s", (taskId,))
            if cursor.rowcount > 0: #successful, has affected a row
                conn.commit()
                return True
            else:
                conn.rollback()
                messagebox.showerror("Error", "Error deleting from the database")
                return False
