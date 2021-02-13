from male import Male


def main():
    x = Male(name_1='Parivesh', address_1='1012 brookhighland lane', bank_balance_1=80000)
    print(x.name)
    print('previous bb was: ', x.bank_balance)
    update_1 = x.update_bb(20000, True)
    print(update_1)
    print('new balance: ', x.bank_balance)

    y = Male(name_1='Bhalu', address_1='Birmingham', bank_balance_1=50000000)
    richer_guy = Male.find_wealthier(x, y)
    print


if __name__ == "__main__":
    main()


