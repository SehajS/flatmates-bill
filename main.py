from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data
        name1 = bill_form.name1.data
        name2 = bill_form.name2.data
        days_in_house1 = int(bill_form.days_in_house1.data)
        days_in_house2 = int(bill_form.days_in_house2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)

        return f"{flatmate1.name} pays {flatmate1.pays(the_bill, flatmate2)}"


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in house: ")
    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in house: ")
    button = SubmitField("Calculate...")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.run(debug=True)
