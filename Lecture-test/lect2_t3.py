outstandingBalance = float(raw_input("Enter the outstanding balance on your credit card: "));
interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "));


monthlyInterestRate = interestRate/12
balance = outstandingBalance
monthlyPayment = 0
lowerBound = balance / 12.0
upperBound = (balance * (1 + (interestRate / 12.0)) ** 12.0) / 12.0
epsilon = 0.02


while abs(balance) > epsilon:
    monthlyPayment = (upperBound + lowerBound) / 2
    balance = outstandingBalance
    for i in range(0, 12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment) * monthlyInterestRate)
    if balance > epsilon:
        lowerBound = monthlyPayment
    else:
        upperBound = monthlyPayment


print "RESULT";
print "Monthly payment to pay off debt in 1 year: ", round(monthlyPayment, 2)
print "Balance: ", round(balance, 2)