import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amount
    and the period of the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # Add icon
        pdf.image("files/house.png", w=30, h=30)
        # Add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, ln=1, align='C')
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=1, align='C')
        pdf.cell(w=150, h=40, txt=f'{bill.period}', ln=1, border=1, align='C')
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=f'{flatmate1.name}', border=1, align='C')
        pdf.cell(w=150, h=20, txt=f'${flatmate1.pays(bill, flatmate2)}', align='C', border=1, ln=1)
        pdf.cell(w=100, h=20, txt=f'{flatmate2.name}', border=1, align='C')
        pdf.cell(w=150, h=20, txt=f'${flatmate2.pays(bill, flatmate1)}', align='C', border=1, ln=1)

        # Change directory to files, generate and open PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
