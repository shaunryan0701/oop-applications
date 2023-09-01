"""
Object that contains the data about a bill,such as
total amount and period of the bill
"""
import os.path
import webbrowser

from fpdf import FPDF


class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


"""
Creates a flatmate person who lives ib ethe flat and 
pays a share of the bill
"""


class FlatMate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight


"""
Creates a pdf file that contains data about the flatmates
such as their names, their due amount and the period of 
the bill
"""


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt')
        pdf.add_page()

        # Add title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=self.format_pay_amount(bill, flatmate1, flatmate2), border=0, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=self.format_pay_amount(bill, flatmate2, flatmate1), border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))

    @staticmethod
    def format_pay_amount(bill, flatmate1, flatmate2):
        return str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))


bill_amount = 120
the_bill = Bill(amount=bill_amount, period="March 2023")

dave = FlatMate(name='Dave', days_in_house=27)
geoff = FlatMate(name='Geoff', days_in_house=20)

print('Dave pays', dave.pays(bill=the_bill, flatmate2=geoff))
print('Geoff pays', geoff.pays(bill=the_bill, flatmate2=dave))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(dave, geoff, the_bill)

