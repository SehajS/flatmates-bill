import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount: float, period):
        assert amount >= 0, "Amount cannot be negative!"

        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        return round(self.days_in_house/(self.days_in_house + flatmate2.days_in_house) * bill.amount,2)


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
        pdf.image("house.png", w=30, h=30)
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

        pdf.output(f'{self.filename}')

        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)
print(f"John Pays: {john.pays(the_bill, marry)}")
print(f"Marry pays: {marry.pays(the_bill, john)}")

report = PdfReport(filename='bill.pdf')
report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
