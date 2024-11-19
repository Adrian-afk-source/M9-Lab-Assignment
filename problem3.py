#Adrian Garcia
#11/19/24
#This is problem 3 and in this it'll prompt us to give it a number and it'll keep asking us until the sum of the list of numbers is greater than 100.

numbers = []
total_sum = 0
while total_sum <= 100:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input) 
        numbers.append(number)
        total_sum += number  
    except ValueError:
        print("Please enter a valid number.")
print(f"The list of numbers entered: {numbers}")
print(f"The total sum of the numbers is: {total_sum}")