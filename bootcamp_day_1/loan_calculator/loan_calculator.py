def loancalculator(amount, time, rate):
    """
    Function used to calculate the total loan amount repayable_amount

    Args:
    Amount is the principal amount borrowed
    Time is the total duration for the loan repayment
    Rate is the rate of interest

    Returns the total repayable amount
    """
    
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
