'''
@author : Mounika2010
# Assignment-2 - Paying Debt off in a Year

# Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
each month, but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will
pay off all debt in under 1 year, for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at the
end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months. Notice
that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly
interest rate x Monthly unpaid balance)
'''

def payingdebtoffinayear(balance_num, annual_interestrate):
    '''
    This calculates min fixed mothly payment
    '''
    init_balance = balance_num
    moninterest_rate = annual_interestrate/12
    low_i = init_balance/12
    up_i = (init_balance* (1+ moninterest_rate)**12)/12.0
    epsilon = 0.03
    balance_in = init_balance
    while abs(balance_in) > epsilon:
        mon_payrate = (up_i+low_i)/2
        for _ in range(12):
            ans_i = balance_in - mon_payrate
            balance_in = ans_i + (ans_i * moninterest_rate)
        if balance_in > epsilon:
            low_i = mon_payrate
        elif balance_in < -epsilon:
            up_i = mon_payrate
        else:
            break
    return str(round(mon_payrate, 2))
def main():
    '''
    This prog prints min fixed monthly payment
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebtoffinayear(data[0], data[1]))
if __name__ == "__main__":
    main()
