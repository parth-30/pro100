    class Atm(object):
    def __init__(atmcardnumber,pinnumber,CashWidthdrawl,BalanceEnquiry):
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
        self.CashWIdthdrawl=CashWidthdrawl
        self.BalanceEnquiry=BalanceEnquiry

    def display(self):
        print("What is my balance?")
        return("$50")

    def display(self):
        print("I want to withdraw some cash")
        return("How much do you want to withdraw?")