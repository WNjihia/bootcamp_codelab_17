def loancalculator(amount, time, rate):
    repayable_amount = amount + (amount*(rate/100)*(time/12))
    return repayable_amount


print(loancalculator(100000, 12, 12))
