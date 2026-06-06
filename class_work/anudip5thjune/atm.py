# ATM Transaction History

transactions = [5000, -2000, 3000, -1000, -500, 7000]

# current balance
balance = 0

# separate lists
deposits = []
withdrawals = []

# process all transactions
for t in transactions:

    # add transaction to balance
    balance = balance + t

    # check deposit or withdrawal
    if t > 0:
        deposits.append(t)
    else:
        withdrawals.append(t)

# assume first values are largest
largest_deposit = deposits[0]
largest_withdrawal = withdrawals[0]

# find largest deposit
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d

# find largest withdrawal
for w in withdrawals:
    if w < largest_withdrawal:
        largest_withdrawal = w

# display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)