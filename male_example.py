class Male:

    # attributes
    name = 'darcy'
    address = 'jungle'
    bank_balance = 100000000

    # constructor
    def __init__(self, name_1, address_1, bank_balance_1):
        self.name = name_1
        self.address = address_1
        self.bank_balance = bank_balance_1

    # funtions / method of class Male
    def update_bb(self, amount, FLAG=False):
        if FLAG == True:
            new_bb = self.bank_balance + amount
            self.bank_balance = new_bb
            print(' your bb would be: ', new_bb)
            return new_bb
        else:
            return self.bank_balance + amount

    @staticmethod
    def find_wealthier(male_1, male_2):
        male_1_flag = isinstance(male_1, Male)
        male_2_flag = isinstance(male_2, Male)

        if any([male_1_flag, male_2_flag]) is False:
            raise Exception(' did not pass 2 males')
        if male_1.bank_balance > male_2.bank_balance:
            print("%s is richer" %male_1.name)
            return male_1
        elif male_2.bank_balance > male_1.bank_balance:
            print("%s is richer" %male_2.name)
            return male_2
        print(' equally rich')


def main():
    x = Male(name_1='Parivesh', address_1='1012 brookhighland lane', bank_balance_1=80000)
    print(x.name)
    print('previous bb was: ', x.bank_balance)
    #print(x.update_bb(20000))
    update_1 = x.update_bb(20000, True)
    print(update_1)
    print('new balance: ', x.bank_balance)

    y=Male(name_1='Bhalu', address_1='Birmingham', bank_balance_1= 50000000)
    richer_guy = Male.find_wealthier(x, y)


if __name__ == "__main__":
    main()


