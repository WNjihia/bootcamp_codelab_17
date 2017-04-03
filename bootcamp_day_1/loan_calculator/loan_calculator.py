def loancalculator(amount, time, rate):
    variable_types = (int, float, complex)
    if isinstance(amount, variable_types) and isinstance(time, variable_types) and isinstance(rate, variable_types):
        if amount > 0:
            if time < 1:
                return 'Invalid month'
            else:
                repayable_amount = amount + (amount*(rate/100)*(time/12))
                return repayable_amount
        else:
            return 'Invalid amount'
    else:
        raise ValueError


print(loancalculator(100000, 12, 12))
