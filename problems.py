#Average of N numbers

number = int(input('Enter the total number of elements: '))

def find_avg(number):
  sum = 0
  for i in range(number):
    sum += int(input('Enter the number: '))
  average = sum / number
  return average

average = find_avg(number)

print(average)
