def is_armstrong_number(number):
    numbers = str(number)
    calculation = sum(int(x)**len(numbers) for x in numbers)
    return number == calculation
