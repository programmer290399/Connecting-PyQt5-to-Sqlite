# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        A simple function to setup the UI and link elements to their respective 
        actions.
        """
        # UI setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(10, 20, 231, 71))
        self.name_label.setObjectName("name_label")
        self.event_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.event_label_2.setGeometry(QtCore.QRect(10, 80, 231, 71))
        self.event_label_2.setObjectName("event_label_2")
        self.mobno_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.mobno_label_3.setGeometry(QtCore.QRect(10, 130, 231, 71))
        self.mobno_label_3.setObjectName("mobno_label_3")
        self.sem_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.sem_label_4.setGeometry(QtCore.QRect(10, 180, 231, 71))
        self.sem_label_4.setObjectName("sem_label_4")
        self.Name_textinp = QtWidgets.QTextEdit(self.centralwidget)
        self.Name_textinp.setGeometry(QtCore.QRect(260, 40, 361, 41))
        self.Name_textinp.setObjectName("Name_textinp")
        self.Event_textinp = QtWidgets.QTextEdit(self.centralwidget)
        self.Event_textinp.setGeometry(QtCore.QRect(260, 90, 361, 41))
        self.Event_textinp.setObjectName("Event_textinp")
        self.Mobnum_textinp = QtWidgets.QTextEdit(self.centralwidget)
        self.Mobnum_textinp.setGeometry(QtCore.QRect(260, 140, 361, 41))
        self.Mobnum_textinp.setObjectName("Mobnum_textinp")
        self.sem_textinp = QtWidgets.QTextEdit(self.centralwidget)
        self.sem_textinp.setGeometry(QtCore.QRect(260, 190, 361, 41))
        self.sem_textinp.setObjectName("sem_textinp")
        self.Submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_btn.setGeometry(QtCore.QRect(320, 310, 106, 30))
        self.Submit_btn.setObjectName("Submit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Linking UI elements to their respective actions.
        self.Submit_btn.clicked.connect(self.submit_btn_action)

    def retranslateUi(self, MainWindow):
        """
        A helper function to setup UI 
        It is resposible for putting desired text on the elements
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB_entry_form"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.event_label_2.setText(_translate("MainWindow", "Event"))
        self.mobno_label_3.setText(_translate("MainWindow", "Mobile No."))
        self.sem_label_4.setText(_translate("MainWindow", "Sem."))
        self.Submit_btn.setText(_translate("MainWindow", "Submit"))

    def submit_btn_action(self):

        """
        Submit action function:
        
        This function is triggered when we click the submit button
        This function accomplished the following 3 tasks:

            1.Create a table in the db if it doesn't exists
                using : create_database function
        
            2.Fetch data from the form and create a list of it
        
            3.Insert the fetched data into the db
                using : insert_data function
        """

        # Create a database if it isn't there
        self.create_database()
        # A lambda function to extract text from the text box on the form
        get_txt = lambda txt_inp: txt_inp.toPlainText()
        # Create a list of the fetched data
        data = [
            str(get_txt(input_type))
            for input_type in [
                self.Name_textinp,
                self.Event_textinp,
                self.Mobnum_textinp,
                self.sem_textinp,
            ]
        ]
        # Insert the fetched data into the db
        self.insert_data(data)

    def create_database(self):

        """
        A simple function to create a database
        and a table in it.
        """
        # create a connection with db
        db_conn = sqlite3.connect("test.db")
        db_handle = db_conn.cursor()

        # execute the command to create the table
        # if it doesn't exists.
        db_handle.execute(
            """
            create table if not exists test_tab(
                name  varchar(10),
                event varchar(10),
                mob   varchar(10),
                sem   varchar(10))
            """
        )
        # commit the changes to db
        db_conn.commit()
        # close the connection
        db_conn.close()

    def insert_data(self, data):

        """
        A simple function to insert data into the db. 
        params:
            data (List): A list of data elements (type str) to be inserted
        """

        # create a connection with db
        db_conn = sqlite3.connect("test.db")
        db_handle = db_conn.cursor()
        # execute the command to insert data into db
        db_handle.execute("INSERT INTO test_tab VALUES(?,?,?,?)", tuple(data))
        # commit the changes to db
        db_conn.commit()
        # close the connection
        db_conn.close()


# the code below creates the UI when run directly through terminal
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
