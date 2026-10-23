class Customer:
    def __init__(self, cid, cname, acc_no, balance):
        self.cid = cid
        self.cname = cname
        self.acc_no = acc_no
        self.balance = balance
        self.credit_card = []

    def transfer_funds(self, beneficiary_cust_object, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            beneficiary_cust_object.balance += amount
            print("Transfer successful!")


class Card:
    def __init__(self, card_no, cvv, expiry_date, balance):
        self.card_no = card_no
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.balance = balance


myCustomerList = []
myCardList = []

while True:
    print("Bank Management System")
    print("Menu:")
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer Funds")
    print("4. Assign Card to Customer")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cid = input("Enter Customer ID: ")
        cname = input("Enter Customer Name: ")
        acc_no = input("Enter Account Number: ")
        balance = float(input("Enter Balance: "))

        cust = Customer(cid, cname, acc_no, balance)
        myCustomerList.append(cust)

        print("Customer created successfully.")

    elif choice == "2":
        card_no = input("Enter Card Number: ")
        cvv = input("Enter CVV: ")
        expiry_date = input("Enter Expiry Date: ")
        balance = float(input("Enter Card Balance: "))

        card = Card(card_no, cvv, expiry_date, balance)
        myCardList.append(card)

        print("Card created successfully.")

    elif choice == "3":
        sender_id = input("Enter Sender Customer ID: ")
        receiver_id = input("Enter Receiver Customer ID: ")
        amount = float(input("Enter Amount to Transfer: "))

        sender = None
        receiver = None

        for cust in myCustomerList:
            if cust.cid == sender_id:
                sender = cust
            if cust.cid == receiver_id:
                receiver = cust

        if sender is None or receiver is None:
            print("Customer not found.")
        elif sender == receiver:
            print("Cannot transfer to the same customer.")
        else:
            sender.transfer_funds(receiver, amount)

    elif choice == "4":
        cid = input("Enter Customer ID: ")
        card_no = input("Enter Card Number: ")

        customer = None
        card = None

        for cust in myCustomerList:
            if cust.cid == cid:
                customer = cust

        for c in myCardList:
            if c.card_no == card_no:
                card = c

        if customer is None or card is None:
            print("Customer or Card not found.")
        elif card in customer.credit_card:
            print("Card already assigned to this customer.")
        else:
            already_assigned = False

            for cust in myCustomerList:
                if card in cust.credit_card:
                    already_assigned = True

            if already_assigned:
                print("Card is already assigned to another customer.")
            else:
                customer.credit_card.append(card)
                print("Card assigned successfully.")

    elif choice == "5":
        if len(myCustomerList) == 0:
            print("No customers found.")
        else:
            for cust in myCustomerList:
                print("Customer ID:", cust.cid)
                print("Customer Name:", cust.cname)
                print("Account Number:", cust.acc_no)
                print("Balance:", cust.balance)

                print("Assigned Cards:")
                if len(cust.credit_card) == 0:
                    print("No cards assigned.")
                else:
                    for card in cust.credit_card:
                        print("Card Number:", card.card_no)

    elif choice == "6":
        if len(myCardList) == 0:
            print("No cards found.")
        else:
            for card in myCardList:
                print("Card Number:", card.card_no)
                print("CVV:", card.cvv)
                print("Expiry Date:", card.expiry_date)
                print("Card Balance:", card.balance)

    elif choice == "7":
        print("Thank you for using Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
