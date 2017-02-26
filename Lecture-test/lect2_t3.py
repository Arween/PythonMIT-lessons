# outstandingBalance = float(raw_input("Enter the outstanding balance on your credit card: "));
# interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "));


# outstandingBalance = 320000.0;
# interestRate = 0.2

outstandingBalance = 999999;
interestRate = 0.18

monthlyInterestRate = interestRate/12
balance = outstandingBalance
lowerBound = balance / 12.0
upperBound = (balance * (1 + (interestRate / 12.0)) ** 12.0) / 12.0
epsilon = 0.2
monthlyPayment = (upperBound + lowerBound) / 2.0


while (balance > epsilon) or (balance < -epsilon):
    monthlyPayment = (upperBound + lowerBound) / 2.0
    balance = outstandingBalance
    for months in range(1,13):
        balance = (balance * (1 + (interestRate / 12.0))) - monthlyPayment
    if balance > epsilon:
        lowerBound = monthlyPayment
    if balance < -epsilon:
        upperBound = monthlyPayment

print "RESULT";
print "Monthly payment to pay off debt in 1 year: ", monthlyPayment
print "Balance: ", round(balance, 2)