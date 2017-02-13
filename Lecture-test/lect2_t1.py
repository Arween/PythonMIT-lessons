balance = float(raw_input("Enter the outstanding balance on your credit card: "));
annualInterestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "));
minMonthlyPaymentRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "));

months = 12;
index = 1;
totalAmountPaid = 0;

for i in range(index, months + 1):
    minMonthlyPayment = minMonthlyPaymentRate * balance;
    interestPaid = annualInterestRate / months * balance;
    principlePaid = minMonthlyPayment - interestPaid;
    remainingBalance = balance - principlePaid;
    print ("Month: " + str(i));
    print ("Minimum monthly payment: " + str(round(minMonthlyPayment)));
    print ("Principle paid: " + str(round(principlePaid, 2)));
    print ("Remaining balance: " + str(round(remainingBalance, 2)));
    balance = remainingBalance;
    totalAmountPaid += interestPaid + principlePaid;

print ("Total amount paid: " + str(round(totalAmountPaid, 2)));
print ("Remaining balance: " + str(round(remainingBalance, 2)));