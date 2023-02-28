apr = 0.25

initBalance = 6200

introPeriod = 18 #months

 

for monthlyPay in range(150, 340, 10):

    month = 1

    balance = initBalance

    while balance > 0:

        balance -= monthlyPay  

        if month > introPeriod:

            balance += balance*(apr/12)

        #print("Month:", month, "| Balance:", balance)

        month += 1

        if month > 48:

            break

    print("Monthly:", monthlyPay, "| Months:", month - 1)
