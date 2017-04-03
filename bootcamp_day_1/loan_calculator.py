def loancalculator(amount, time, rate):
    if time < 1:
        return 'Invalid month'
    else:
        repayable_amount = amount + (amount*(rate/100)*(time/12))
        return repayable_amount


print(loancalculator(100000, 12, 12))
