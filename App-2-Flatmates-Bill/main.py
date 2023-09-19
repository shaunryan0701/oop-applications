from bill import Bill
from flatmate import FlatMate
from pdfreport import PdfReport, FileSharer

"""
Creates a flatmate person who lives ib ethe flat and 
pays a share of the bill
"""

bill_amount = float(input('What is the bill amount: '))
period = input('What is the bill period (eg December 2020): ')

the_bill = Bill(amount=bill_amount, period=period)

name1 = input("What is your name: ")
days_in_house1 = int(input(f'How many days was {name1} in the house: '))

name2 = input("What is the name of the other flatmate: ")
days_in_house2 = int(input(f'How many days was {name2} in the house: '))

flatmate1 = FlatMate(name=name1, days_in_house=days_in_house1)
flatmate2 = FlatMate(name=name2, days_in_house=days_in_house2)

print(f'{flatmate1.name} pays', flatmate1.pays(bill=the_bill, other_flatmate=flatmate2))
print(f'{flatmate2.name} pays', flatmate2.pays(bill=the_bill, other_flatmate=flatmate1))

pdf_report = PdfReport(filename=f'{period}.pdf')
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(pdf_report.filename)
print(file_sharer.share())


