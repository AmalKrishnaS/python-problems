#sum of first N positive numbers

number = int(input('Enter a number: '))

def find_sum(number):
  sum = 0
  for i in range(number+1):
    sum += i
  return sum

sum = find_sum(number)

print(sum)