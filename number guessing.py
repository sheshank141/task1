import  random


# Generate a random number between 1 and 100
secret_number = random.randint(1,100)

attempts = 0

print("welcome to the number guessing game ")
print ("I have chosen anumber between 1 and 100.")

while True:
    try:
        guess = int(input("Please enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please try again.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")



