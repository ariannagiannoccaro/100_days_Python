"""
student_score = [123, 78, 199, 89, 200, 33]
max = 0
for score in student_score:
	if max <= score:
		max =score
print(max)

total = 0
for number in range(1,101):
    total += number
print(total)
"""
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)