"""
Object that contains the data about a bill,such as
total amount and period of the bill
"""


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
        pass


bill_amount = 120
the_bill = Bill(amount=bill_amount, period="March 2023")

dave = FlatMate(name='Dave', days_in_house=27)
geoff = FlatMate(name='Geoff', days_in_house=20)


print('Dave pays', dave.pays(bill=the_bill, flatmate2=geoff))
print('Geoff pays', geoff.pays(bill=the_bill, flatmate2=dave))

