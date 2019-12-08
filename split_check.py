import math

def cal_total(total, num_of_people):
  total = float(total)
  num_of_people = int(num_of_people)
  return math.ceil(total / num_of_people)


# Get bill total
print('What\'s the bill total?')
bill_total = input()

# Get total number of people
print('How many people?')
group_total = input()

# Return the outcome 
output = cal_total(bill_total, group_total)
print(f'The total for each is ${output}')
