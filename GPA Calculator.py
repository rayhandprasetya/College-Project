from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QFormLayout, QPushButton, QHeaderView,
    QLabel
)
from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Set title
        self.setWindowTitle('GPA Calculation')

        # Set size
        self.resize(500, 700)

        # Using form layout
        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)
        
        # Add label
        self.result = QLabel('')
        self.result.setAlignment(QtCore.Qt.AlignCenter)  

        self.a = QLabel('')
        self.a.setAlignment(QtCore.Qt.AlignCenter)      # Set the position

        self.a_min = QLabel('')
        self.a_min.setAlignment(QtCore.Qt.AlignCenter)

        self.b_plus = QLabel('')
        self.b_plus.setAlignment(QtCore.Qt.AlignCenter) 

        self.b = QLabel('')
        self.b.setAlignment(QtCore.Qt.AlignCenter)

        self.b_min = QLabel('')
        self.b_min.setAlignment(QtCore.Qt.AlignCenter)

        self.c_plus = QLabel('')    
        self.c_plus.setAlignment(QtCore.Qt.AlignCenter)

        self.c_min = QLabel('')
        self.c_min.setAlignment(QtCore.Qt.AlignCenter)

        self.d = QLabel('')
        self.d.setAlignment(QtCore.Qt.AlignCenter)

        self.e = QLabel('')
        self.e.setAlignment(QtCore.Qt.AlignCenter)

        self.total_index = QLabel('')
        self.total_index.setAlignment(QtCore.Qt.AlignCenter)

        self.total_credit = QLabel('')
        self.total_credit.setAlignment(QtCore.Qt.AlignCenter)

        self.gpa = QLabel('')
        self.gpa.setAlignment(QtCore.Qt.AlignCenter)

        self.button_add = QPushButton('Add Subject')
        self.button_remove = QPushButton('Remove Subject')
        self.button_total = QPushButton('Calculate GPA')

        # Set table
        self.table = QTableWidget()
        
        self.table.setColumnCount(2)
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)


        # Define what is the table header
        self.table.setHorizontalHeaderLabels(['Subject', 'Score'])
        
        # Set position for every label and button
        self.form_layout.addRow(self.button_add)
        self.form_layout.addRow(self.button_remove)
        self.form_layout.addRow(self.button_total)
        self.form_layout.addRow(self.table)
        self.form_layout.addRow(self.result)
        self.form_layout.addRow(self.a)
        self.form_layout.addRow(self.a_min)
        self.form_layout.addRow(self.b_plus)
        self.form_layout.addRow(self.b)
        self.form_layout.addRow(self.b_min)
        self.form_layout.addRow(self.c_plus)
        self.form_layout.addRow(self.c_min)
        self.form_layout.addRow(self.d)
        self.form_layout.addRow(self.e)
        self.form_layout.addRow(self.total_index)
        self.form_layout.addRow(self.total_credit)
        self.form_layout.addRow(self.gpa)

        # Connect the button
        self.button_add.clicked.connect(self.add_subject)
        self.button_remove.clicked.connect(self.remove_subject)
        self.button_total.clicked.connect(self.gpa_calculation)
        self.table.itemChanged.connect(self.score_validate)

    def gpa_calculation(self):
        total_credit = 0
        total_index = 0
        new_total = 0
        gpa = 0
        grade = [0,0,0,0,0,0,0,0,0]
        
        for row in range(0, self.table.rowCount()):
            data = self.table.item(row, 1)          
            if data:
                if data.text():
                    if float(data.text()) >= 85 and float(data.text()) <= 100:
                        grade[0] = grade[0] + 1
                        new_total = 4.00 * 3
                        
                    elif float(data.text()) >= 80 and float(data.text()) < 85:
                        grade[1] = grade[1] + 1
                        new_total = 3.67 * 3
                        
                    elif float(data.text()) >= 75 and float(data.text()) < 80:
                        grade[2] = grade[2] + 1
                        new_total = 3.33 * 3
                        
                    elif float(data.text()) >= 70 and float(data.text()) < 75:
                        grade[3] = grade[3] + 1
                        new_total = 3.00 * 3
                        
                    elif float(data.text()) >= 67 and float(data.text()) < 70:
                        grade[4] = grade[4] + 1
                        new_total = 2.67 * 3
                        
                    elif float(data.text()) >= 64 and float(data.text()) < 67:
                        grade[5] = grade[5] + 11
                        new_total = 2.33 * 3
                        
                    elif float(data.text()) >= 60 and float(data.text()) < 64:
                        grade[6] = grade[6] + 1
                        new_total = 2.00 * 3

                    elif float(data.text()) >= 55 and float(data.text()) < 60:
                        grade[7] = grade[7] + 1
                        new_total = 1.00 * 3

                    elif float(data.text()) >= 0 and float(data.text()) < 55:
                        grade[8] = grade[8] + 1
                        new_total = 0.00 * 3 
                
                    # Calculate total index
                    total_index += new_total 

                    # Calculate total credit
                    total_credit += 3

                    # Calculate gpa
                    gpa = total_index / total_credit

        self.result.setText('Result: \n')    
        self.a.setText('A: %d' % grade[0])  
        self.a_min.setText('A-: %d' % grade[1])       
        self.b_plus.setText('B+: %d' % grade[2])
        self.b.setText('B: %d' % grade[3])
        self.b_min.setText('B-: %d' % grade[4])
        self.c_plus.setText('C+: %d' % grade[5])
        self.c_min.setText('C-: %d' % grade[6])
        self.d.setText('D: %d' % grade[7])
        self.e.setText('E: %d' % grade[8])
        self.total_index.setText('Total Index:' + '{:6.2f}'.format(total_index))
        self.total_credit.setText('Total Credit:' + '{:6.2f}'.format(total_credit))
        self.gpa.setText('GPA :' + '{:6.2f}'.format(gpa))

    def add_subject(self):
        get_row = self.table.rowCount()  
        self.table.insertRow(get_row)  

    def remove_subject(self):
        row_count = self.table.rowCount()
        self.table.removeRow(row_count - 1)

    def score_validate(self, item):
        col = item.column()    
        try:
            # validate the score to get only 0 - 100
            if col == 1 and float(item.text()) > 100 or float(item.text()) < 0:
                item.setText('')  

        except:
            # validate the score to remove string
            if col == 1 and not item.text().isnumeric():
                item.setText('')
                
app = QApplication([])
window = Window()
window.show()
app.exec_()

