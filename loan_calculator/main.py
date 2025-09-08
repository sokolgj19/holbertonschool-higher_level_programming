#!/usr/bin/python3
from calculator import calculateMonthlyRepayment, calculateTotalAmountPaid

def main():
    print("Welcome to the Loan Repayment Calculator!\n")

    # User inputs
    principal = float(input("Enter loan amount (e.g., 5000): "))
    annualInterestRate = float(input("Enter annual interest rate (e.g., 5): "))
    loanTerm = int(input("Enter loan term in years (e.g., 5): "))

    # Calculations
    monthlyRepayment = calculateMonthlyRepayment(principal, annualInterestRate, loanTerm)
    totalPayment = calculateTotalAmountPaid(monthlyRepayment, loanTerm)

    # Results
    print(f"\nYour monthly repayment is: {monthlyRepayment:.2f}")
    print(f"The total amount paid over the term is: {totalPayment:.2f}")

if __name__ == "__main__":
    main()