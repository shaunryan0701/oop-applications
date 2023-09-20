"""
Creates a pdf file that contains data about the flatmates
such as their names, their due amount and the period of
the bill
"""

import webbrowser
from fpdf import FPDF
import os
from filestack import Client


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

        os.chdir('files')
        pdf.output(f'{self.filename}')

        webbrowser.open(self.filename)

    @staticmethod
    def format_pay_amount(bill, flatmate1, flatmate2):
        return str(round(flatmate1.pays(bill=bill, other_flatmate=flatmate2), 2))


class FileSharer:
    def __init__(self, filepath, api_key='A1MyKk2SQQuCXyltPaN6vz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
