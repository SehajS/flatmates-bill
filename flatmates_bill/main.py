from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name?: ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house?: "))
name2 = input("What is the name of the other flatmate?: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house?: "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)
print(f"John Pays: {flatmate1.pays(the_bill, flatmate2)}")
print(f"Marry pays: {flatmate2.pays(the_bill, flatmate1)}")

report = PdfReport(filename=f'{period}.pdf')
report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
