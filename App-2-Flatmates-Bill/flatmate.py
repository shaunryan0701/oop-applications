
"""
Creates a flatmate person who lives ib ethe flat and
pays a share of the bill
"""

from bill import Bill


class FlatMate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount * weight
