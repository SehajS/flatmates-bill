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
        return round(self.days_in_house/(self.days_in_house + flatmate2.days_in_house) * bill.amount, 2)
