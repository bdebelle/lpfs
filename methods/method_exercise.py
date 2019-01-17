"""
**Exercise**
Tax in US based on states:
Create a method, which takes the state and gross income as the arguments and returns the net income
after deducting tax based on the state.
Assume Federal Tax: 10% Assume state tax on your wish.
You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.
"""

def net_income(gross, state):
    """
    Calculate net income after state and federal taxes
    :param gross: Gross income
    :param state: State
    :return: Net income
    """
    state_tax = {'ca':10, 'tx':5, 'ny':6}
    #calcutate net income after 10% fed tax
    net = gross - (gross * .10)
    #calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your income after taxes is : " + str(net))
        return
    else:
        print("State not in list")
        return None

net_income(80000, 'ca')



