from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout
)

def taxCalculation(result_agi, result_nti, result_ti, result_it, agi, nti):
    if agi and nti:

        if agi.isnumeric() and nti.isnumeric():
            # Convert string to numbers  
            taxIncome = float(agi) - float(nti)
            result_agi.setText("Rp" + f"{float(agi):,}")
            result_nti.setText("Rp" + f"{float(nti):,}")
            result_ti.setText("Rp" + f"{float(taxIncome):,}")

            if taxIncome <= 0:
                result_it.setText('No tax is paid')

            elif taxIncome > 0 and taxIncome <= 50000000:
                incomeTax = taxIncome * 0.05
                result_it.setText("Rp" + f"{float(incomeTax):,}")

            elif taxIncome > 50000000 and taxIncome <= 250000000:
                incomeTax = (0.05 * 50000000) + ((taxIncome - 50000000) * 0.15)
                result_it.setText("Rp" + f"{float(incomeTax):,}")

            elif taxIncome > 250000000 and taxIncome <= 500000000:
                incomeTax = (0.05 * 50000000) + (0.15 * (250000000 - 50000000)) + ((taxIncome - 250000000) * 0.25)
                result_it.setText("Rp" + f"{float(incomeTax):,}")

            elif taxIncome > 500000000:
                incomeTax = (0.05 * 50000000) + (0.15 * (250000000 - 50000000)) + (0.25 * (500000000 - 250000000)) + ((taxIncome - 500000000) * 0.30)
                result_it.setText("Rp" + f"{float(incomeTax):,}")
     
        else:    
            result_it.setText('Input numbers only')

    # Show warning if only 1 column inputed
    else:
        result_it.setText('Input both numbers')
        
def main():
    app = QApplication([])
    window = QWidget()

    # Set title
    window.setWindowTitle('Tax Calculation')

    # Using form layout
    layout = QFormLayout()

    # Define what's is form
    agi = QLabel('Enter Annual Gross Income')
    agi_input = QLineEdit()
    nti = QLabel('Enter Non-Taxable Income')
    nti_input = QLineEdit()
    button = QPushButton('Calculate')   
    label_agi = QLabel('Annual Gross Income: ')
    result_agi = QLabel('')
    label_nti = QLabel('Non-Taxable Income: ')
    result_nti = QLabel('')
    label_ti = QLabel('Taxable Income: ')
    result_ti = QLabel('')
    label_it = QLabel('Income Tax: ')
    result_it = QLabel('')

    button.clicked.connect(lambda : taxCalculation(result_agi, result_nti, result_ti, result_it, agi_input.text(), nti_input.text()))

    layout.addRow(agi, agi_input)
    layout.addRow(nti, nti_input)
    layout.addRow(button)
    layout.addRow(label_agi, result_agi)
    layout.addRow(label_nti, result_nti)
    layout.addRow(label_ti, result_ti)
    layout.addRow(label_it, result_it)

    window.setLayout(layout)
    window.show()
    app.exec_()
    
main()


