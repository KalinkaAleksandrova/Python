import random

print("Enter minimum value for the number range:")
min_value=int(input())
print("Enter maximum value for the number range:")
max_value=int(input())

random_number=random.randint(min_value, max_value)
counter=0
user_input=0

while user_input!=random_number:
    print(f"Guess the number (between {min_value} and {max_value}):")
    user_input=int(input())
    if user_input<random_number:
        print("Too low! Try again.")
    elif user_input>random_number:
        print("Too high! Try again.")
    elif user_input==random_number:
        print(f"Congratulations! You guessed the number in {counter} attempts.")
    counter+=1
    if counter==5:
        print(f"You run out of attempts. The correct number is {random_number}")
        break


