#!/usr/bin/python3

def calculateMonthlyRepayment(principal, annualInterestRate, loanTerm):
    """
    Calculate the monthly repayment using the amortization formula:
    M = P * r * (1 + r)^n / ((1 + r)^n - 1)

    principal: Loan amount
    annualInterestRate: Annual interest rate in %
    loanTerm: Loan term in years
    """
    n = loanTerm * 12  # total number of payments
    r = (annualInterestRate / 100) / 12  # monthly interest rate

    if r == 0:  # handle 0% interest
        return principal / n

    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def calculateTotalAmountPaid(monthlyRepayment, loanTerm):
    """
    Calculate total payment = monthly repayment * total months
    """
    return monthlyRepayment * loanTerm * 12
