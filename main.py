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
        # Add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, ln=1,align='C')
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=100, h=40, txt=f'{bill.period}', ln=1, border=1)
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100, h=20, txt=f'{flatmate1.name}', border=0, align='C')
        pdf.cell(w=100, h=20, txt=f'{flatmate1.pays(bill, flatmate2)}', align='C', border=0, ln=1)
        pdf.cell(w=100, h=20, txt=f'{flatmate2.name}', border=0, align='C')
        pdf.cell(w=100, h=20, txt=f'{flatmate2.pays(bill, flatmate1)}', align='C', border=0, ln=1)

        pdf.output(f'{self.filename}.pdf')


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)
print(f"John Pays: {john.pays(the_bill, marry)}")
print(f"Marry pays: {marry.pays(the_bill, john)}")

report = PdfReport('bill')
report.generate(john, marry, the_bill)