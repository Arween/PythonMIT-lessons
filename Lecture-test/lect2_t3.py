outstandingBalance = float(raw_input("Enter the outstanding balance on your credit card: "));
interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "));


monthlyInterestRate = interestRate/12
balance = outstandingBalance
lowerBound = balance / 12.0
upperBound = (balance * (1 + (interestRate / 12.0)) ** 12.0) / 12.0


while balance > 0:
    monthlyPayment = (upperBound + lowerBound) / 2.0
    for months in range(1,13):
        balance = round((balance * (1 + monthlyInterestRate)-monthlyPayment),2)
        if balance <= 0:
            break
    if balance == 0.0:
        outstandingBalance = balance
    elif balance > 0.0:
        balance = outstandingBalance
        lowerBound = monthlyPayment
    else:
        balance = outstandingBalance
        upperBound = monthlyPayment

print "RESULT";
print "Monthly payment to pay off debt in 1 year: ", round(monthlyPayment, 2)
print "Number of months needed: ", months
print "Balance: ", round(balance, 2)