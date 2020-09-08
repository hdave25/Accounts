class Accounts:
    
    def __init__(self):
        self.bal_save = 10000
        self.bal_check = 10000
        self.type1 = "Savings"
        self.type2 = "Checking"
        self.track_save = []
        self.track_check = []

    def Extract(self, x, type, date):
        s = "Debit"
        if x % 500 != 0 or x < 0:
            print("The value should be positive and multiple of 500!")
            return
        else:
            if type == self.type1:
                self.bal_save -= x
                self.track_save.append(date+" "+s+" "+str(x)+" ")
            elif type == self.type2:
                self.bal_check -= x
                self.track_check.append(date+" "+s+" "+str(x)+" ")
            else:
                print("Please enter correct type of account!")
                return
            
            
    def Add(self, x, type, date):
        s = "Credit"
        if x % 500 != 0 or x < 0:
            print("The value should be positive and multiple of 500!")
            return
        else:
            if type == self.type1:
                self.bal_save += x
                self.track_save.append(date+" "+s+" "+str(x)+" ")
            elif type == self.type2:
                self.bal_check += x
                self.track_check.append(date+" "+s+" "+str(x)+" ")
            else:
                print("Please enter correct type of account!")
                return
    
    def Final(self, type):
        if type == self.type1:
            for i in self.track_save:
                print(i)
            print("Final Balance {0}".format(self.bal_save))
        elif type == self.type2:
            for i in self.track_check:
                print(i)
            print("Final Balance {0}".format(self.bal_check))


acc = Accounts()
acc.Extract(1000, "Savings", "07-09-2020")
acc.Add(500, "Savings", "08-09-2020")
acc.Extract(1500, "Savings", "08-09-2020")
acc.Final("Savings")

acc.Add(1000, "Checking", "07-09-2020")
acc.Extract(2500, "Checking", "07-09-2020")
acc.Add(1500, "Checking", "08-09-2020")
acc.Final("Checking")


