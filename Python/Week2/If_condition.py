birth_year = int(input("Please enter your date of birth: "))
current_year = 2024
age = current_year - birth_year
if (age < 13):
    print("You are under age , you cannot watch this movie")
else:
    print("You are enough to watch Avengers, enjoy!")