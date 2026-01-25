# Problem: Optimal Account Balancing

Given a list of transactions, where each transaction is represented as
transaction[i] = [from(i), to(i), amount(i)], indicating the person from(i)
gave amount(i) to person to(i).​

. Return the minimum number of transactions needed to settle all debts.

# Solution

Approach the problem in 3 steps:

Step 1: Calculate the amount each person has. Positive is the debit, Negative is the credit

Step 2: Store credit also as absolute numbers and create credit and debit lists and sort them in place

Step 3: Use a greedy approach, read from debit list and balance out with credit
