from collections import defaultdict

def min_transfers(transactions):
  """
  >>> min_transfers([[0,1,40],[1,0,30],[1,4,10],[4,5,15],[0,3,10]])
  3
  >>> min_transfers([[8,2,34],[8,0,69],[9,10,23],[2,1,53],[6,9,63],[4,8,21],[7,0,89],[0,9,29]])
  8
  """
  people = defaultdict(int)
  for transaction in transactions:
    people[transaction[0]] = people[transaction[0]] - transaction[2]
    people[transaction[1]] = people[transaction[1]] + transaction[2]

  credit = []
  debit = []
  for amount in people.values():
    if amount < 0:
      credit.append(-amount)
    if amount > 0:
      debit.append(amount)

  credit.sort()
  debit.sort()
  count = 0
  i = 0
  j = 0
  while j < len(debit):
    amount = min(debit[j], credit[i])
    debit[j] -= amount
    credit[i] -= amount
    count += 1
    if credit[i] == 0:
      i += 1
    if debit[j] == 0:
      j += 1
  return count
